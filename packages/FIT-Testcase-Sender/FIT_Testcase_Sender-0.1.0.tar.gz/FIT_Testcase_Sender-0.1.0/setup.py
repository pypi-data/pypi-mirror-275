from setuptools import setup, find_packages

setup(
    name='FIT_Testcase_Sender',
    version='0.1.0',
    packages=find_packages(),
    description='A utility for sending scenarios via TCP/IP and checking their completion',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='suresofttech',
    author_email='sdhan@suresofttch.com',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)