# 📧 Email Spam Filter

## Introduction
The Email Spam Filter is a tool designed to analyze and filter out spam emails using various criteria and machine learning algorithms. This repository provides a simple yet effective implementation of a spam filter in Python.

## How It Works
The tool uses natural language processing (NLP) techniques and machine learning algorithms to classify emails as spam or not spam. It is trained on a dataset of labeled emails and can be used to predict whether new emails are spam.

## Features
- Analyzes email content and metadata.
- Uses machine learning algorithms for spam classification.
- Provides a simple command-line interface for testing and usage.

## Setup Instructions
1. **Clone the repository**:
    ```bash
    git clone https://github.com/coderprasnt/email-spam-filter.git
    cd email-spam-filter
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the spam filter**:
    ```bash
    python spam_filter.py
    ```

## Usage
The tool can be used to classify emails as spam or not spam. It takes a text file containing the email content as input and outputs whether the email is spam.

### Training the Model
To train the spam filter model, run the following command:
```bash
python spam_filter.py --train
```

### Predicting Spam
To predict whether an email is spam, use the following command:
```bash
python spam_filter.py --email_path "path/to/email.txt"
```

### Example
Here's an example of training the model and predicting whether an email is spam:
1. **Train the model**:
    ```bash
    python spam_filter.py --train
    ```

2. **Predict if an email is spam**:
    ```bash
    python spam_filter.py --email_path "data/test/spam/spam1.txt"
    ```

## Conclusion
The Email Spam Filter is a powerful tool for detecting and filtering out spam emails. By leveraging machine learning algorithms, it provides an effective solution for managing email spam.

## Contact
If you have any questions or need further assistance, please contact me through my social media channels.

- **Telegram**: [@Witchshophub](https://t.me/witchshophub) 🐦
