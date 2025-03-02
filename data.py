# List of movies

favourite_movies = [
    {
        "title": "Kill Bill",
        "year": 2003,
        "rating": 8.2,
        "directors": ["Quentin Tarantino"],
        "writers": ["Quentin Tarantino"],
        "actors": ["Uma Thurman", "Lucy Liu", "David Carradine"],
        "genres": ["Action", "Comedy", "Drama"],
        "description": "A pregnant assassin, code-named The Bride, goes into a coma for four years after her ex-boss Bill brutally attacks her. When she wakes up, she sets out to seek revenge on him and his associates."
    },
    {
        "title": "Matrix",
        "year": 1999,
        "rating": 8.7,
        "directors": ["Lana Wachowski", "Lilly Wachowski"],
        "writers": ["Lana Wachowski", "Lilly Wachowski"],
        "actors": ["Keanu Reeves", "Carrie-Anne Moss", "Laurence Fishburne"],
        "genres": ["Action", "Noir", "Drama"],
        "description": "Neo, a computer programmer and hacker, has always questioned the reality of the world around him. His suspicions are confirmed when Morpheus, a rebel leader, contacts him and reveals the truth to him."
    },
    {
        "title": "Madagascar",
        "year": 2005,
        "rating": 6.9,
        "directors": ["Simon J. Smith", "David Soren"],
        "writers": ["Tom McGrath", "Eric Darnell"],
        "actors": ["Chris Rock", "Chris Miller"],
        "genres": ["comedy"],
        "description": "Four spoiled animals from the New York Central Zoo escape with the unintentional help of four fugitive penguins. They subsequently find themselves in Madagascar amidst happy lemurs."
    },
    {
        "title": "Dumb and Dumber",
        "year": 1994,
        "rating": 7.3,
        "directors": ["Peter Farrelly"],
        "writers": ["Peter Farrelly"],
        "actors": ["Jim Carry"],
        "genres": ["comedy"],
        "description": "Lloyd and Harry stumble upon a suitcase full of money left behind by Mary. Unaware that the money is connected to a kidnapping case, they try to return it only to be pursued by killers and the police."
    }
]

# The for loop

for movies in favourite_movies:
    print(movies["title"])

# The while loop

a = 0

while a < len(favourite_movies):
    print(favourite_movies[a]["title"])
    a += 1

# Average rate

total_rate = 0

for movies in favourite_movies:
    total_rate += movies['rating']
average_rate = total_rate / len(favourite_movies)
print(average_rate)

# Newest movie

newest_movie = favourite_movies[0]

for movies in favourite_movies:
    if movies["year"] > newest_movie["year"]:
        newest_movie = movies
print(newest_movie["title"])

# Combined loops

actors_by_movies = ""
for movies in favourite_movies:
    actors_by_movies += movies["title"] + "\n\n"
    for actor in movies["actors"]:
        actors_by_movies += actor + ",\n"
    actors_by_movies += "\n_\n\n"
print(actors_by_movies)