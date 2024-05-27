from setuptools import setup, find_packages

VERSION = '0.0.13'
DESCRIPTION = 'StorageAPI for games'

# Setting up
setup(
    name="GameStorageAPI",
    version=VERSION,
    author="Fouad (Fouad Jabri)",
    author_email="<fouad.jabri@proton.me>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests', 'pywin32'],
    keywords=['python', 'storage', 'game', 'game API'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)