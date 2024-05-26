import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Torrent Watcher Script")

    parser.add_argument(
        "--generate-config",
        action="store_true",
        help="Generate configuration file",
    )
    parser.add_argument(
        "--config",
        type=str,
        help="Specify a custom configuration file path",
    )
    parser.add_argument(
        "--history",
        action="store_true",
        help="Show torrent history",
    )
    parser.add_argument(
        "--ui",
        type=str,
        choices=["rofi", "curses"],
        default="curses",
        help="Choose the UI: rofi or curses",
    )
    parser.add_argument(
        "--player",
        type=str,
        choices=["mpv", "vlc"],
        default="mpv",
        help="Choose the Player: mpv or vlc",
    )

    return parser.parse_args()
