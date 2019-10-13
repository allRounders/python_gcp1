from setuptools import setup, find_packages

setup(name="python_gcp1",
        version="0.1",
        packages=['com','com.common','com.util','com.nltk_exp','resources'],
        entry_points={'console_script':['run=python_gcp1.com.spacy_nlp:run']}
        )