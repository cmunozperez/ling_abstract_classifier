from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import hamming_loss
from sklearn.naive_bayes import MultinomialNB
from skmultilearn.problem_transform import BinaryRelevance
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_models(df):
    
    # This instantiates the TF-IDF vectorizer
    vectorizer = TfidfVectorizer(
        max_features=None,
        stop_words='english',
        lowercase=True
    )
    
    #This fits and transform the abstracts
    X_features = vectorizer.fit_transform(df['context'])
    
    # This defines the labels
    y = df[['phonology', 'morphology', 'syntax', 'semantics']]
    
    # This splits the data for training and testing (the function prints the Hamming Loss values for the models)
    X_train, X_test, y_train, y_test = train_test_split(X_features, y, test_size = 0.2, random_state=42)
    
    ###################################################
    ###################################################
    # The classifier is actually an ensemble of a naive Bayes classifier and a random forest classifier.
    # Both are defined here.
    
    # The following three lines (i) instantiate the naive Bayes classifier, (ii) train it and (iii) make test predictions
    classifier_nb = BinaryRelevance(MultinomialNB())
    classifier_nb.fit(X_train, y_train)
    pred_nb = classifier_nb.predict(X_test)
    
    #This saves the naive Bayes classifier.
    file_nb = 'classifier_nb.pkl'
    joblib.dump(classifier_nb, file_nb)
    
    ###################################
    
    #This is the classifier using randomforest. As before, it is instantiated, trained and tested.
    classifier_rf = BinaryRelevance(RandomForestClassifier(random_state=42))
    classifier_rf.fit(X_train, y_train)
    pred_rf = classifier_rf.predict(X_test)
    
    #This saves the random forest classifier.
    file_rf = 'classifier_rf.pkl'
    joblib.dump(classifier_rf, file_rf)
    
    #####################################################
    #####################################################
    
    #This creates and saves a count vectorization of the abstracts
    c_vect = CountVectorizer(stop_words='english', lowercase=True)
    c_vect.fit_transform(df['context'])
    joblib.dump(c_vect, 'c_vect.pkl')
    
    #This calculates the Hamming Loss for each model based on the tests.
    hamming_nb = hamming_loss(y_test, pred_nb)
    hamming_rf = hamming_loss(y_test, pred_rf)
    
    print('')
    print(f'Models saved as {file_nb} and {file_rf}.')
    print('')
    print(f'The Hamming Loss value for the NB model ({file_nb}) is {hamming_nb}.')
    print(f'The Hamming Loss value for the RF model ({file_rf}) is {hamming_rf}.')