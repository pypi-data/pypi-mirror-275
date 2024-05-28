from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'A python image to ASCII CLI tool'
LONG_DESCRIPTION = 'A python image to ASCII CLI tool, using the PIL and numpy libraries'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="asciiscape", 
        version=VERSION,
        author="Lucca Chiguti",
        author_email="luktha12345@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=["Pillow", "numpy"], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'ascii'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)