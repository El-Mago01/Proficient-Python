from top250 import top250movies

def get_title_by_rank(rank:int):
    return top250movies[rank-1 ]['title']

def get_rank_by_title(title):
    for movie in top250movies:
        if movie['title'] == title:
            return movie['rank']
    return -1

def most_appearing_actor():
    actors = []

    for movie in top250movies:
        for actor in movie['actors']:
            actors.append(actor)
    actors_set = set(actors)
    appearing_actors = []
    for actor in actors_set:
        appearing_actors.append((actors.count(actor), actor))
    appearing_actors.sort(key=lambda x: x[0], reverse=True)
    print(appearing_actors)
    print(f"Most frequent appearing actor is: {appearing_actors[0][1]}, appearing {appearing_actors[0][0]} times")


def most_appearing_duo_actor_director():
    duo_director_actor = []
    for movie in top250movies:
        director = movie['director']
        for actor in movie['actors']:
            duo_director_actor.append((director, actor))
    duo_director_actor_set = set(duo_director_actor)
    print(duo_director_actor_set)
    top_duo_nr = 0
    top_pair = ("","")
    for director_actor in duo_director_actor_set:
        this_duo_nr = duo_director_actor.count(director_actor)
        if this_duo_nr > top_duo_nr:
            top_duo_nr = this_duo_nr
            top_pair = director_actor
            print(top_pair)
    print(f"The best director/actor duo with {top_duo_nr} films together is:")
    print(top_pair)


def rank_top_decades():
    # What is the decade that has the most movies in the top 250
    bins = [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020]
    number_per_bin = [0,0,0,0,0,0,0,0,0,0,0,]

    for movie in top250movies:
        bin = (int(movie['year']) // 10) * 10
        bin_index = bins.index(bin)
        number_per_bin[bin_index] += 1
    highest_nr_of_films_per_decade = max(number_per_bin)
    number_of_highest_decades = number_per_bin.count(highest_nr_of_films_per_decade)
    best_decade_list = []
    for nr_of_best_decades in range(number_of_highest_decades):
        index_best_bin = number_per_bin.index(highest_nr_of_films_per_decade)
        best_decade_list.append(bins[index_best_bin])
    print(f"The following decade(s) has/have {highest_nr_of_films_per_decade}:")
    for decade in best_decade_list:
        print(f"decade: {decade}"
)


def main():
    title = 'The Good, the Bad and the Ugly'
    rank = get_rank_by_title(title)
    print(f"The rank of {title} is {rank}")

    rank = 30
    title = get_title_by_rank(rank)
    print(f"The title for the film in ranking {rank} is {title}")

    most_appearing_actor()
    rank_top_decades()
    most_appearing_duo_actor_director()
if __name__ == '__main__':
    main()
