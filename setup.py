from glob import glob
from os.path import basename
from os.path import splitext
from setuptools import find_packages
from setuptools import setup


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name="doctlin",
    version="0.1.0",
    license="MIT",
    description="doctlin descriptions.",
    author="Takashi OKADA",
    url="https://github.com/tkokada/doctlin",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    install_requires=_requires_from_file('requirements.txt'),
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"]
)
