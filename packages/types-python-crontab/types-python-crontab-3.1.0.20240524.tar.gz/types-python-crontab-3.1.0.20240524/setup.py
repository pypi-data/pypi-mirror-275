from setuptools import setup

name = "types-python-crontab"
description = "Typing stubs for python-crontab"
long_description = '''
## Typing stubs for python-crontab

This is a [PEP 561](https://peps.python.org/pep-0561/)
type stub package for the [`python-crontab`](https://gitlab.com/doctormo/python-crontab) package.
It can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
PyCharm, etc. to check code that uses
`python-crontab`.

This version of `types-python-crontab` aims to provide accurate annotations
for `python-crontab==3.1.*`.
The source for this package can be found at
https://github.com/python/typeshed/tree/main/stubs/python-crontab. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/main/README.md for more details.
This package was generated from typeshed commit `ac6c61ba04c3d3abf476570de04a9afe7447890b` and was tested
with mypy 1.10.0, pyright 1.1.364, and
pytype 2024.4.11.
'''.lstrip()

setup(name=name,
      version="3.1.0.20240524",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/python-crontab.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['crontab-stubs', 'crontabs-stubs', 'cronlog-stubs'],
      package_data={'crontab-stubs': ['__init__.pyi', 'METADATA.toml', 'py.typed'], 'crontabs-stubs': ['__init__.pyi', 'METADATA.toml', 'py.typed'], 'cronlog-stubs': ['__init__.pyi', 'METADATA.toml', 'py.typed']},
      license="Apache-2.0 license",
      python_requires=">=3.8",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
