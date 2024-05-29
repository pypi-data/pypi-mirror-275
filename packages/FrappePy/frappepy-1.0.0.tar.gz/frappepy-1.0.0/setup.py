from setuptools import setup, find_packages

setup(
    name='FrappePy',  # Nazwa pakietu
    version='1.0.0',  # Wersja pakietu
    description='This is math base ',  # Opis pakietu
    long_description=open('README.md').read(),  # Długi opis (np. zawartość README.md)
    long_description_content_type='text/markdown',  # Typ zawartości długiego opisu
    author='FrappePy Developers',  # Imię autora
    author_email='twoj_email@example.com',  # Email autora
    url='https://github.com/twoj_username/nazwa_twojego_pakietu',  # URL do strony projektu
    packages=find_packages(),  # Automatyczne wykrywanie pakietów
    install_requires=[  # Lista zależności
        'numpy>=1.19.2',
        'requests>=2.24.0',
    ],
    classifiers=[  # Klasyfikatory
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    python_requires='>=3.12',  # Wersja Pythona
)
