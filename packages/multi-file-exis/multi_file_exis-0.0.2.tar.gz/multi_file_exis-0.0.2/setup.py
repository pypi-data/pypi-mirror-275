from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 11',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='multi_file_exis',
  version='0.0.2',
  description='allows to make a json file in a network folder',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',
  author='Vincent Welter',
  author_email='vincent.welter@outlook.de',
  license='MIT', 
  classifiers=classifiers,
  keywords='json',
  packages=find_packages(),
  install_requires=['json', 'os'] 
)