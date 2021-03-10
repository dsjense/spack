# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPyqtgraph(PythonPackage):
    """A pure-python graphics and GUI library built on PyQt4 / PySide and numpy."""

    homepage = "http://www.pyqtgraph.org/"
    url      = "https://pypi.io/packages/source/P/PyQtGraph/pyqtgraph-0.11.1.tar.gz"
    git      = "https://github.com/pyqtgraph/pyqtgraph"

    maintainers = ['danielsjensen1']

    version('0.11.1', sha256='7d1417f36b5b92d1365671633a91711513e5afbcc82f32475d0690317607714e')
    version('0.11.0', sha256='082cdec1e559644e083cd8c5752fc06a18582fb2bebb83cdf6eb8ad33c735535')

    depends_on('python@3.5:', type=('build', 'run'), when='@0.11:')
    depends_on('py-pyside2@5.13:5.13.999', when='^python@3.7:3.7.999')
    depends_on('py-pyside2@5.14:', when='^python@3.8:')
    depends_on('py-numpy')

    # TODO: add optional support for scipy, pyopengl, and hdf5
