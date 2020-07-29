# -*- coding: utf-8 -*-

"""Parse configuration information."""

from distroinfo import info


def parse_distro_info_path(path):
    """Break distro_info path into repo + file"""
    path = path.strip().rsplit("/", 1)
    info_repo = path[0]
    info_file = path[1]
    remote = False

    if info_repo.startswith("http"):
        remote = True

    return info_file, info_repo, remote


def setup_distro_info(distroinfo_repo):
    """Set up distro_info based on path"""
    info_file, info_repo, remote = parse_distro_info_path(distroinfo_repo)

    if remote:
        di = info.DistroInfo(info_file, remote_git_info=info_repo)
    else:
        di = info.DistroInfo(info_file, local_info=info_repo)

    return di.get_info()
