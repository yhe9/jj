from flask import (render_template, request, redirect, url_for)
from . import main
from ..tmdbAPI import get_movies, get_movie, search_movie
from ..wikiAPI import wikiurlByTitle


# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    popular_movies = get_movies("popular")
    upcoming_movie = get_movies("upcoming")
    now_showing_movie = get_movies("now_playing")
    title = 'Home - Welcome to The best Movie Review Website Online'

    search_movie = request.args.get('movie_query')
    if search_movie:
        return redirect(url_for('.search', movie_name=search_movie))
    else:
        return render_template('index.html',
                               title=title,
                               popular=popular_movies,
                               upcoming=upcoming_movie,
                               now_showing=now_showing_movie)

@main.route('/popular')
def popular():
    popular_movies = get_movies("popular")
    title = 'Home - Welcome to The best Movie Review Website Online'
    search_movie = request.args.get('movie_query')
    if search_movie:
        return redirect(url_for('.search', movie_name=search_movie))
    else:
        return render_template('index.html',
                               title=title,
                               popular=popular_movies
                               )

@main.route('/nowshowing')
def nowshowing():
    now_showing_movie = get_movies("now_playing")
    title = 'Home - Welcome to The best Movie Review Website Online'
    search_movie = request.args.get('movie_query')
    if search_movie:
        return redirect(url_for('.search', movie_name=search_movie))
    else:
        return render_template('index.html',
                               title=title,
                               now_showing=now_showing_movie)

@main.route('/upcoming')
def upcoming():
    upcoming_movie = get_movies("upcoming")
    title = 'Home - Welcome to The best Movie Review Website Online'
    search_movie = request.args.get('movie_query')
    if search_movie:
        return redirect(url_for('.search', movie_name=search_movie))
    else:
        return render_template('index.html',
                               title=title,
                               upcoming=upcoming_movie)
@main.route("/movie/<int:id>")
def movie(id):
    '''
    View movie page function that returns the movie details page and its data
    '''
    movie = get_movie(id)
    title = f'{movie.title}'
    wikiurl = wikiurlByTitle(title)
    print(wikiurl)
    return render_template('movie.html',
                           id=id,
                           title=title,
                           movie=movie,
                           wikiURL=wikiurl)

@main.route('/search/<movie_name>')
def search(movie_name):
    '''
    View function to display the search results
    '''
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    title = f'search results for {movie_name}'
    return render_template('search.html',
                           title=title,
                           movies=searched_movies)
