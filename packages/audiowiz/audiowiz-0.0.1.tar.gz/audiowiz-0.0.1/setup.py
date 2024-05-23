from setuptools import setup, find_packages

VERSION = '0.0.01'
DESCRIPTION = 'Audio and voice package'
LONG_DESCRIPTION = 'A package that uses famous audio and voice packages to make it easier to code'

# Setting up
setup(
    name="audiowiz",
    version=VERSION,
    author="P.Ghaywat)",
    author_email="<Pratham.Ghaywat@outlook.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['opencv-python', 'pyautogui', 'pyaudio'],
    keywords=['python', 'audio', 'voice', 'recording', 'voice command', 'text-to-speech'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)