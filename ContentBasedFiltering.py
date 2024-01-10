class BookRecommender:
    def __init__(self, books_data):
        self.books_data = books_data

    def recommend_books(self, selected_genre):
        recommended_books = []

        for book_title, book_info in self.books_data.items():
            # Check if the selected genre is in the book's genres
            if selected_genre in book_info['genres']:
                recommended_books.append(book_title)

        return recommended_books


# Example books data with numerical genres
books_data = {
    'The Silent Detective': {'genres': [1, 3]},      # Mystery, Thriller
    'Love in Bloom': {'genres': [2, 4]},              # Romance, Drama
    'Galactic Odyssey': {'genres': [5, 6]},           # Science Fiction, Adventure
    'Laugh Out Loud': {'genres': [7, 8]},             # Comedy, Fantasy
    'Twisted Secrets': {'genres': [3, 1]},            # Thriller, Mystery
    'Starry Nights': {'genres': [2, 5]},              # Romance, Science Fiction
    'Drama on Everest': {'genres': [4, 6]},           # Drama, Adventure
    'The Enchanted Mystery': {'genres': [1, 8]},      # Mystery, Fantasy
    'Comedy Central': {'genres': [7, 3]},             # Comedy, Thriller
    'Whimsical Tales': {'genres': [4, 7]}             # Drama, Comedy
}

# Genre mapping
genre_mapping = {
    1: 'Mystery',
    2: 'Romance',
    3: 'Thriller',
    4: 'Drama',
    5: 'Science Fiction',
    6: 'Adventure',
    7: 'Comedy',
    8: 'Fantasy'
}

# Display genre options
print("Genre Options:")
for num, genre in genre_mapping.items():
    print(f"{num}: {genre}")

# Get user input for the selected genre
selected_genre = int(input("Enter the number of the genre you want to explore: "))

# Create a book recommender instance
book_recommender = BookRecommender(books_data)

# Get recommended books based on the selected genre
recommended_books = book_recommender.recommend_books(selected_genre)

# Display the recommended books
if recommended_books:
    print("Recommended Books:")
    for book in recommended_books:
        print(f"- {book}: {books_data[book]['genres']}")
else:
    print("No books found for the selected genre.")
