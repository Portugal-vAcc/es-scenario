from setuptools import setup

setup(
  name='es-scenario-maker',
  version='0.1',
  py_modules=['make'],
  install_requires=['Click'],
  entry_points='''
    [console_scripts]
    make=make:main
  '''
)
