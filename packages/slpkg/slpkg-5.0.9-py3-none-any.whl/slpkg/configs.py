#!/usr/bin/python3
# -*- coding: utf-8 -*-


try:
    import tomli
except ModuleNotFoundError:
    import tomllib as tomli

import platform
from typing import Any
from pathlib import Path
from dataclasses import dataclass

from slpkg.toml_errors import TomlErrors


@dataclass
class Configs:  # pylint: disable=[R0902]
    """Default configurations."""

    toml_errors = TomlErrors()

    prog_name: str = 'slpkg'
    tmp_path: Path = Path('/tmp')
    tmp_slpkg: Path = Path(tmp_path, prog_name)
    build_path: Path = Path(tmp_path, prog_name, 'build')
    etc_path: Path = Path('/etc', prog_name)
    lib_path: Path = Path('/var/lib', prog_name)
    log_path: Path = Path('/var/log/', prog_name)
    log_packages: Path = Path('/var', 'log', 'packages')

    deps_log_file: Path = Path(log_path, 'deps.log')
    slpkg_log_file: Path = Path(log_path, 'slpkg.log')
    upgrade_log_file: Path = Path(log_path, 'upgrade.log')

    os_arch: str = platform.machine()
    file_list_suffix: str = '.pkgs'
    installpkg: str = 'upgradepkg --install-new'
    reinstall: str = 'upgradepkg --reinstall'
    removepkg: str = 'removepkg'
    kernel_version: str = True
    colors: bool = True
    makeflags: str = '-j4'
    gpg_verification: bool = False
    checksum_md5: bool = True
    dialog: bool = True
    view_missing_deps: bool = True
    delete_sources: bool = False
    downloader: str = 'wget'
    wget_options: str = '--c -q --progress=bar:force:noscroll --show-progress'
    curl_options: str = ''
    lftp_get_options: str = '-c get -e'
    lftp_mirror_options: str = '-c mirror --parallel=100 --only-newer --delete'
    download_only_path: Path = Path(tmp_slpkg, '')
    ascii_characters: bool = True
    ask_question: bool = True
    parallel_downloads: bool = False
    maximum_parallel: int = 5
    progress_bar_conf: bool = False
    progress_spinner: str = 'pixel'
    spinner_color: str = 'green'
    border_color: str = 'bold_green'
    process_log: bool = True

    urllib_retries: Any = False
    urllib_redirect: Any = False
    urllib_timeout: float = 3.0

    proxy_address: str = ''
    proxy_username: str = ''
    proxy_password: str = ''

    try:
        # Load user configuration.
        configs = {}
        config_path_file = Path(etc_path, f'{prog_name}.toml')
        if config_path_file.exists():
            with open(config_path_file, 'rb') as conf:
                configs = {k.lower(): v for k, v in tomli.load(conf).items()}

        if configs:
            config = {k.lower(): v for k, v in configs['configs'].items()}

            os_arch: str = config['os_arch']
            file_list_suffix: str = config['file_list_suffix']
            installpkg: str = config['installpkg']
            reinstall: str = config['reinstall']
            removepkg: str = config['removepkg']
            kernel_version: str = config['kernel_version']
            colors: bool = config['colors']
            makeflags: str = config['makeflags']
            gpg_verification: bool = config['gpg_verification']
            checksum_md5: bool = config['checksum_md5']
            dialog: bool = config['dialog']
            view_missing_deps: bool = config['view_missing_deps']
            delete_sources: bool = config['delete_sources']
            downloader: str = config['downloader']
            wget_options: str = config['wget_options']
            curl_options: str = config['curl_options']
            lftp_get_options: str = config['lftp_get_options']
            lftp_mirror_options: str = config['lftp_mirror_options']
            download_only_path: Path = Path(config['download_only_path'])
            ascii_characters: bool = config['ascii_characters']
            ask_question: bool = config['ask_question']
            parallel_downloads: bool = config['parallel_downloads']
            maximum_parallel: int = config['maximum_parallel']
            progress_bar_conf: bool = config['progress_bar']
            progress_spinner: str = config['progress_spinner']
            spinner_color: str = config['spinner_color']
            border_color: str = config['border_color']
            process_log: bool = config['process_log']

            urllib_retries: Any = config['urllib_retries']
            urllib_redirect: Any = config['urllib_redirect']
            urllib_timeout: float = config['urllib_timeout']

            proxy_address: str = config['proxy_address']
            proxy_username: str = config['proxy_username']
            proxy_password: str = config['proxy_password']

    except (KeyError, tomli.TOMLDecodeError) as error:
        toml_errors.raise_toml_error_message(error, toml_file=Path('/etc/slpkg/slpkg.toml'))

    blink: str = ''
    bold: str = ''
    red: str = ''
    bred: str = ''
    green: str = ''
    bgreen: str = ''
    yellow: str = ''
    byellow: str = ''
    cyan: str = ''
    bcyan: str = ''
    blue: str = ''
    bblue: str = ''
    grey: str = ''
    violet: str = ''
    endc: str = ''

    if colors:
        blink: str = '\033[32;5m'
        bold: str = '\033[1m'
        red: str = '\x1b[91m'
        bred: str = f'{bold}{red}'
        green: str = '\x1b[32m'
        bgreen: str = f'{bold}{green}'
        yellow: str = '\x1b[93m'
        byellow: str = f'{bold}{yellow}'
        cyan: str = '\x1b[96m'
        bcyan: str = f'{bold}{cyan}'
        blue: str = '\x1b[94m'
        bblue: str = f'{bold}{blue}'
        grey: str = '\x1b[38;5;247m'
        violet: str = '\x1b[35m'
        endc: str = '\x1b[0m'

    # Creating the paths if not exists
    paths = [
        lib_path,
        etc_path,
        build_path,
        tmp_slpkg,
        log_path,
        download_only_path,
    ]

    for path in paths:
        if not path.is_dir():
            path.mkdir(parents=True, exist_ok=True)
