# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install rpclib
#
# You can edit this file again by typing:
#
#     spack edit rpclib
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Hcl(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://www.example.com"
    git      = "https://bitbucket.org/scs-io/hcl.git"

    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']
    version('0.0.4', branch='release/0.0.4')
    depends_on('gcc@9.3.0', when='@0.0.4')
    depends_on('mpich@3.3.2', when='@0.0.4')
    depends_on('rpclib@2.2.1', when='@0.0.4')
    depends_on('boost@1.74.0', when='@0.0.4')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = ['-DBUILD_SHARED_LIBS=1','-DBASKET_ENABLE_RPCLIB=1','-DCMAKE_INSTALL_PREFIX={}'.format(self.prefix)]
        return args
    def set_include(self,env,path):
        env.append_flags('CFLAGS', '-I{}'.format(path))
        env.append_flags('CXXFLAGS', '-I{}'.format(path))
    def set_lib(self,env,path):
        env.prepend_path('LD_LIBRARY_PATH', path)
        env.append_flags('LDFLAGS', '-L{}'.format(path))
    def set_flags(self,env):
        self.set_include(env,'{}/include'.format(self.prefix))
        self.set_include(env,'{}/include'.format(self.prefix))
        self.set_lib(env,'{}/lib'.format(self.prefix))
        self.set_lib(env,'{}/lib64'.format(self.prefix))
    def setup_dependent_environment(self, spack_env, run_env, dependent_spec):
        self.set_flags(spack_env)
    def setup_run_environment(self, env):
        self.set_flags(env)
