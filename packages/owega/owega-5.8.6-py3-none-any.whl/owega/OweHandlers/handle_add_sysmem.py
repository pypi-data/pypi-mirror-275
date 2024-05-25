"""Handle /add_sysmem."""
import prompt_toolkit as pt

from ..OwegaSession import OwegaSession as ps
from ..utils import clrtxt, info_print


# adds a system message
def handle_add_sysmem(
    temp_file,
    messages,
    given="",
    temp_is_temp=False,
    silent=False
):
    """Handle /add_sysmem.

    Command description:
        Adds a system souvenir (permanent).

    Usage:
        /add_sysmem [souvenir]
    """
    given = given.strip()
    if not given:
        try:
            given = ps['main'].prompt(pt.ANSI(
                '\n' + clrtxt("magenta", " System souvenir ") + ": ")).strip()
        except (KeyboardInterrupt, EOFError):
            return messages
    if given:
        messages.add_sysmem(given)
    else:
        if not silent:
            info_print("System souvenir empty, not adding.")
    return messages


item_add_sysmem = {
    "fun": handle_add_sysmem,
    "help": "adds a system souvenir (permanent)",
    "commands": ["add_sysmem"],
}
