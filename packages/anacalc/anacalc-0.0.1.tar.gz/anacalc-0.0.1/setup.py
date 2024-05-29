from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='anacalc',
    version='0.0.1',
    description='A very basic calculator',
    long_description=open('README.txt').read(),
    url='',  # Replace with a valid URL or remove this line if not available
    author='A K Ghosh',
    author_email='anantafcs@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='simple_anacalc',
    packages=find_packages(),
    install_requires=[]  # Update with actual dependencies or leave as an empty list
)

