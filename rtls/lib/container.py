#! /usr/bin/env python
"""This module acts as an interface for locating patches in containers"""


class ContainerLocator(object):

    def __init__(self, locator, logger):
        """Constructor for ContainerLocator object

            :param rtls.Locator locator: A pre-constructed Locator
            :param logging.Logger logger: A pre-configured Python Logger object
        """
        self.locator = locator
        self.logger = logger
