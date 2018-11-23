from setuptools import setup

setup(name='bambooHRappy',
      version='0.1',
      description='Python wrapper for BambooHR api',
      url='https://github.com/infinityworks/Bamboo-api-exporter',
      author='Ashley Walls and James Sheard',
      license='MIT',
      packages=['bambooHRappy'],
      install_requires=['requests'],
      zip_safe=False)