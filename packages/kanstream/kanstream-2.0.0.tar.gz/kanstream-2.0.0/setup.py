from setuptools import setup, find_packages
from pathlib import Path


PARENT = Path(__file__).resolve().parent

version_file = PARENT / 'kanstream/version.py'
requirements_file = PARENT / 'requirements.txt'


def get_version():
    with open(version_file, 'r') as f:
        exec(compile(f.read(), version_file, 'exec'))

    return locals()['__version__']


def parse_requirements():
    with open(requirements_file, 'r') as f:
        requires = list(map(lambda x: x.strip(), f.readlines()))

    return requires


setup(
    name='kanstream',
    description='pull and push stream',
    version=get_version(),
    author="flinzhao",
    packages=find_packages(),
    install_requires=parse_requirements(),
    python_requires=">=3.10",
)
