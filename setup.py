# coding: utf-8
import os
from setuptools import setup, find_packages
try:  # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements


ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__)))

__VERSION__ = 'v0.0.1'

install_requires = []
development_requires = []

setup_requires = parse_requirements(
    os.path.join(ROOT, 'requirements', 'base.txt'), session='hack')
setup_requires = [str(ir.req) for ir in setup_requires]

print(setup_requires)

tests_requires = [
    'pytest==3.0.7',
]

setup_requires = []

setup(
    name="cielo",
    version=__VERSION__,
    author="Stored",
    author_email="guilherme.tavares@maistodos.com.br",
    url="https://github.com/MaisTodos/django-plus",
    package_dir={'': 'src'},
    packages=find_packages('src'),
    description='Django Plus',
    long_description=open(os.path.join(ROOT, 'README.md'), 'r', encoding='utf8').read(),
    install_requires=install_requires,
    setup_requires=setup_requires,
    extras_require={
        'tests': tests_requires,
        'dev': development_requires,
    },
    zip_safe=True,
    include_package_data=True,
)
