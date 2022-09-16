# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        movie = {
            "title": title,
            "genre": genre,
            "rating": rating
        }
        return movie
    else:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    i = 0
    for movie in user_data["watchlist"]:
        if title == movie["title"]:
            popped_movie = user_data["watchlist"].pop(i)
            print(popped_movie)
            user_data["watched"].append(popped_movie)
        i += 1
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    ratings = []
    if not user_data["watched"]:
        return 0.0

    for movie in user_data["watched"]:
        ratings.append(movie["rating"])
    return sum(ratings) / len(user_data["watched"])

def get_most_watched_genre(user_data):
    genre_counts = {}
    if not user_data["watched"]:
        return None
    
    for movie in user_data["watched"]:
        current_genre = movie["genre"]
        if current_genre not in genre_counts:
            genre_counts[current_genre] = 1
        else:
            genre_counts[current_genre] += 1
    
    return max(genre_counts, key=genre_counts.get)


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

