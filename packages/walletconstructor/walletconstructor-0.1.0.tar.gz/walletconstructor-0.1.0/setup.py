from setuptools import setup, find_packages


setup(
    name="walletconstructor",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "web3",
        "cryptography",
        "pathlib",
        "requests"
    ],
    entry_points={
        'console_scripts': [
            'walletconstructor=walletconstructor.wallet.wallet:main',  # Exemple de point d'entrée si vous avez un script exécutable
        ],
    },
    author="kikakop",
    author_email="kikakopjunior@gmail.com",
    description="Module gestion wallet basee sur la blockchain ethereurm",
    long_description= open("README.md").read(),
    long_description_content_type='text/markdown',
    url="https://gitlab.com/kikakopjunior/walletconstructor.git",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',

)