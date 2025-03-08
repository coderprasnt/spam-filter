import argparse
import os
import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

def load_data():
    # Load training data
    train_spam = []
    train_not_spam = []
    for filename in os.listdir('data/train/spam'):
        with open(os.path.join('data/train/spam', filename), 'r') as file:
            train_spam.append(file.read())
    for filename in os.listdir('data/train/not_spam'):
        with open(os.path.join('data/train/not_spam', filename), 'r') as file:
            train_not_spam.append(file.read())
    train_data = train_spam + train_not_spam
    train_labels = [1] * len(train_spam) + [0] * len(train_not_spam)
    
    # Load test data
    test_spam = []
    test_not_spam = []
    for filename in os.listdir('data/test/spam'):
        with open(os.path.join('data/test/spam', filename), 'r') as file:
            test_spam.append(file.read())
    for filename in os.listdir('data/test/not_spam'):
        with open(os.path.join('data/test/not_spam', filename), 'r') as file:
            test_not_spam.append(file.read())
    test_data = test_spam + test_not_spam
    test_labels = [1] * len(test_spam) + [0] * len(test_not_spam)

    return (train_data, train_labels), (test_data, test_labels)

def train_model():
    (train_data, train_labels), _ = load_data()
    model = make_pipeline(TfidfVectorizer(), MultinomialNB())
    model.fit(train_data, train_labels)
    joblib.dump(model, 'spam_filter_model.pkl')
    print("Model trained and saved as spam_filter_model.pkl")

def predict(email_path):
    if not os.path.exists('spam_filter_model.pkl'):
        print("Model not found. Please train the model first.")
        return

    model = joblib.load('spam_filter_model.pkl')
    with open(email_path, 'r') as file:
        email_content = file.read()
    
    prediction = model.predict([email_content])
    if prediction[0] == 1:
        print("The email is spam.")
    else:
        print("The email is not spam.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Email Spam Filter")
    parser.add_argument('--train', action='store_true', help="Train the spam filter model")
    parser.add_argument('--email_path', type=str, help="Path to the email text file")
    args = parser.parse_args()

    if args.train:
        train_model()
    elif args.email_path:
        predict(args.email_path)
    else:
        parser.print_help()
