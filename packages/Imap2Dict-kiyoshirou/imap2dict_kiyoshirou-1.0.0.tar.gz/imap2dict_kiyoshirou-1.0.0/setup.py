# Licence: MIT

from setuptools import setup

DESCRIPTION = 'Automatically convert .doc and .docx and .xlsx and .pptx to .pdf format.'
NAME = 'Imap2Dict_kiyoshirou'
AUTHOR = 'Kiyoshirou Matsubara'
AUTHOR_EMAIL = 's2222035@stu.musashino-u.ac.jp'
LICENSE = 'MIT'
VERSION = '1.0.0'
PYTHON_REQUIRES = '>=3.6'
INSTALL_REQUIRES = [
    "os",
    "comtypes",
    "docx",
    "xlsxwriter.workbook",
    "pptx",
    "subprocess"
]
PACKAGES = [
    'Imap2Dict_kiyoshirou'
]
KEYWORDS = 'docx ,xlsx ,pptx ,pdf,convert,docx to pdf,xlsx to pdf,pptx to'
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
    packages=PACKAGES,
    classifiers=CLASSIFIERS,
    license=LICENSE,
    keywords=KEYWORDS,
    install_requires=INSTALL_REQUIRES
)