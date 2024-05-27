# Licence: MIT

from setuptools import setup

DESCRIPTION = 'Convert all files directly under the directory to any music file.'
NAME = 'Image-f-c'
AUTHOR = 'Goki Nagata'
AUTHOR_EMAIL = 's2222068@stu.musashino-u.ac.jp'
URL = 'https://github.com/Ryomo0797/AudioAlchemist.git'
LICENSE = 'MIT'
DOWNLOAD_URL = URL
VERSION = '0.1.6'
PYTHON_REQUIRES = '>=3.6'
INSTALL_REQUIRES = [
    "pillow>=0.25.1"
]
PACKAGES = [
    'src'
]
KEYWORDS = 'PIL, image, file, png, jpeg, bmp'
CLASSIFIERS=[
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6'
]
with open('README.md', 'r', encoding='utf-8') as fp:
    readme = fp.read()
LONG_DESCRIPTION = readme
LONG_DESCRIPTION_CONTENT_TYPE = 'text/markdown'

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    url=URL,
    download_url=URL,
    packages=PACKAGES,
    classifiers=CLASSIFIERS,
    license=LICENSE,
    keywords=KEYWORDS,
    install_requires=INSTALL_REQUIRES
)