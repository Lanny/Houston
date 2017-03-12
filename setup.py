import os
import subprocess
import distutils

from setuptools import find_packages, setup
from setuptools.command.build_py import build_py

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

class CustomBuild(build_py):
    def run(self):
        self.run_command('gulp_build')
        build_py.run(self)
        print 'Done!'

class GulpBuild(distutils.cmd.Command):
    def initialize_options(self):
        pass

    def finalize_options(self):
        assert os.path.exists('Houston/static/Houston/js/tracker.js')

    def run(self):
        wd = 'Houston/static-src'

        self.announce('Running `npm install`', level=distutils.log.INFO)
        cmd = subprocess.Popen(['npm', 'install'], cwd=wd)
        cmd.wait()

        self.announce('Running `gulp generate`', level=distutils.log.INFO)
        cmd = subprocess.Popen(['gulp', 'generate', '--optimize'], cwd=wd)
        cmd.wait()

setup(
    name='django-houston',
    version='0.1a',
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
        'License :: OSI Approved :: GPL v3.0',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    cmdclass={
        'build_py': CustomBuild,
        'gulp_build': GulpBuild
    },
)
