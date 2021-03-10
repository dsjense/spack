# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyShell(PythonPackage):
    """A better way to run shell commands in Python."""

    homepage = "https://www.example.co://shell.readthedocs.io/en/latest/"
    url      = "https://pypi.io/packages/source/S/Shell/shell-1.0.1.tar.gz"
    git      = "https://github.com/toastdriven/shell"

    maintainers = ['danielsjensen1']

    version('1.0.1', sha256='6fbaa88f85de228ddecef33cb1e9037f4959f6f76942b01769e4139a038f6513')

