# Compulsory task 2

import spacy

nlp = spacy.load("en_core_web_md")

movie_description = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, 
the Illuminatu trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land
on the planet Sakaar where he is sold into slavery and trained as a gladiator."""

def read_movies():
    with open("movies.txt", 'r') as file:
        movies = [line.rstrip('\n').split(' :') for line in file]

    return movies

def movie_recomendation(movie_description):
    model_description = nlp(movie_description)
    most_similar_movie_title = ""
    largest_similarity = 0.0

    for movie in movies:
        similarity = nlp(movie[1]).similarity(model_description)
        if similarity > largest_similarity:
            largest_similarity = similarity
            most_similar_movie_title = movie[0]
    
    return f"Since you have watched Planet Hulk you should watch {most_similar_movie_title} next."

movies = read_movies()
print(movie_recomendation(movie_description))