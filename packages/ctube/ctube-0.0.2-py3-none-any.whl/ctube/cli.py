import sys
from typing import Optional
from signal import signal, SIGINT
from pytubefix import request
from ctube.app import App
from ctube.paths import MUSIC


def signal_handler(_: Optional[int] = None):
    print('\033[?25h', end="")
    sys.exit(0)


signal(SIGINT, lambda signum, _: signal_handler(signum))

request.default_range_size = request.default_range_size // 15


def main() -> None:
    app = App(output_path=MUSIC)
    app.main_loop()
    signal_handler()


if __name__ == "__main__":
    main()
