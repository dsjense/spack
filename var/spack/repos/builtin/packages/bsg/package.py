# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Bsg(CMakePackage):
    """Beta Spectrum Generator: High precision allowed beta spectrum shapes."""

    homepage = "https://bsg.readthedocs.io/en/latest/index.html"
    git      = "https://github.com/leenderthayen/BSG.git"

    maintainers = ['dsjense']# leenderthayen'

    # Master branch
    version('python3', git = "https://github.com/dsjense/BSG.git",
            commit="e748943e2b82edeb7508077f7a19acdae48af182")
    version('master', git="https://github.com/root-project/root.git",
            branch='master')

    version('04.27.2020', commit='99d4526cd6a0b3fb42ea46170b87b5bf779b1157',
            preferred=True)

    variant('python',   default=True, description='Build with Python GUI support')

    depends_on('gsl')
    depends_on('boost +program_options')
    depends_on('spdlog')
    depends_on('root')
    depends_on('python@3.5:', type=('build', 'run'), when='+python')
    depends_on('py-shell', type=('build', 'run'), when='+python')
    # py-pyside2 and py-numpy are py-pyqtgraph dependencies
#    depends_on('py-pyside2', type=('build', 'run'), when='+python')
#    depends_on('py-numpy', type=('build', 'run'), when='+python')
    depends_on('py-pyqtgraph@0.11.0:', type=('build', 'run'), when='+python')

