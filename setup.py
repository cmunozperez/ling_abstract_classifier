from setuptools import setup, find_packages

setup(
    name='ling_abstract_classifier',
    version='0.1',
    description='An abstract classifier for linguistics: given an abstract, it classifies it into one of the main areas of theoretical linguistics (phonology, morphology, syntax or semantics), or into a combination of these',
    author='Carlos Muñoz Pérez',
    author_email='cmunozperez@filo.uba.ar',
    packages=find_packages(),
    install_requires=[
        'joblib==1.2.0',
        'nltk==3.8.1',
        'numpy==1.23.1',
        'pandas==1.4.4',
        'scikit-learn==1.2.1',
        'scikit-multilearn==0.2.0',
    ],
)