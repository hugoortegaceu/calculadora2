#setup.py
from setuptools import setup
 
setup(
    name="proyecto_ciberseguridad",
    version="0.1",
    description="Proyecto de Ciberseguridad: Calculadora Básica y Autenticación",
    packages=["modulos_utiles", "tests"],
    install_requires=[
        "pytest",
        "selenium",
        "flake8",
        "pylint",
        "bandit",
        "sonar-scanner",
    ],
)
 
