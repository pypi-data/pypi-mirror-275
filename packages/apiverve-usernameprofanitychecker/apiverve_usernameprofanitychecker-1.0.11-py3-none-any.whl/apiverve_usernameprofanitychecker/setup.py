from setuptools import setup, find_packages

setup(
    name='apiverve_usernameprofanitychecker',
    version='1.0.11',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
        'setuptools'
    ],
    description='Username Profanity Checker is a simple tool for checking if a username is inappropriate or profane. It returns if the username is inappropriate or profane.',
    author='APIVerve',
    author_email='hello@apiverve.com',
    url='https://apiverve.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
