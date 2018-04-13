from setuptools import setup, find_packages

tests_require = [
    'pytest',
    'pytest-cov'
]

setup(name='Super Simple Stock Market',
      version='0.0',
      author='Sten Vael',
      packages=find_packages(),
      setup_requires=['pytest-runner'],
      tests_require=tests_require
      )
