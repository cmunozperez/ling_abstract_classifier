import numpy as np
import pandas as pd
from clean_text import lemmatize
from generate_train_df import generate_train_df 
from training import train_models
import joblib
import argparse

####################################
####################################

# The following gives the option of generating new training data in case you want to use more current abstracts from Lingbuzz
parser = argparse.ArgumentParser(description='An abstract classifier for linguistics: given an abstract, it classifies it into one of the main areas of theoretical linguistics (phonology, morphology, syntax or semantics), or into a combination of these.')
parser.add_argument('-newdata', action='store_true', help='Allows to change the training data set by providing new Lingbuzz data.')
args = parser.parse_args()

new_train_df = 'no'

if args.newdata:
    try:
        print('')
        new_train_df = input('A proper training dataset is already included. However, you can generate a new one from data scrapped from Lingbuzz in csv format. If you wish to generate a new training file, enter "y". If you just want to ignore this and continue, enter whatever else. ')
        if new_train_df == 'y':
            print('')
            file_name = input('Introduce the name of the file to generate training data (e.g., lingbuzz_002_002022.csv). ')
            generate_train_df(file_name)
            new_train_df = 'ready'
    except:
        print('That is not a valid Lingbuzz database.')

#####################################

# This loads the training data
df = pd.read_csv('to_train.csv')


# This gives the option of training the model with new training data.
# It just activates if a new training dataset was generated.
if new_train_df.lower() == 'ready':
    print('')
    retrain = input('Do you wish to train the models with the newly provided dataset? If yes, enter "y". If you just want to ignore this and continue, enter whatever else. ')
    if retrain.lower() == 'y':
        try:
            train_models(df)
        except:
            print('An unexpected error occurred.')


#The following loads the models and the vectorization of the abstracts
classifier_nb = joblib.load('classifier_nb.pkl')
classifier_rf = joblib.load('classifier_rf.pkl')
c_vect = joblib.load('c_vect.pkl')


#################################################
# This is the part that loads a new abstract and classifies it.

print('')
enter_abstract = input('Copy your abstract here: ')

#This lemmatizes the abstract
enter_abstract = lemmatize(enter_abstract)

# This vectorizes the provided abstract
abstract_vect = c_vect.transform([enter_abstract])

#This classifies the abstract using the naive Bayes model
pred_nb = classifier_nb.predict(abstract_vect).toarray()

# This classifies the abstract using random forests
pred_rf = classifier_rf.predict(abstract_vect).toarray()

# This combines the predictions of both models
combined_pred = np.logical_and(pred_nb,pred_rf)

cats = ['phonology', 'morphology', 'syntax', 'semantics']
output = []

for num in range(4):
    if combined_pred[0, num] == 1:
        output.append(cats[num])
if len(output) == 0:
    print('')
    print('The linguistic subdiscipline of this abstract is unknown.')
else:
    print('')
    print('This is an abstract on the following area(s) of linguistics: ' + ', '.join(output))