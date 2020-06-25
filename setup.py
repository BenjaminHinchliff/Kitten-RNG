import pathlib
from setuptools import setup, find_packages

root = pathlib.Path(__file__).parent

readme = (root / 'README.md').read_text()

setup(
    name='kitten-rng',
    version='1.0.0',
    description='''an rng that generates its numbers based off of a
        kitten livestream''',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/SuniTheFish/Kitten-RNG',
    author='Benjamin Hinchliff',
    author_email='benjamin.hinchliff@gmail.com',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    packages=find_packages(exclude=('KRNG_env',)),
    include_package_data=True,
    install_requires=[
        'opencv-python', 'pafy', 'youtube_dl', 'importlib-resources'
    ],
    entry_points={
        'console_scripts': [
            'realpython=reader.__main__:main',
        ],
    },
)

