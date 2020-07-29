#!/usr/bin/env python

"""Tests for `rtls` package."""

from unittest.mock import patch

from rtls.lib.git import GitLocator
from rtls.lib.rpm import RpmLocator
from rtls.lib.compose import ComposeLocator
from rtls.lib.container import ContainerLocator
from rtls.rtls import Locator


def test_locator_init():
    """
    GIVEN Locator initialized with a distro info path
    WHEN the object is created
    THEN the library objects are initialized
    """
    with patch('rtls.config.setup_distro_info'):
        locator = Locator('https://example.com/git/example-full.yml')
        assert type(locator.git) is GitLocator
        assert type(locator.rpm) is RpmLocator
        assert type(locator.compose) is ComposeLocator
        assert type(locator.container) is ContainerLocator
