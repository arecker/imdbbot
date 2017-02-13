import urlparse

from chalice import Chalice
from imdb import IMDb

app = Chalice(app_name='imdbbot')
imdb = IMDb()


def to_response(text, public=True):
    response = {
        'text': text,
        'unfurl_links': True
    }

    if public:
        response['response_type'] = 'in_channel'

    return response


@app.route('/', cors=True)
def handler():
    title = app.current_request.query_params.get('text', None)

    if not title:
        return to_response('Need a movie title, stupid', public=False)

    results = imdb.search_movie(title)

    if results:
        return to_response('http://www.imdb.com/title/tt' + results[0].getID())

    return to_response(
        'Sorry - couldn\'t find "{}" on imdb.'.format(title),
        public=False
    )
