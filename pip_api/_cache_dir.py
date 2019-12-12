from pip_api._vendor.packaging.version import Version

import pip_api


def cache_dir():
    """
    Return the user cache directory for pip.
    """
    if pip_api.PIP_VERSION < Version("10.0.0"):
        from pip.locations import USER_CACHE_DIR
    else:
        from pip._internal.locations import USER_CACHE_DIR

    return USER_CACHE_DIR
