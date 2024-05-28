from setuptools import setup, find_packages

setup(
    name='facify',
    version='0.1',
    author="Digvijay Patil",
    author_email="patildigvijay7878@gmail.com",
    description="A simple and efficient tool for extracting faces from images using face detection Haar cascade.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'facify': ['facify/data/haarcascade_frontalface_default.xml'],
    },
    install_requires=[
        'opencv-python',
    ],
    
)