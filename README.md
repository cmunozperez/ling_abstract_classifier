# A classifier of abstracts in linguistics

The **ling_abstract_classifier** script takes an abstract in theoretical linguistics and classifies it into one or more of the core linguistic subdisciplines (phonology, morphology, syntax, semantics).

This project primarily serves as a proof of concept, aiming to test the applicability of the Lingbuzz database in creating tools for linguists.

## Data Source

The classifier's data source is Lingbuzz.net, and it was collected using the [lingbuzz_scraper](https://github.com/cmunozperez/lingbuzz_scraper) tool.

## Usage

First, you need to clone this repository to your local machine.

```
git clone https://github.com/cmunozperez/ling_abstract_classifier.git
```

You run the classifier by executing the main.py file in the project directory.

```
python main.py
```

Alternatively, you can import the `main.py` module and use the function `classify_abstract`. It takes as its only argument the string you want to classify.

```
classify_abstract('Campos (1986) argues that object drop in Spanish exhibits island effects. This claim has remained unchallenged up to date and is largely assumed in the literature. In this squib, I show that this characterization is not empirically correct: given a proper discourse context, null objects can easily appear within a syntactic island in Spanish. This observation constitutes a non-trivial problem for object drop analyses based on movement.')
```
