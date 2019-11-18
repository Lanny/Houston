#!/usr/bin/env python
import os
import subprocess
import distutils

from setuptools import find_packages, setup
from setuptools.command.sdist import sdist
from setuptools.command.install import install
from setuptools.command.egg_info import egg_info

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

class CustomDist(sdist):
    def run(self):
        self.run_command('gulp_build')
        sdist.run(self)

class GulpBuild(distutils.cmd.Command):
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        wd = 'Houston/static-src'

        self.announce('Running `npm install`', level=distutils.log.INFO)
        cmd = subprocess.Popen(['npm', 'install'],
                               cwd=wd,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        out, err = cmd.communicate()

        if cmd.returncode != 0:
            self.announce('Return code was: %d' % cmd.returncode,
                          level=distutils.log.ERROR)
            assert cmd.returncode == 0

        self.announce('Running `gulp generate`', level=distutils.log.INFO)
        cmd = subprocess.Popen(['node_modules/gulp-cli/bin/gulp.js',
                                'generate',
                                '--optimize'],
                                cwd=wd,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        out, err = cmd.communicate()

        if cmd.returncode != 0:
            self.announce('Return code was: %d' % cmd.returncode,
                          level=distutils.log.ERROR)
            assert cmd.returncode == 0

setup(
    name='django-houston',
    version='0.1.0',
    packages=find_packages(exclude=('testsite',)),
    include_package_data=True,
    license='GPL v3.0',
    
    description='Straightforward analytics that don\'t involve shipping your data to "Someone Else"',
    long_description=README,
    url='https://github.com/RyanJenkins/Houston',
    author='Lanny',
    author_email='lan.rogers.book@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    cmdclass={
        'sdist': CustomDist,
        'gulp_build': GulpBuild,
    },
)
