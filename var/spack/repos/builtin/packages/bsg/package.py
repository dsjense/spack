# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack import *


class Bsg(CMakePackage):
    """Beta Spectrum Generator: High precision allowed beta spectrum shapes."""

    homepage = "https://bsg.readthedocs.io/en/latest/index.html"
    git      = "https://github.com/leenderthayen/BSG.git"

    maintainers = ['dsjense']# leenderthayen'

    # Master branch
    version('python3', git = "https://github.com/dsjense/BSG.git",
            commit="8d1a2a25ef93ed707f6b39b2c0ac37c7764e2817")
    version('master', git="https://github.com/root-project/root.git",
            branch='master')

    version('04.27.2020', commit='99d4526cd6a0b3fb42ea46170b87b5bf779b1157',
            preferred=True)

    variant('python',   default=True, description='Build with Python GUI support')

    dbpath = join_path('data', 'databases')    
    resource(
        name='ENSDF_099',
        url='https://www.nndc.bnl.gov/ensarchivals/distributions/dist19/ensdf_190101_099.zip',
        sha256='f995129cd4cd50ae2c049f26168dd1f2d503c98749ecb42889440aab355819c2',
        destination=dbpath,
        placement='ENSDF_099',
        expand=True,
        when='+python',
    )
    resource(
        name='ENSDF_199',
        url='https://www.nndc.bnl.gov/ensarchivals/distributions/dist19/ensdf_190101_199.zip',
        sha256='36e1c65f665a75f8387876346de780f7e3d3caa41d67155bdd35fdb993beed72',
        destination=dbpath,
        placement='ENSDF_199',
        expand=True,
        when='+python',
    )
    resource(
        name='ENSDF_299',
        url='https://www.nndc.bnl.gov/ensarchivals/distributions/dist19/ensdf_190101_299.zip',
        sha256='f33239f1d5239183391aba0ba9206163037c842d35900ccf752ab3df682a1deb',
        destination=dbpath,
        placement='ENSDF_299',
        expand=True,
        when='+python',
    )
    resource(
        name='FRDM',
        url='https://ars.els-cdn.com/content/image/1-s2.0-S0092640X1600005X-mmc1.zip',
        sha256='6beb50fadd05cbf0a026d658ce5ee45964eb1fcf66f169fd79686fe94499811b',
        destination=dbpath,
        placement='FRDM',
        expand=True,
        when='+python',
    )
    resource(
        name='ChargeRadii',
        url='https://journals.aps.org/prc/supplemental/10.1103/PhysRevC.94.064315/nuclear_charge_radii.txt',
        sha256='2fdfcd7c39f62557696bdedd90e2859146cf503b7fbe3245ec53a6d0f9d7bdcc',
        destination=dbpath,
        placement='ChargeRadii',
        expand=False,
        when='+python',
    )


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

# Uncomment these lines if you want to download the resource files with CMake
#    def cmake_args(self):
#        args = ['-DBSG_INSTALL_DATA=ON']
#        return args

    def setup_run_environment(self, env):
        env.set('BSGPATH', join_path(self.prefix, 'bin', 'bsg_exec'))
        env.set('BSGEXCHANGEPATH', join_path(self.prefix, 'data', 'ExchangeData.dat'))
        dbdir = join_path(self.prefix, 'data', 'databases')
        env.set('ENSDFDIR', join_path(dbdir, 'ENSDF'))
        env.set('FRDMPATH', join_path(dbdir, 'FRDM', 'supplement-tabmas2012.dat'))
        env.set('CHARGERADIIPATH', join_path(dbdir, 'ChargeRadii', 'nuclear_charge_radii.txt'))

    @run_before('build')
    def merge_ensdf_files(self):
        print(self.stage.source_path)
        if '+python' in self.spec:
            prefix = self.stage.source_path
            print('prefix=', prefix)
            with working_dir(join_path(prefix, 'data', 'databases')):
                mkdirp("ENSDF")
                for ensdf_folder in ['ENSDF_' + num for num in ('099', '199', '299')]:
                    for ensdf_file in os.listdir(ensdf_folder):
                        oldpath = join_path(ensdf_folder, ensdf_file)
                        newpath = join_path('ENSDF', ensdf_file)
                        os.rename(oldpath, newpath)
                    os.rmdir(ensdf_folder)
