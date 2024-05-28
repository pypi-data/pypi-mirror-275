from .dataset_upload import *
from .tweets_embedding import get_vector_bert
from .frnn import *

print("Bert Vector Process Start")

anger_data["Vector_bert"] = anger_data["Tweet"].apply(get_vector_bert)
anger_test["Vector_bert"] = anger_test["Tweet"].apply(get_vector_bert)

joy_data["Vector_bert"] = joy_data["Tweet"].apply(get_vector_bert)
joy_test["Vector_bert"] = joy_test["Tweet"].apply(get_vector_bert)

sad_data["Vector_bert"] = sad_data["Tweet"].apply(get_vector_bert)
sad_test["Vector_bert"] = sad_test["Tweet"].apply(get_vector_bert)

fear_data["Vector_bert"] = fear_data["Tweet"].apply(get_vector_bert)
fear_test["Vector_bert"] = fear_test["Tweet"].apply(get_vector_bert)

print("1st done")

anger_data["Vector_bert_cl"] = anger_data["Cleaned_tweet"].apply(get_vector_bert)
anger_test["Vector_bert_cl"] = anger_test["Cleaned_tweet"].apply(get_vector_bert)

joy_data["Vector_bert_cl"] = joy_data["Cleaned_tweet"].apply(get_vector_bert)
joy_test["Vector_bert_cl"] = joy_test["Cleaned_tweet"].apply(get_vector_bert)

sad_data["Vector_bert_cl"] = sad_data["Cleaned_tweet"].apply(get_vector_bert)
sad_test["Vector_bert_cl"] = sad_test["Cleaned_tweet"].apply(get_vector_bert)

fear_data["Vector_bert_cl"] = fear_data["Cleaned_tweet"].apply(get_vector_bert)
fear_test["Vector_bert_cl"] = fear_test["Cleaned_tweet"].apply(get_vector_bert)

print("2nd done")

# BERT
# With raw tweets

anger_data["Vector_bert_cl_ws"] = anger_data["Cleaned_tweet_wt_stopwords"].apply(
    get_vector_bert
)
anger_test["Vector_bert_cl_ws"] = anger_test["Cleaned_tweet_wt_stopwords"].apply(
    get_vector_bert
)

joy_data["Vector_bert_cl_ws"] = joy_data["Cleaned_tweet_wt_stopwords"].apply(
    get_vector_bert
)
joy_test["Vector_bert_cl_ws"] = joy_test["Cleaned_tweet_wt_stopwords"].apply(
    get_vector_bert
)

sad_data["Vector_bert_cl_ws"] = sad_data["Cleaned_tweet_wt_stopwords"].apply(
    get_vector_bert
)
sad_test["Vector_bert_cl_ws"] = sad_test["Cleaned_tweet_wt_stopwords"].apply(
    get_vector_bert
)

fear_data["Vector_bert_cl_ws"] = fear_data["Cleaned_tweet_wt_stopwords"].apply(
    get_vector_bert
)
fear_test["Vector_bert_cl_ws"] = fear_test["Cleaned_tweet_wt_stopwords"].apply(
    get_vector_bert
)


vector_names = ["Vector_bert"]
NNeighbours = [
    5,
]  # Number of neighbors to consider
lower = [1] * (NNeighbours[0] // 2)
upper = [1] * (NNeighbours[0] - len(lower))
alpha = 0.5  # Example value for alpha


from sklearn.model_selection import KFold
from scipy.stats import pearsonr


def cross_validation_ensemble_owa(
    data, vector_names, NNeighbours, lower, upper, alpha, cv=5
):
    # Function to calculate PCC score
    def calculate_pcc_score(data_vectors, test_vectors):
        pcc_scores = []
        for data_vector, test_vector in zip(data_vectors, test_vectors):
            if isinstance(data_vector, float) or isinstance(test_vector, float):
                # Skip float values
                continue
            # Convert to numpy arrays if not already
            data_vector = np.array(data_vector)
            test_vector = np.array(test_vector)
            if len(data_vector) == 0 or len(test_vector) == 0:
                # Skip empty vectors
                continue
            pcc_score, _ = pearsonr(data_vector, test_vector)
            pcc_scores.append(pcc_score)
        return pcc_scores

    # Prepare data for cross-validation
    X = data[vector_names]
    y = data["Class"]

    # Initialize lists to store PCC scores
    mean_pcc_scores = []

    # Perform cross-validation
    kf = KFold(n_splits=cv, shuffle=True, random_state=42)
    for train_index, test_index in kf.split(X):
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]

        # Calculate PCC scores for each emotion category and vector type
        pcc_scores = []
        for vector_name in vector_names:
            pcc_scores_vector = calculate_pcc_score(
                X_train[vector_name], X_test[vector_name]
            )
            pcc_scores.append(np.mean(pcc_scores_vector))

        mean_pcc_scores.append(pcc_scores)

    # Calculate mean PCC scores for each emotion category and vector type
    mean_pcc_scores = np.mean(mean_pcc_scores, axis=0)

    return mean_pcc_scores
