from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 11',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

with open('README.txt', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

with open('CHANGELOG.txt', 'r', encoding='utf-8') as fh:
    long_description += '\n\n' + fh.read()

setup(
    name='MaskaAI',
    version='0.0.2',
    description='MaskaAI from maska.ai',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='',
    author='Maska',
    author_email='maska@maska.ai',
    license='MIT',
    classifiers=classifiers,
    keywords='AI',
    packages=find_packages(),
    install_requires=['requests', 'datetime']
)