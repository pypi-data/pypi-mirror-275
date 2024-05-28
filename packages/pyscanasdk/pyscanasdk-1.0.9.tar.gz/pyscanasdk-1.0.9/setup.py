from setuptools import setup, find_packages  
  
setup(
    name='pyscanasdk',
    version='1.0.9',
    packages=['pyscanasdk'],
    url='https://github.com/scanasdk/scana-sdk-python',
    license='MIT',
    author='scana',
    author_email='',
    description='123',
    install_requires=[
        # List your dependencies here
        'requests>=2.24.0'
    ],
)


# print(find_packages())