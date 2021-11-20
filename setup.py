from setuptools import setup

setup(name = "pyre",
    version = "0.0.1",
    description = "A low-dependency library for epidemiologic analysis.",
    url = "https://github.com/chevalier-deon/PyRE.git",
    author = "chevalier-deon/guro_io",
    author_email = "do.not.email.rightnow@gmail.com",
    license="MIT",
    packages=["pyre"],
    install_requires=[
        "numpy",
        "pandas"
    ],
    zip_safe=False)
