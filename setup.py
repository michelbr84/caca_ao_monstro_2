from setuptools import setup, find_packages

setup(
    name="caca_ao_monstro_2",
    version="2.0.0",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        'pygame',  # Lista a dependência principal do jogo
    ],
    entry_points={
        'console_scripts': [
            'caca_ao_monstro_2=game:main',  # Ajuste conforme o ponto de entrada do jogo
        ],
    },
    author="MichelBr",
    description="Caça ao Monstro 2: Um jogo de aventura com gráficos e sons.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/michelbr84/caca_ao_monstro_2",  # Coloque a URL correta
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
