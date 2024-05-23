import shutil
from typing import List
from ctube.cmds import Commands, get_cmd_by_name
from ctube.colors import color, Color
from ctube.containers import MusicItem


def print_header() -> None:
    print(color("░█▀▀░▀█▀░█░█░█▀▄░█▀▀░", Color.GREEN))
    print(color("░█░░░░█░░█░█░█▀▄░█▀▀░", Color.GREEN))
    print(color("░▀▀▀░░▀░░▀▀▀░▀▀░░▀▀▀░", Color.GREEN))
    print(f"\u2022 {color('version', Color.BOLD)}: {color('0.0.2', Color.BLUE)}")
    print("\u2022 source: https://github.com/g3nsy/ctube")
    print("\u2022 Type 'help' to list the available commands")


def print_info(cmd_name: str) -> None:
    try:
        cmd_obj = get_cmd_by_name(cmd_name)
        print(cmd_obj.value.description)
    except KeyError:
        print(color(f"Invalid argument for command 'info': {cmd_name}", Color.RED))
        print(color(f"Valid arguments are {Commands.INFO.value.accepted_args}", Color.RED))


def print_help() -> None:
    print(color("Commands overview", Color.GREEN))
    for cmd in Commands:
        print(f"\u2022 {color(cmd.value.name, Color.BOLD)}", end=" ")
        print(color(cmd.value.description, Color.BLUE))


def print_music_items(music_items: List[MusicItem]) -> None:
    terminal_columns = shutil.get_terminal_size().columns
    max_index_len = len(str(len(music_items)))
    space_for_title = terminal_columns - max_index_len - 3  # [, ], ' '
    for i, music_item in enumerate(music_items):
        if len(music_item.title) > space_for_title:
            title = f"{music_item.title[:space_for_title - 3]}..."
        else:
            title = music_item.title
        lb = color("[", Color.BLUE)
        rb = color("]", Color.BLUE)
        ci = color(str(i), Color.GREEN)
        print(f"{lb}{ci}{rb}{' ' * (1 + max_index_len - len(str(i)))}{title}")


