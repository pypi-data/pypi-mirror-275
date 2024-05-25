#!/usr/bin/python3
# -*- coding: utf-8 -*-


import shutil
from pathlib import Path

from slpkg.configs import Configs
from slpkg.load_data import LoadData
from slpkg.utilities import Utilities
from slpkg.repositories import Repositories


class RepoInfo(Configs):  # pylint: disable=[R0902]
    """View information about repositories."""

    def __init__(self, flags: list, repository: str):
        super(Configs, self).__init__()
        self.flags: list = flags
        self.repository: str = repository

        self.load_data = LoadData(flags)
        self.utils = Utilities()
        self.repos = Repositories()
        self.columns, self.rows = shutil.get_terminal_size()
        self.name_alignment: int = self.columns - 61

        self.name_alignment = max(self.name_alignment, 1)

        self.enabled: int = 0
        self.total_packages: int = 0
        self.repo_data: dict = {}
        self.dates: dict = {}

        self.option_for_repository: bool = self.utils.is_option(
            ('-o', '--repository'), flags)

    def info(self) -> None:
        """Print information about repositories."""
        self.load_repo_data()

        self.view_the_title()

        if self.option_for_repository:
            self.view_the_repository_information()
        else:
            self.view_the_repositories_information()

    def load_repo_data(self) -> None:
        """Load repository data."""
        self.dates: dict = self.repo_information()
        if self.option_for_repository:
            self.repo_data: dict = self.load_data.load(self.repository)
        else:
            self.repo_data: dict = self.load_data.load('*')

    def repo_information(self) -> dict:
        """Load repository information.

        Returns:
            dict: Description
        """
        repo_info_json: Path = Path(f'{self.repos.repositories_path}', self.repos.repos_information)
        if repo_info_json.is_file():
            repo_info_json: Path = Path(f'{self.repos.repositories_path}', self.repos.repos_information)
            return self.utils.read_json_file(repo_info_json)
        return {}

    def view_the_title(self) -> None:
        """Print the title."""
        title: str = 'repositories information:'.title()
        if self.option_for_repository:
            title: str = 'repository information:'.title()
        print(f'\n{title}')
        print('=' * (self.columns - 1))
        print(f"{'Name:':<{self.name_alignment}}{'Status:':<14}{'Last Updated:':<34}{'Packages:':>12}")
        print('=' * (self.columns - 1))

    def view_the_repository_information(self) -> None:
        """Print the repository information."""
        args: dict = {
            'repo': self.repository,
            'date': 'None',
            'count': 0,
            'color': self.red,
            'status': 'Disable'
        }

        if self.dates.get(self.repository):
            args['date']: str = self.dates[self.repository].get('last_updated', 'None')

        if self.repos.repositories[self.repository]['enable']:
            self.enabled += 1
            args['status'] = 'Enabled'
            args['color'] = self.green
            args['count'] = len(self.repo_data)

        self.view_the_line_information(args)
        self.view_summary_of_all_repositories()

    def view_the_repositories_information(self) -> None:
        """Print the repositories information."""
        args: dict = {}
        for repo, conf in self.repos.repositories.items():
            args: dict = {
                'repo': repo,
                'date': 'None',
                'count': 0,
                'color': self.red,
                'status': 'Disable'
            }

            if self.dates.get(repo):
                args['date']: str = self.dates[repo].get('last_updated', 'None')

            if conf['enable']:
                self.enabled += 1
                args['status'] = 'Enabled'
                args['color'] = self.green
                args['count'] = len(self.repo_data[repo])

            self.view_the_line_information(args)
        self.view_summary_of_all_repositories()

    def view_the_line_information(self, args: dict) -> None:
        """Print the row of information.

        Args:
            args (dict): Arguments for print.
        """
        repository: str = args['repo']
        repo_color: str = self.cyan
        if args['repo'] == self.repos.default_repository:
            repo_color: str = self.byellow
            repository: str = f"{args['repo']} (default)"

        print(f"{repo_color}{repository:<{self.name_alignment}}{self.endc}{args['color']}{args['status']:<14}"
              f"{self.endc}{args['date']:<34}{self.yellow}{args['count']:>12}{self.endc}")

    def view_summary_of_repository(self) -> None:
        """Print the repository summary."""
        print('=' * (self.columns - 1))
        print(f"{self.grey}Total {self.total_packages} packages available from the '{self.repository}' repository.\n")

    def view_summary_of_all_repositories(self) -> None:
        """Print the total summary of repositories."""
        print('=' * (self.columns - 1))
        print(f"{self.grey}Total of {self.enabled}/{len(self.repos.repositories)} "
              f"repositories are enabled with {self.total_packages} packages available.\n")
