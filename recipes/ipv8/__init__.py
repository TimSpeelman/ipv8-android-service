from __future__ import absolute_import

from os import getenv
from os.path import exists, join

from pythonforandroid.recipe import PythonRecipe, current_directory
from sh import cp, mkdir


class LocalIPV8Recipe(PythonRecipe):
    """
    Python-for-Android IPV8 recipe
    """

    url = 'git+https://github.com/Tribler/py-ipv8.git'

    # A list of any other recipe names
    # that must be built before this
    # one
    # https://github.com/kivy/python-for-android/tree/master/pythonforandroid/recipes
    # [IPv8]: In https://github.com/Tribler/py-ipv8/blob/master/requirements.txt
    # [sv]: In https://github.com/Tribler/ipv8-android-service/blob/jenkins_wild/recipes/ipv8/__init__.py
    # [?]: Possibly unnecessary as not in sv, whilst in IPv8
    depends = [
                'aiohttp', # [IPv8][?] unknown
                'aiohttp_apispec', # [IPv8][?] unknown
                'asynctest', # [IPv8][?] unknown
                'cryptography', # [IPv8][sv] https://github.com/kivy/python-for-android/tree/master/pythonforandroid/recipes/cryptography
                'libnacl', # [IPv8][sv] unknown
                'libsodium', # [sv] https://github.com/kivy/python-for-android/tree/master/pythonforandroid/recipes/libsodium
                'netifaces', # [IPv8][sv] https://github.com/kivy/python-for-android/tree/master/pythonforandroid/recipes/netifaces
                'pyasn1', # [IPv8][sv] unknown
                'pyopenssl', # [IPv8] https://github.com/kivy/python-for-android/tree/master/pythonforandroid/recipes/pyopenssl
                'python3', # [sv] https://github.com/kivy/python-for-android/tree/master/pythonforandroid/recipes/python3
                'setuptools', # [sv] https://github.com/kivy/python-for-android/tree/master/pythonforandroid/recipes/setuptools
                'lib2to3',  # [sv][local] unknown
                'sqlite3', # [sv]
                'decorator' # [sv]
               ]

    patches = []

    python_depends = ['hyperlink'] # [sv]

    site_packages_name = 'ipv8'

    call_hostpython_via_targetpython = False

    def postbuild_arch(self, arch):
        super(LocalIPV8Recipe, self).postbuild_arch(arch)

        # Install twistd plugins
        cp('-rf', join(self.get_build_dir(arch.arch), 'twisted', 'plugins'),
            join(self.ctx.get_python_install_dir(), 'twisted'))

        # Copy ipv8_service.py
        cp('-rf', join(self.get_build_dir(arch.arch), 'ipv8_service.py'),
            self.ctx.get_python_install_dir())


recipe = LocalIPV8Recipe()
