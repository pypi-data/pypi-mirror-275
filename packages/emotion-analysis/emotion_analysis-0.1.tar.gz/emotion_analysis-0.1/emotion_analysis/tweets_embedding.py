import os

# Get the current directory where this script is located
current_directory = os.path.dirname(os.path.abspath(__file__))

# Change the current working directory to the directory of this script
os.chdir(current_directory)

# Now you can access files and folders relative to this directory


import numpy as np
from transformers import (
    RobertaTokenizer,
    RobertaModel,
)


import torch
from transformers import BertModel, BertTokenizer

# Define the functions for extracting vector representations

print("TWEETS EMBEDDING BERT AND ROBERTA IMPORT START!")


def get_vector_bert(text):
    # Load pre-trained BERT model and tokenizer
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    model = BertModel.from_pretrained("bert-base-uncased")

    # Tokenize input text
    inputs = tokenizer(text, return_tensors="pt", max_length=512, truncation=True)

    # Forward pass through BERT model
    with torch.no_grad():
        outputs = model(**inputs)

    # Extract the embeddings for [CLS] token (the first token)
    cls_embedding = outputs.last_hidden_state[:, 0, :]

    # Convert tensor to list
    cls_embedding_list = cls_embedding.squeeze().tolist()

    return cls_embedding_list


def get_vector_roberta(text):
    try:
        tokenizer = RobertaTokenizer.from_pretrained("twitter-roberta-base-emotion")
        model = RobertaModel.from_pretrained("twitter-roberta-base-emotion")
        inputs = tokenizer(text, return_tensors="pt", max_length=512, truncation=True)
        with torch.no_grad():
            outputs = model(**inputs)
        cls_embedding = outputs.last_hidden_state[:, 0, :]
        cls_embedding_list = cls_embedding.squeeze()
        return cls_embedding_list.numpy()
    except Exception as e:
        print(f"Error in get_vector_roberta: {e}")
        return np.zeros(768)


print("TWEETS EMBEDDING BERT AND ROBERTA IMPORT SUCCESSFULL!")
