from setuptools import setup, find_packages


setup(
  name='PySerLogger',
  version='1.1',
  author='conhosts',
  author_email='conshots.dev@gmail.com',
  description='Module for beautiful log',
  long_description="Usage: sert()",
  long_description_content_type='text/markdown',
  url='https://google.com',
  packages=find_packages(),
  install_requires=['requests>=2.28.2', 'bs4==0.0.2'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='files speedfiles',
  python_requires='>=3.6'
)