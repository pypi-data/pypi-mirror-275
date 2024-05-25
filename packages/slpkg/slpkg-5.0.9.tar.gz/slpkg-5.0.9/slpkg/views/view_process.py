#!/usr/bin/python3
# -*- coding: utf-8 -*-


import time

from multiprocessing import Process
from slpkg.configs import Configs
from slpkg.utilities import Utilities
from slpkg.progress_bar import ProgressBar
from slpkg.views.asciibox import AsciiBox


class ViewProcess(Configs):
    """View the process messages."""

    def __init__(self, flags: list):
        super(Configs, self).__init__()

        self.progress = ProgressBar()
        self.utils = Utilities()
        self.ascii = AsciiBox()

        self.bar_process = None

        self.option_for_progress_bar: bool = self.utils.is_option(
            ('-B', '--progress-bar'), flags)

    def message(self, message: str) -> None:
        """Show spinner with message or message."""
        if self.progress_bar_conf or self.option_for_progress_bar:
            self.bar_process = Process(target=self.progress.progress_bar, args=(message,))
            self.bar_process.start()
        else:
            print(f'\r{message}... ', end='')

    def done(self) -> None:
        """Show done message."""
        if self.progress_bar_conf or self.option_for_progress_bar:
            time.sleep(0.1)
            self.bar_process.terminate()
            self.bar_process.join()
            print(f'\b{self.bgreen}{self.ascii.done}{self.endc}', end='')
            print('\x1b[?25h')  # Reset cursor after hiding.
        else:
            print(f'{self.bgreen}{self.ascii.done}{self.endc}')

    def failed(self) -> None:
        """Show for failed message."""
        if self.progress_bar_conf or self.option_for_progress_bar:
            time.sleep(0.1)
            self.bar_process.terminate()
            self.bar_process.join()
            print(f'\b{self.bred}{self.ascii.failed}{self.endc}', end='')
            print('\x1b[?25h')  # Reset cursor after hiding.
        else:
            print(f'{self.bred}{self.ascii.failed}{self.endc}')
