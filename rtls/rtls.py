# -*- coding: utf-8 -*-

"""Main module."""

import logging

from rtls import config
from rtls.lib.git import GitLocator
from rtls.lib.rpm import RpmLocator
from rtls.lib.compose import ComposeLocator
from rtls.lib.container import ContainerLocator


LOGGER = logging.getLogger("rtls")
LOGGER.setLevel(logging.INFO)


class Locator(object):
    """Provides functions to locate a patch through its life cycle"""

    def __init__(self, distroinfo_path='', logger=None):
        """Constructor for Locator object

            :param str distroinfo_path: Path to local or remote distroinfo repo
            :param logging.Logger logger: A pre-configured Python Logger object
        """
        self._git = None
        self._rpm = None
        self._container = None
        self._compose = None

        self.distro_info = config.setup_distro_info(distroinfo_path)
        self._setup_logger(logger)

    def _setup_logger(self, logger):
        """Set up a pre-configured logger or create a new one

            :param logging.Logger logger: A pre-configured Python Logger object
        """
        if logger:
            self.logger = logger
        else:
            self.logger = logging.getLogger(__name__)

    @property
    def git(self):
        """Return object to locate a patch in git"""
        if not self._git:
            self._git = GitLocator(distro_info=self.distro_info,
                                   logger=self.logger)
        return self._git

    @git.setter
    def git(self, new_git):
        """Set up object to interact with git

            :param rtls.git.GitLocator new_git: Pre-constructed GitLocator
        """
        if not isinstance(new_git, GitLocator):
            raise TypeError("Git must be a GitLocator object.")
        self._git = new_git

    @property
    def rpm(self):
        """Return object to locate a patch in rpms"""
        if not self._rpm:
            self._rpm = RpmLocator(distro_info=self.distro_info,
                                   logger=self.logger)
        return self._rpm

    @rpm.setter
    def rpm(self, new_rpm):
        """Set up object to interact with rpms

            :param rtls.rpm.RpmLocator new_rpm: Pre-constructed RpmLocator
        """
        if not isinstance(new_rpm, RpmLocator):
            raise TypeError("Rpm must be a RpmLocator object.")
        self._rpm = new_rpm

    @property
    def container(self):
        """Return object to locate a patch in containers"""
        if not self._container:
            # TODO: Only send the required config options rather than
            # the full Locator
            self._container = ContainerLocator(
                locator=self, logger=self.logger
            )
        return self._container

    @container.setter
    def container(self, new_container):
        """Set up object to interact with containers

           :param rtls.container.ContainerLocator new_container:
              Pre-constructed ContainerLocator
        """
        if not isinstance(new_container, ContainerLocator):
            raise TypeError("Container must be a ContainerLocator object.")
        self._container = new_container

    @property
    def compose(self):
        """Return object to locate a patch in composes"""
        if not self._compose:
            # TODO: Only send the required config options rather than
            # the full Locator
            self._compose = ComposeLocator(locator=self, logger=self.logger)
        return self._compose

    @compose.setter
    def compose(self, new_compose):
        """Set up object to interact with composes

            :param rtls.compose.ComposeLocator new_compose: Pre-constructed
               ComposeLocator
        """
        if not isinstance(new_compose, ComposeLocator):
            raise TypeError("Compose must be a ComposeLocator object.")
        self._compose = new_compose
