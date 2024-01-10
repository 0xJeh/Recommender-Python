import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# User-Item Matrix
ratings_matrix = np.array([
    [4, 5, 2, np.nan],
    [3, 2, np.nan, 5],
    [np.nan, 3, 5, 2]
])

# cosine similarity
def item_similarity(matrix):
    # Replace NaN with 0 for the calculation
    matrix = np.nan_to_num(matrix)
    # Calculate cosine similarity between items
    similarity = cosine_similarity(matrix.T)
    # Fill diagonal elements with zeros to avoid self-similarity
    np.fill_diagonal(similarity, 0)
    return similarity

# Function to predict ratings for unrated items
def predict_ratings(user_ratings, item_similarity):
    user_ratings = np.nan_to_num(user_ratings)

    # Calculate the weighted sum of ratings using item similarity
    weighted_sum = np.dot(user_ratings, item_similarity)
    # Calculate the sum of similarity values
    sum_similarity = np.sum(item_similarity, axis=0)
    sum_similarity[sum_similarity == 0] = 1
    # Predict the ratings
    predicted_ratings = weighted_sum / sum_similarity
    # Set predicted ratings for already rated items to NaN
    predicted_ratings[user_ratings != 0] = np.nan

    return predicted_ratings

# Calculate item similarity
item_sim = item_similarity(ratings_matrix)

# Predict ratings for unrated items
predicted_ratings = predict_ratings(ratings_matrix, item_sim)

actual_ratings_matrix = np.nan_to_num(ratings_matrix)


print("Combined Ratings Matrix:")
print("{:<12} {:<12} {:<12} {:<12} {:<12} {:<12}".format("Actual 1", "Actual 2", "Actual 3", "Actual 4", "Predicted", "Mutual"))
for i in range(ratings_matrix.shape[0]):
    combined_row = []
    for j in range(ratings_matrix.shape[1]):
        actual_rating = int(ratings_matrix[i, j]) if not np.isnan(ratings_matrix[i, j]) else 0
        predicted_rating = predicted_ratings[i, j]
        combined_value = "{:.2f}".format(predicted_rating) if actual_rating == 0 else actual_rating
        combined_row.append("{:<12}".format(str(combined_value)))
    mutual_ratings_row = ["{:<12}".format(str(int(actual))) if not np.isnan(actual) else "{:<12}".format("") for actual in ratings_matrix[i]]
    print(" ".join(combined_row + mutual_ratings_row))
