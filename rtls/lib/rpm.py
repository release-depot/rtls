#! /usr/bin/env python
"""This module acts as an interface for locating patches in rpms"""


class RpmLocator(object):

    def __init__(self, distro_info, logger):
        """Constructor for RpmLocator object

            :param dict distro_info: A distro info dictionary
            :param logging.Logger logger: A pre-configured Python Logger object
        """
        self.distro_info = distro_info
        self.logger = logger
