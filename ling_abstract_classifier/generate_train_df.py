import pandas as pd
pd.options.mode.chained_assignment = None

#This loads a function to lemmatize the abstracts
from clean_text import lemmatize


def generate_train_df(lingbuzz_data_file):
    '''
    This function returns a balanced dataframe for training the classifier.

    Returns
    -------
    df : A Pandas DataFrame

    '''

    # Load the data from lingbuzz
    df = pd.read_csv(lingbuzz_data_file)

    # Drop nan entries
    df.dropna(subset=['Title'], inplace=True)
    
    # Giving format to the Date column
    df['Date'] = pd.to_datetime(df['Date'])
    df['Date'] = df['Date'].dt.strftime('%Y-%m')

    # These are the labels of the subdisciplines to consider
    disciplines = ['phonology', 'morphology', 'syntax', 'semantics']

    # Creating a new df with the relevant information
    #to_train = df_main[['Title', 'Abstract', 'Keywords']]

    # Filling the empty abstract spaces with empty strings
    df['Abstract'] = df['Abstract'].fillna('')

    # Creating columns for the labels and giving them values 0 and 1
    for word in disciplines:
        df[word] = df['Keywords'].apply(lambda x: 1 if word in x else 0)

    # Combining the text in titles and abstracts
    df['context'] = df['Title'] + '. ' + df['Abstract']

    ####################################################################
    ####################################################################
    # This part is designed to balance the database. Lingbuzz has many
    # more manuscripts on syntax and semantics than on the other fields,
    # and this leads to a classification problem if all the abstracts
    # are used.
    
    # This is a dictionary with counts of labels for each subdiscipline
    label_count = {dis: df[dis].sum() for dis in disciplines}
    
    # And this the number of labels with the lowest count (it is phonology)
    lowest_label_count = min(label_count.values())

    selected_abstracts = []
    
    for dis in disciplines:
        small_df = df[df[dis] == 1]
        small_df = small_df.sort_values(by='Date', ascending=False)
        small_df = small_df.head(lowest_label_count)
        selected_abstracts.append(small_df)
    
    df = pd.concat(selected_abstracts, ignore_index=False, join='inner')
    
    ####################################################################
    ####################################################################
    
    # Lemmatizing the abstracts
    df['context'] = df['context'].apply(lemmatize)
    
    # Reordering the columns and droping the unnecesary ones
    df = df[['context', 'phonology', 'morphology', 'syntax',
            'semantics']]
    
    df.to_csv('to_train.csv', index=False)
    