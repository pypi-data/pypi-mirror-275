# setup.py

from setuptools import setup, find_packages

setup(
    name='sakurose',  # Nombre del paquete
    version='0.1',  # Versión del paquete
    packages=find_packages(),  # Encuentra todos los paquetes en el directorio
    include_package_data=True,  # Incluye archivos de datos del paquete
    install_requires=[
        'fastapi',
        'Flask',
        'discord.py',
        'py-cord',
        'SQLAlchemy',
        'httpx',
        'uvicorn',
        'pydantic',
        'gino',
        'googletrans',
        'pymongo'
    ],
    entry_points={
        'console_scripts': [
            'sakurose=mypackage.module:greet',
        ],
    },
    author='InsAnya606',
    author_email='insanyadev@gmail.com',
    description='Instala SakuRose en tu sistema para simplificar lo que quieres hacer.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/InsAnya606/SakuRose',  # URL del proyecto
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)