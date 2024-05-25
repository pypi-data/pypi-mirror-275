#!/usr/bin/python3
# -*- coding: utf-8 -*-


import os
from pathlib import Path

from slpkg.configs import Configs
from slpkg.utilities import Utilities
from slpkg.dialog_box import DialogBox
from slpkg.error_messages import Errors


class FormConfigs(Configs):
    """Edit slpkg.toml config file with dialog utility."""

    def __init__(self):
        super(Configs).__init__()
        self.dialogbox = DialogBox()
        self.errors = Errors()
        self.utils = Utilities()

        self.orig_configs: list = []
        self.config_file: Path = Path(self.etc_path, f'{self.prog_name}.toml')

    def is_dialog_enabled(self) -> None:
        """Check if the dialog box is enabled by the user."""
        if not self.dialog:
            self.errors.raise_error_message(f"You should enable the dialog in the "
                                            f"'{self.etc_path}/{self.prog_name}.toml' file", exit_status=1)

    def edit(self) -> None:
        """Read and write the configuration file."""
        self.is_dialog_enabled()
        elements: list = []
        height: int = 9
        width: int = 0
        form_height: int = 0
        text: str = f'Edit the configuration file: {self.config_file}'
        title: str = ' Configuration File '

        # Creating the elements for the dialog form.
        for i, (key, value) in enumerate(self.configs['configs'].items(), start=1):
            if value is True:
                value: str = 'true'
            elif value is False:
                value: str = 'false'
            elements.extend(
                [(key, i, 1, str(value), i, 21, 47, 200, '0x0', f'Config: {key} = {value}')]
            )

        code, tags = self.dialogbox.mixedform(text, title, elements, height, width, form_height)

        os.system('clear')

        if code == 'help':
            tags = self.configs.values()
            self.help()

        check: bool = self.check_configs(tags)

        if code == 'ok' and check:
            self.write_file(tags)

        elif not check:
            self.edit()

    def help(self) -> None:
        """Load the configuration file on a text box."""
        self.dialogbox.textbox(str(self.config_file), 40, 60)
        self.edit()

    def check_configs(self, tags: list) -> bool:
        """Check for true of false values."""
        keys: list = [
            'COLORS',
            'DIALOG',
            'VIEW_MISSING_DEPS',
            'DELETE_SOURCES',
            'SILENT_MODE',
            'ASCII_CHARACTERS',
            'ASK_QUESTION',
            'KERNEL_VERSION',
            'PARALLEL_DOWNLOADS',
            'PROGRESS_BAR',
            'SPINNING_BAR',
            'CASE_INSENSITIVE',
            'PROCESS_LOG',
            'URLLIB_RETRIES',
            'URLLIB_REDIRECT',
            'GPG_VERIFICATION',
            'CHECKSUM_MD5'
        ]
        values: list = ['true', 'false']

        for key, value in zip(self.configs['configs'].keys(), tags):

            if key in keys and value not in values:
                self.dialogbox.msgbox(f"\nError: Value for '{key}', it must be 'true' or 'false.'\n",
                                      height=7, width=60)
                return False

            if key in ['DOWNLOADER'] and value not in ['wget2', 'wget', 'curl', 'lftp']:
                self.dialogbox.msgbox(f"\nError: Value for '{key}' not supported.\n",
                                      height=7, width=60)
                return False

        return True

    def read_configs(self) -> None:
        """Read the original config file."""
        with open(self.config_file, 'r', encoding='utf-8') as toml_file:
            self.orig_configs: list = toml_file.readlines()

    def write_file(self, tags: list) -> None:
        """Write the new values to the config file."""
        self.read_configs()

        with open(self.config_file, 'w', encoding='utf-8') as patch_toml:
            for line in self.orig_configs:
                for key, value in zip(self.configs['configs'].keys(), tags):

                    if line.lstrip().startswith(f'{key} ='):
                        line = f'  {key} = "{value}"\n'

                    if line.lstrip().startswith(

                            ('COLORS =',
                             'DIALOG =',
                             'VIEW_MISSING_DEPS =',
                             'DELETE_SOURCES =',
                             'SILENT_MODE =',
                             'ASCII_CHARACTERS =',
                             'ASK_QUESTION =',
                             'KERNEL_VERSION =',
                             'PARALLEL_DOWNLOADS =',
                             'MAXIMUM_PARALLEL = ',
                             'PROGRESS_BAR =',
                             'SPINNING_BAR =',
                             'CASE_SENSITIVE =',
                             'PROCESS_LOG =',
                             'URLLIB_RETRIES =',
                             'URLLIB_REDIRECT =',
                             'URLLIB_TIMEOUT =',
                             'GPG_VERIFICATION =',
                             'CHECKSUM_MD5 =')
                    ):
                        line: str = line.replace('"', '')

                patch_toml.write(line)
