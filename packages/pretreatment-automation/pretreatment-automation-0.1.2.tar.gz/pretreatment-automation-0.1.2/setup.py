from setuptools import setup, find_packages

setup(
    name='pretreatment-automation',
    version='0.1.2',
    author='Aso Okada',
    author_email='s2222083@stu.musashino-u.ac.jp',
    description='A Python library for automatically preprocessing datasets.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'pandas>=1.0.0',
    ],
)