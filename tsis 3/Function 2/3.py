# Dictionary of movies

movies=[
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

# Task 1: Check if the imdb score of a movie is above 5.5
def is_above_5_5(movie):
    return movie["imdb"] > 5.5

# Task 2: Return a sublist of movies with an imdb score above 5.5
def above_5_5_movies(movie_list):
    return [movie for movie in movie_list if is_above_5_5(movie)]

# Task 3: Return movies under a specific category
def movies_by_category(movie_list, category):
    return [movie for movie in movie_list if movie["category"] == category]

# Task 4: Compute the average imdb score of a list of movies
def average_imdb_score(movie_list):
    if not movie_list:
        return 0
    total_score = sum(movie["imdb"] for movie in movie_list)
    return total_score / len(movie_list)

# Task 5: Compute the average imdb score for a specific category
def average_imdb_score_by_category(movie_list, category):
    category_movies = movies_by_category(movie_list, category)
    return average_imdb_score(category_movies)

# Example usage:
print(is_above_5_5(movies[0]))
print(above_5_5_movies(movies))
print(movies_by_category(movies, "Romance"))
print(average_imdb_score(movies))
print(average_imdb_score_by_category(movies, "Suspense"))