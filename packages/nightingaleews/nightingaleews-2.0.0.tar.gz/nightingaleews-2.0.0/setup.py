from setuptools import setup, find_packages

VERSION = '2.0.0' 
DESCRIPTION = 'Early Warning Score Calculator'
LONG_DESCRIPTION = 'Early Warning Score Calculator for Nightingale SmartPro'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="nightingaleews", 
        version=VERSION,
        author="Nuno Antunes",
        author_email="<nuno.f.antunes@inov.pt>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['earlywarningscore']
)

# python setup.py sdist bdist_wheel
# twine upload dist/*