
from movies import movies_alt_1, movies_alt_2, movies_alt_3
# movies_alt_1={
#      '1' : { 
#         'name' : 'The Swawshank Redemption',
#         'year'  : '1994',
#         'imdb_rank' : 9.9,
#         'director' : 'Frank Darabont',
#         'actors' : ['Tim Robbins', 'Morgan Freeman', 'Bob Gunton']
#     },
#     '2' : {
#         'name' : 'The Godfather',
#         'year'  : '1972',
#         'imdb_rank' : 9.0,
#         'director' : 'Francis Ford Coppola',
#         'actors' : ['Marlon Brando', 'Al Pacino', 'James Caan']
#     }
# }
# 
# movies_alt_2={
#     'The Swawshank Redemption' : {
#         'year'  : '1994',
#         'imdb_rank' : 9.9,
#         'director' : 'Frank Darabont',
#         'actors' : ['Tim Robbins', 'Morgan Freeman', 'Bob Gunton']
#     },
#     'The Godfather' : {
#         'year'  : '1972',
#         'imdb_rank' : 9.0,
#         'director' : 'Francis Ford Coppola',
#         'actors' : ['Marlon Brando', 'Al Pacino', 'James Caan']
#     }
# }
# movies_alt_3=[{
#     'name' : 'The Swawshank Redemption',
#     'year'  : '1994',
#     'imdb_rank' : 9.9,
#     'director' : 'Frank Darabont',
#     'actors' : ['Tim Robbins', 'Morgan Freeman', 'Bob Gunton']
# },{
#     'name' : 'The Godfather',
#     'year'  : '1972',
#     'imdb_rank' : 9.0,
#     'director' : 'Francis Ford Coppola',
#     'actors' : ['Marlon Brando', 'Al Pacino', 'James Caan']
# }]
# For all 3 alternatives, let's do the following 3 activities
# 1 get the top 10 movies:
# 2 get the actors of the film "The Godfather"
# 3 See in what films Al Pacino played.
# imagine this to be for 250 films

# 1. Get the top 10 movies
# Alternative 1:
print("ALTERNATIVE 1 - EXERCISE 1")
for place in range(2):
    print(movies_alt_1[str(place+1)]['name'])

# Alternative 2
# Not possible as Alternative 2 structure does not contain the ranking
# print("ALTERNATIVE 2 - EXERCISE 1")
# ranking_list = []
# for movie in movies_alt_2:
#     ranking_list.append((movies_alt_2[movie]['imdb_rank'], movie))
# ranking_list.sort(reverse=True)
# print(ranking_list)

# Alternative 3 BEST SOLUTION FOR THIS CHALLENGE
print("ALTERNATIVE 3 - EXERCISE 1")
top_2 = movies_alt_3[:2]
for movie in top_2:
    print(movie['name'])

# 2 get the actors of the film "The Godfather".
# Alternative 1:
print("ALTERNATIVE 1 - EXERCISE 2")
film = "The Godfather"
for movie in movies_alt_1:
    # print(movies_alt_1[movie]['actors'])
    if film in movies_alt_1[movie]['name']:
        print(movies_alt_1[movie]['actors'])

# Alternative 2 BEST SOLUTION FOR THIS CHALLENGE
print("ALTERNATIVE 2 - EXERCISE 2")
print(movies_alt_2[film]['actors'])

# Alternative 3
print("ALTERNATIVE 3 - EXERCISE 2")
for movie in movies_alt_3:
    if movie['name'] == film:
        print(movie['actors'])

# 3 See in what films Marlon Brando played.
actor = "Marlon Brando"

# Alternative 1:
print("ALTERNATIVE 1 - EXERCISE 3")
for movie in movies_alt_1:
    if actor in movies_alt_1[movie]['actors']:
        print(movies_alt_1[movie]['name'])

print("ALTERNATIVE 1 - EXERCISE 3 - OPTIMIZED")
for ranking, movie in movies_alt_1.items():
    if actor in movie['actors']:
        print(movie['name'])

# Alternative 2:
print("ALTERNATIVE 2 - EXERCISE 3")
for movie in movies_alt_2:
    if actor in movies_alt_2[movie]['actors']:
        print(movie)

# A better way is:
print("ALTERNATIVE 2 - EXERCISE 3 - OPTIMIZED")
for name, movie in movies_alt_2.items():
    if actor in movie['actors']:
        print(name)


# Alternative 3 - is a bit better than Alternative a and Alternative 2
# as lists are more optimized for looping
print("ALTERNATIVE 3 - EXERCISE 3")
for movie in movies_alt_3:
    if actor in movie['actors']:
        print(movie['name'])

