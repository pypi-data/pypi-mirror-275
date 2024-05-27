from setuptools import setup

setup(
    name='scocli',
    version='1.3.1',
    author= 'Vasapg',
    description= 'CLI to facilitate the creation and management of SCORM packages',
    url='https://github.com/Vasapg/SCO/tree/main',
    scripts=[
        'sco/removeResource.py',
        'sco/addResource.py',
        'sco/build.py',
        'sco/seeManifest.py',
        'sco/checkManifest.py',
        'sco/organizeManifest.py',
        'sco/bundle.py'
        ],
)
