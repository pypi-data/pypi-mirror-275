#!/usr/bin/env python3
'''
Functions for dynamically importing modules.
'''

import importlib.util
import logging
import pathlib
import pkgutil
import sys
from collections import deque


LOGGER = logging.getLogger(__name__)


def import_modules(paths, path_log_msg=None):
    '''
    Import modules by paths.

    Args:
        paths:
            An iterable of file and directory paths. File paths will import
            single modules while directory paths will recursively import all
            modules contained in the directory.

        path_log_msg:
            An optional logging format string for logging messages about the
            given paths. If given, it should contain a single "%s" placeholder
            for the path argument.

    Returns:
        The set of loaded module names.
    '''
    # Dicts from version 3.7 preserve order.
    paths = list(dict.fromkeys(pathlib.Path(path).resolve() for path in paths))
    # Subpaths of other paths will be detected by the parent path so omit them.
    paths = [
        path for path in paths if not any(
            path.is_relative_to(p) for p in paths if path != p
        )
    ]
    if not paths:
        LOGGER.warning('No paths passed to import_modules().')

    if path_log_msg:
        for path in sorted(paths):
            LOGGER.debug(path_log_msg, path)

    file_paths = []
    dir_paths = []
    all_dir_paths = []
    for path in paths:
        if path.is_dir():
            dir_paths.append(path)
            all_dir_paths.append(path)
        else:
            file_paths.append(path)
            all_dir_paths.append(path.parent)

    loaded = set()
    for loader, name, _is_pkg in pkgutil.walk_packages(path=all_dir_paths):
        path = pathlib.Path(loader.path) / f'{name}.py'
        if path in file_paths or any(path.is_relative_to(p) for p in dir_paths):
            LOGGER.debug('Loading module %s from %s', name, path)
            spec = loader.find_spec(name)
            mod = importlib.util.module_from_spec(spec)
            sys.modules[name] = mod
            spec.loader.exec_module(mod)
            loaded.add(name)

    return loaded
