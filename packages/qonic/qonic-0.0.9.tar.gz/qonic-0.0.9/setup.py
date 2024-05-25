from setuptools import setup, find_packages

setup(
    name = 'qonic',
    packages = ['qonic', 'qonic.ConstraintSatisfaction', 'qonic.QProgram'],
    version = '0.0.9',
    description = 'The Qonic project is an open source, expandable framework for solving problems using hybrid quantum computing solutions.',
    author = 'cogrpar',
    author_email = 'owen.r.welsh@hotmail.com',
    url = 'https://github.com/Qonic-Team/qonic.git',
    download_url = 'https://github.com/Qonic-Team/qonic/archive/refs/heads/main.zip',
    license='Apache License 2.0',
    keywords = ['qonic', 'quantum computing'],
    setup_requires=['wheel'],
    install_requires=['numpy>=1.22.2', 'sympy>=1.12', 'PyYAML>=5.4.1', 'tequila-basic>=1.8.1', 'qiskit>=0.21.2', 'forest-benchmarking>=0.8.0', 'dimod>=0.11.5','dwavebinarycsp>=0.2.0', 'pillow>=10.3.0', 'fonttools>=4.43.0', 'setuptools>=65.5.1']
)
