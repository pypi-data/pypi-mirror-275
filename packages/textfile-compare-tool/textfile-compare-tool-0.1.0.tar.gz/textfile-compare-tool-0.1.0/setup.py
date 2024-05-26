from setuptools import setup, find_packages

setup(
    name='textfile-compare-tool',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'compare-textfiles = cli:main',
        ],
    },
    description='A tool to compare and highlight differences between text files.',
    author='MizukiNozawa',
    author_email='s2222090@stu.musashino-u.ac.jp',
    url='https://github.com/MizukiNozawa/textfile-compare-tool.git',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)