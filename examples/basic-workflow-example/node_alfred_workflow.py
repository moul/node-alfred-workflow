# -*- coding: utf-8 -*-

import os
import subprocess


class AlfredError(Exception):
    pass


class NodeAlfredWorkflow(object):
    """ NodeAlfredWorkflow. """

    PATH = "/usr/local/bin:/usr/bin:/bin"
    BINARY_NAMES = ['node', 'nodejs']

    def __init__(self):
        super(NodeAlfredWorkflow, self).__init__()

    @property
    def paths(self):
        paths = set()
        paths.update(set(self.PATH.split(':')))
        paths.update(set(os.environ.get('PATH').split(':')))
        return paths

    @property
    def node_binaries(self):
        counter = 0
        for path in self.paths:
            for binary in self.BINARY_NAMES:
                filepath = os.path.join(path, binary)
                if os.path.exists(filepath):
                    counter += 1
                    yield filepath
        if not counter:
            raise AlfredError('Cannot find the `node` binary on your system')

    @property
    def node_is_installed(self):
        try:
            self.node_path  # Try to access the property
        except:
            return False
        return True

    @property
    def node_path(self):
        for binary in self.node_binaries:
            return binary

    def run_file(self, filepath, args=None):
        try:
            if not args:
                args = []
            argv = [self.node_path, filepath] + list(args)
            argv = map(str, argv)
            return subprocess.call(argv)
        except AlfredError as e:
            print(e)
