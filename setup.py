from setuptools import setup, find_packages

setup(name='spiral_matrix',
      version='1.0',
      url='https://github.com/jetsnake/spiral_matrix',
      license='MIT',
      author='jetsnake',
      author_email='g.kulchitskij@gmail.com',
      description='Spiral traversing in square matrix',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False)
