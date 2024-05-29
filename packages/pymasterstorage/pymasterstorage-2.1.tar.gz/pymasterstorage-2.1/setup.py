from setuptools import setup, find_packages

VERSION = '2.1'
DESCRIPTION = 'Master Storage checker'


setup(
    name="pymasterstorage",
    version=VERSION,
    author="Fouad (Fouad Jabri)",
    author_email="<fouad.jabri@proton.me>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests', 'pywin32'],
    keywords=['python', 'storage'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)