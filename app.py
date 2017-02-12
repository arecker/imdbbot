import urlparse

from chalice import Chalice
from imdb import IMDb

app = Chalice(app_name='imdbbot')
imdb = IMDb()


@app.route('/', cors=True)
def handler():
    title = app.current_request.query_params.get('text', None)

    if not title:
        return 'Need a movie title, stupid'

    results = imdb.search_movie(title)

    if results:
        return 'http://www.imdb.com/title/tt' + results[0].getID()

    return 'Sorry - couldn\'t find "{}" on imdb.'.format(title)
