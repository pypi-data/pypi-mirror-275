from setuptools import setup, find_packages

setup(
    name='keggpathway2genes',
    version='0.0.2',
    author='Pr (France) Dr. rer. nat. Vijay K. ULAGANATHAN',
    author_email=' ',
    description='A package to convert KEGG Pathway IDs to genes',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'keggpathway2genes=kp2genes.kp2genes:main_cli',
        ],
    },
    install_requires=[
        'argparse',
        'requests',
        'bs4',
        'tqdm'
    ],
)

