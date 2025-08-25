from setuptools import setup, find_packages

setup(
    name="calculatorsimulator",           # Nom du package
    version="1.0.0",                 # Numéro de version
    packages=find_packages(),        # Recherche automatique des sous-packages
    description="Package pour calculer et visualiser les émissions CO2",
    long_description=open("README.md").read(),  # Optionnel : contenu de la doc
    long_description_content_type="text/markdown",  # Format de la doc
    author="Achouri Mohamed",                # Auteur  
    author_email= "Mohamed.Achouri@etu.sorbonne-universite.fr",# Email de l'auteur
    url= "https://github.com/Camel-glitch/carbsimulator",      # URL du dépôt Git (optionnel)
    install_requires=[               # Dépendances nécessaires au package
        "matplotlib","pandas","numpy"                
    ],
    classifiers=[                    # Informations complémentaires
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.8.8',         # Version minimale de Python
)
#Test pushing
