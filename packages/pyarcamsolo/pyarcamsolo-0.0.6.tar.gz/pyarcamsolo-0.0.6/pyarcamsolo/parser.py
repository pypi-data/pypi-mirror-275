"""Arcam Parser Helper."""

from .commands import (
    SOURCE_SELECTION_CODES,
    ANSWER_CODES,
    ACCEPTED_ANSWER_CODES,
    COMMAND_CODES,
    POWER_STATUS_CODES,
    CD_PLAYBACK_STATUS_CODES
)

def get_answer_code(ac: bytes) -> str:
    """Return the answer code from the byte."""
    return (list(ANSWER_CODES.keys())[list(ANSWER_CODES.values()).index(ac)])

def get_command_code(cc: bytes) -> str:
    """Return the command code from the byte."""
    return (list(COMMAND_CODES.keys())[list(COMMAND_CODES.values()).index(cc)])

def parse_response(response: bytes) -> dict | list[dict] | None:
    """Convert response bytes into a tuple for the main module to handle."""
    output = {
        "k": "",
        "v": None,
        "z": None
    }
    # Ignore start byte
    output["z"] = response[1:2][0] # Second byte is zone
    cc = response[2:3] # Third byte is command code
    ac = response[3:4] # Forth byte is answer code
    size = response[4:5][0] # Fith byte is length
    data = response[5:(5+size)] # Sixth byte+ is data

    cc = get_command_code(cc)
    # check answer code is valid
    if get_answer_code(ac) not in ACCEPTED_ANSWER_CODES:
        raise ValueError(
            f"Provided response for {cc} is invalid at this time: {get_answer_code(ac)}"
        )

    if cc == "volume":
        output["k"] = cc
        output["v"] = data[0]
    elif cc == "mute":
        output["k"] = "muted"
        output["v"] = bool(data[0])
    elif cc == "source":
        output["k"] = "source"
        output["v"] = SOURCE_SELECTION_CODES.get(data)
    elif cc == "status":
        output["k"] = "power"
        output["v"] = POWER_STATUS_CODES.get(data)
    elif cc == "software_version":
        output["k"] = cc
        output["v"] = f"{data[0]}.{data[1]}"
    elif cc == "rs232_version":
        output["k"] = cc
        output["v"] = f"{data[0]}.{data[1]}"
    elif cc == "balance":
        output["k"] = cc
        output["v"] = (data[0])-100
    elif cc == "bass":
        output["k"] = cc
        output["v"] = bytes_to_int_with_offset(data[0], 2, 0x5D,
                                               range_upper_limit=14)
    elif cc == "treble":
        output["k"] = cc
        output["v"] = bytes_to_int_with_offset(data[0], 2, 0x5D,
                                               range_upper_limit=14)
    elif cc == "display_brightness":
        output["k"] = cc
        output["v"] = data[0]
    elif cc == "stby_display_brightness":
        output["k"] = "standby_display_brightness"
        output["v"] = data[0]
    elif cc == "cd_playback_state":
        output["k"] = cc
        output["v"] = CD_PLAYBACK_STATUS_CODES.get(data, "Unknown")
    elif cc == "cdusb_playback_time":
        output["k"] = "current_track_position"
        hour = int.from_bytes(data[0:1]) * 3600
        minute = int.from_bytes(data[1:2]) * 60
        sec = int.from_bytes(data[2:3])
        output["v"] = hour+minute+sec
    elif cc == "cdusb_current_track":
        return parse_cdusb_current_track(
            z=output["z"],
            b=data
        )

    return output if output["v"] is not None else None


def parse_cdusb_current_track(z: int, b: bytes) -> list[dict]:
    """Parse CD / USB Current Track info."""
    current_folder = int.from_bytes(b[0:1])
    total_folder = int.from_bytes(b[1:2])
    msb_current_track = int.from_bytes(b[2:3])
    lsb_current_track = int.from_bytes(b[3:4])
    msb_total_track = int.from_bytes(b[4:5])
    lsb_total_track = int.from_bytes(b[5:6])
    return [
        {
            "k": "current_folder",
            "v": current_folder,
            "z": z
        },
        {
            "k": "total_folder",
            "v": total_folder,
            "z": z
        },
        {
            "k": "msb_current_track",
            "v": msb_current_track,
            "z": z
        },
        {
            "k": "lsb_current_track",
            "v": lsb_current_track,
            "z": z
        },
        {
            "k": "msb_total_track",
            "v": msb_total_track,
            "z": z
        },
        {
            "k": "lsb_total_track",
            "v": lsb_total_track,
            "z": z
        },
    ]

def bytes_to_int_with_offset(b: bytes, offset: int, normalizer, range_upper_limit: int):
    """Converts bytes to an int with a provided offset"""
    i = int.from_bytes(b, byteorder='big', signed=True)
    # apply a base range from a normalizer
    i -= normalizer
    # now apply scaling using the offset provided
    i *= offset
    i -= range_upper_limit
    return i
