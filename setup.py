from setuptools import setup, find_packages

setup(
  name='es-scenario-maker',
  version='0.1',
  py_modules=['esmake'],
  packages=find_packages(),
  install_requires=['Click'],
  entry_points='''
    [console_scripts]
    esmake=esmake:main
  '''
)
