"""Handle /estimation."""
from ..config import baseConf
from ..OwegaSession import OwegaSession as ps
from ..utils import info_print


def handle_estimation(
    temp_file,
    messages,
    given="",
    temp_is_temp=False,
    silent=False
):
    """Handle /estimation.

    Command description:
        Toggles displaying the token estimation.

    Usage:
        /estimation [on/true/enable/enabled/off/false/disable/disabled]
    """
    given = given.strip()
    if given.lower() in ["on", "true", "enable", "enabled"]:
        baseConf["estimation"] = True
        if not silent:
            info_print("Token estimation enabled.")
        return messages

    if given.lower() in ["off", "false", "disable", "disabled"]:
        baseConf["estimation"] = False
        if not silent:
            info_print("Token estimation disabled.")
        return messages

    baseConf["estimation"] = (not baseConf.get("estimation", False))
    if baseConf.get("estimation", False):
        if not silent:
            info_print("Token estimation enabled.")
    else:
        if not silent:
            info_print("Token estimation disabled.")
    return messages


item_estimation = {
    "fun": handle_estimation,
    "help": "toggles displaying the token estimation",
    "commands": ["estimation"],
}
