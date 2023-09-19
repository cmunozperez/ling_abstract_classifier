# Automatic classification of linguistic abstracts

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
classify_abstract('This is an abstract about syntax and morphology.')
```

## Retraining the Classifier
You can retrain the classifier by providing a new dataset from Lingbuzz. To do this, follow these steps:

1. Obtain a new dataset from Lingbuzz by running the [lingbuzz_scraper](https://github.com/cmunozperez/lingbuzz_scraper) tool.
2. Place the newly generated csv file in the project directory.
3. Run the script with the -newdata flag:

```
python main.py -newdata
```

This will allow you to retrain the classifier using the new dataset.

## Web Application
Additionally, there is a web app implementation of the classifier through Streamlit. You can access the web app by visiting the following URL:

[Linguistics Abstract classifier](https://lingabstractclass.streamlit.app/)



