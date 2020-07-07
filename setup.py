from setuptools import setup

setup(
    name="aws-ec2-snapshot",
    version="0.1",
    author="Ankur Patel",
    author_email="techgenius@ankurpatel18.com",
    description="This tool manage aws EC2 snapshots",
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/ankurpatel18/aws-ec2-snapshot/",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    '''
)