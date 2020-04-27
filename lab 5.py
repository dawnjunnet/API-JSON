import urllib.request
from urllib.parse import urlencode
import json

site = 'https://www.omdbapi.com'

searchterm = input('Please enter a search term: ')
params = urlencode({'s': searchterm, 'apikey': '1d293c01'})

response_object = urllib.request.urlopen(site + '?' + params)
response_string = response_object.read()

response_dict = json.loads(response_string)

try:
    movie = [doc['Title'] for doc in response_dict['Search']]
    for char in movie:
        movie_params = urlencode({'t': char, 'apikey': '1d293c01'})
        movie_object = urllib.request.urlopen(site + '?' + movie_params)
        movie_string = movie_object.read()
        movie_dict = json.loads(movie_string)
        print(movie_dict['Title'])
        print(movie_dict['Year'])
        print(movie_dict['Runtime'])
        print(movie_dict['Ratings'][0]['Value'])
except:
    print('No results found')


