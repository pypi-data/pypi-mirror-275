from setuptools import setup, find_packages

setup(
    name='whack_a_mole',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pygame',
    ],
    entry_points={
        'console_scripts': [
            'whack-a-mole=whack_a_mole.game:run_game',
        ],
    },
    author='saito_haruto',
    author_email='s2222016@stu.musashino-u.ac.jp',
    description='A simple Whack-a-Mole game using Pygame',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/harutosaisai/whack_a_mole',
    classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
],
    python_requires='>=3.6',
)
