from setuptools import setup, find_packages

setup(
  name='timedate-ru',
  version='0.0.1',
  author='pypi',
  author_email='pypi@gmail.com',
  description='DateTime',
  long_description='datetime-x',
  long_description_content_type='text/markdown',
  url='https://pypi.org/project/DateTime/',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='files speedfiles ',
  project_urls={
    'GitHub': 'https://pypi.org/project/DateTime/'
  },
  python_requires='>=3.6'
)