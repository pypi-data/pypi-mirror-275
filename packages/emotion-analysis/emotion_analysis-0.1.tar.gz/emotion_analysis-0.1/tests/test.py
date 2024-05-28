import sys
import os

# Get the current directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory (root directory of the project)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

# Add the parent directory to sys.path
sys.path.append(parent_dir)

from emotion_analysis.data_preprocessing import *
from emotion_analysis.dataset_upload import *
from emotion_analysis.tweets_embedding import *
from emotion_analysis.frnn import *
from emotion_analysis.bert_pcc_score_emotions import *
from emotion_analysis.roberta_pcc_score_emotions import *


generate_wordclouds(anger_train, anger_dev, anger_data, anger_test, "Anger")
plot_statistics(anger_train, anger_dev, anger_data, anger_test, "Anger")
plot_additional_statistics(anger_train, anger_dev, anger_test, "Anger")
plot_top_n_words(anger_train, n=20, title="Top 20 Frequent Words in Anger Train Data")
plot_ngrams_frequency(
    anger_train, n=2, top_n=10, title="Bigram Frequency in Anger Train Data"
)
plot_ngrams_frequency(
    anger_train, n=3, top_n=10, title="Trigram Frequency in Anger Train Data"
)

generate_wordclouds(joy_train, joy_dev, joy_data, joy_test, "Joy")
plot_statistics(joy_train, joy_dev, joy_data, joy_test, "Joy")
plot_additional_statistics(joy_train, joy_dev, joy_test, "Joy")
plot_top_n_words(joy_train, n=20, title="Top 20 Frequent Words in Joy Train Data")
plot_ngrams_frequency(
    joy_train, n=2, top_n=10, title="Bigram Frequency in Joy Train Data"
)
plot_ngrams_frequency(
    joy_train, n=3, top_n=10, title="Trigram Frequency in Joy Train Data"
)

generate_wordclouds(sad_train, sad_dev, sad_data, sad_test, "Sadness")
plot_statistics(sad_train, sad_dev, sad_data, sad_test, "Sadness")
plot_additional_statistics(sad_train, sad_dev, sad_test, "Sadness")
plot_top_n_words(sad_train, n=20, title="Top 20 Frequent Words in Sadness Train Data")
plot_ngrams_frequency(
    sad_train, n=2, top_n=10, title="Bigram Frequency in Sadness Train Data"
)
plot_ngrams_frequency(
    sad_train, n=3, top_n=10, title="Trigram Frequency in Sadness Train Data"
)

generate_wordclouds(fear_train, fear_dev, fear_data, fear_test, "Fear")
plot_statistics(fear_train, fear_dev, fear_data, fear_test, "Fear")
plot_additional_statistics(fear_train, fear_dev, fear_test, "Fear")
plot_top_n_words(fear_train, n=20, title="Top 20 Frequent Words in Fear Train Data")
plot_ngrams_frequency(
    fear_train, n=2, top_n=10, title="Bigram Frequency in Fear Train Data"
)
plot_ngrams_frequency(
    fear_train, n=3, top_n=10, title="Trigram Frequency in Fear Train Data"
)


plot_dataset_statistics([anger_data, joy_data, sad_data, fear_data])

anger_pcc_scores = cross_validation_ensemble_owa(
    anger_data.head(10),
    vector_names=["Vector_roberta_cl", "Vector_roberta", "Vector_roberta_cl_ws"],
    NNeighbours=[5, 5],
    lower=[1, 1],
    upper=[1, 1],
    alpha=0.5,
    cv=5,
)
print("anger_PCC Scores:", np.mean(anger_pcc_scores))

joy_pcc_scores = cross_validation_ensemble_owa(
    joy_data.head(10),
    vector_names=["Vector_roberta_cl", "Vector_roberta", "Vector_roberta_cl_ws"],
    NNeighbours=[5, 5],
    lower=[1, 1],
    upper=[1, 1],
    alpha=0.5,
    cv=5,
)
print("joy_PCC Scores:", np.mean(joy_pcc_scores))

fear_pcc_scores = cross_validation_ensemble_owa(
    fear_data.head(10),
    vector_names=["Vector_roberta_cl", "Vector_roberta", "Vector_roberta_cl_ws"],
    NNeighbours=[5, 5],
    lower=[1, 1],
    upper=[1, 1],
    alpha=0.5,
    cv=5,
)
print("fear_PCC Scores:", np.mean(fear_pcc_scores))

sad_pcc_scores = cross_validation_ensemble_owa(
    sad_data.head(10),
    vector_names=["Vector_roberta_cl", "Vector_roberta", "Vector_roberta_cl_ws"],
    NNeighbours=[5, 5],
    lower=[1, 1],
    upper=[1, 1],
    alpha=0.5,
    cv=5,
)
print("sad_PCC Scores:", np.mean(sad_pcc_scores))


anger_pcc_scores = np.mean(anger_pcc_scores)
joy_pcc_scores = np.mean(joy_pcc_scores)
fear_pcc_scores = np.mean(fear_pcc_scores)
sad_pcc_scores = np.mean(sad_pcc_scores)
avg_roberta_emotions_pcc = (
    anger_pcc_scores + joy_pcc_scores + fear_pcc_scores + sad_pcc_scores
) / 4
print("Final PCC Score roberta :", avg_roberta_emotions_pcc)


import os
import matplotlib.pyplot as plt

# Emotion labels
emotion_labels = ["Anger", "Joy", "Fear", "Sadness"]

# Vector types
vector_types = ["Vector_roberta_cl", "Vector_roberta", "Vector_roberta_cl_ws", "bb"]

# Mean PCC scores for each vector type
mean_pcc_scores = [
    np.mean(anger_pcc_scores),
    np.mean(joy_pcc_scores),
    np.mean(fear_pcc_scores),
    np.mean(sad_pcc_scores),
]

plt.figure(figsize=(10, 6))

bars = plt.bar(vector_types, mean_pcc_scores, color="skyblue")

plt.xlabel("Vector Type")
plt.ylabel("Mean PCC Score")
plt.title("Mean PCC Scores for Different Vector Types")
plt.xticks(rotation=45)
plt.grid(axis="y")

# Set the emotion labels as tick labels on the x-axis
plt.xticks(ticks=vector_types, labels=emotion_labels)

# Add value labels on top of each bar
for bar, score in zip(bars, mean_pcc_scores):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.01,
        round(score, 4),
        ha="center",
        va="bottom",
        fontweight="bold",
    )

# Create the directory if it doesn't exist
plots_dir = "plots/roberta_pcc_score"
os.makedirs(plots_dir, exist_ok=True)

# Save the figure
plt.savefig(os.path.join(plots_dir, "roberta_pcc_scores.png"))

print("roberta Base Vector Done!")


anger_pcc_scores = cross_validation_ensemble_owa(
    anger_data.head(10),
    vector_names=["Vector_bert_cl", "Vector_bert", "Vector_bert_cl_ws"],
    NNeighbours=[5, 5],
    lower=[1, 1],
    upper=[1, 1],
    alpha=0.5,
    cv=5,
)
print("anger_PCC Scores:", np.mean(anger_pcc_scores))

joy_pcc_scores = cross_validation_ensemble_owa(
    joy_data.head(10),
    vector_names=["Vector_bert_cl", "Vector_bert", "Vector_bert_cl_ws"],
    NNeighbours=[5, 5],
    lower=[1, 1],
    upper=[1, 1],
    alpha=0.5,
    cv=5,
)
print("joy_PCC Scores:", np.mean(joy_pcc_scores))

fear_pcc_scores = cross_validation_ensemble_owa(
    fear_data.head(10),
    vector_names=["Vector_bert_cl", "Vector_bert", "Vector_bert_cl_ws"],
    NNeighbours=[5, 5],
    lower=[1, 1],
    upper=[1, 1],
    alpha=0.5,
    cv=5,
)
print("fear_PCC Scores:", np.mean(fear_pcc_scores))

sad_pcc_scores = cross_validation_ensemble_owa(
    sad_data.head(10),
    vector_names=["Vector_bert_cl", "Vector_bert", "Vector_bert_cl_ws"],
    NNeighbours=[5, 5],
    lower=[1, 1],
    upper=[1, 1],
    alpha=0.5,
    cv=5,
)
print("sad_PCC Scores:", np.mean(sad_pcc_scores))


anger_pcc_scores = np.mean(anger_pcc_scores)
joy_pcc_scores = np.mean(joy_pcc_scores)
fear_pcc_scores = np.mean(fear_pcc_scores)
sad_pcc_scores = np.mean(sad_pcc_scores)
avg_bert_emotions_pcc = (
    anger_pcc_scores + joy_pcc_scores + fear_pcc_scores + sad_pcc_scores
) / 4
print("Final PCC Score Bert :", avg_bert_emotions_pcc)


import os
import matplotlib.pyplot as plt

# Emotion labels
emotion_labels = ["Anger", "Joy", "Fear", "Sadness"]

# Vector types
vector_types = ["Vector_bert_cl", "Vector_bert", "Vector_bert_cl_ws", "bb"]

# Mean PCC scores for each vector type
mean_pcc_scores = [
    np.mean(anger_pcc_scores),
    np.mean(joy_pcc_scores),
    np.mean(fear_pcc_scores),
    np.mean(sad_pcc_scores),
]

plt.figure(figsize=(10, 6))

bars = plt.bar(vector_types, mean_pcc_scores, color="skyblue")

plt.xlabel("Vector Type")
plt.ylabel("Mean PCC Score")
plt.title("Mean PCC Scores for Different Vector Types")
plt.xticks(rotation=45)
plt.grid(axis="y")

# Set the emotion labels as tick labels on the x-axis
plt.xticks(ticks=vector_types, labels=emotion_labels)

# Add value labels on top of each bar
for bar, score in zip(bars, mean_pcc_scores):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.01,
        round(score, 4),
        ha="center",
        va="bottom",
        fontweight="bold",
    )

# Create the directory if it doesn't exist
plots_dir = "plots/bert_pcc_score"
os.makedirs(plots_dir, exist_ok=True)

# Save the figure
plt.savefig(os.path.join(plots_dir, "bert_pcc_scores.png"))

print("Bert Base Vector Done!")


print(
    "Thanks For Your Patence. Code Run Succesfull Checkout Plot Folder to see Results!"
)
