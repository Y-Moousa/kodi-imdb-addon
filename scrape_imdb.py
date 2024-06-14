import requests
from bs4 import BeautifulSoup
import json
import os

def get_imdb_data(url, selector):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    items = []
    page = 1
    while True:
        paginated_url = f"{url}?page={page}" if page > 1 else url
        response = requests.get(paginated_url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.select(selector)
        items.extend([{'title': title.text.strip(), 'streaming_link': 'No link available'} for title in titles])
        print(f"Scraped {len(titles)} items from {paginated_url}")  # Debug print statement
        
        # Check if there is a next page
        next_button = soup.select_one('a[aria-label="Next"]')
        if not next_button:
            break
        page += 1
    return items

if __name__ == "__main__":
    # URLs for different IMDb categories
    most_watched_movies_url = 'https://www.imdb.com/chart/moviemeter/'
    in_theater_movies_url = 'https://www.imdb.com/movies-in-theaters/'
    most_watched_tv_url = 'https://www.imdb.com/chart/tvmeter/'

    # CSS selectors for the movie and TV show titles
    movie_selector = '.ipc-title--title'
    theater_selector = 'a[href*="/showtimes/title/"]'
    tv_selector = 'h3.ipc-title__text'

    # Scrape data
    movies = get_imdb_data(most_watched_movies_url, movie_selector)
    in_theater_movies = get_imdb_data(in_theater_movies_url, theater_selector)
    tv_shows = get_imdb_data(most_watched_tv_url, tv_selector)

    if not os.path.exists('data'):
        os.makedirs('data')

    with open('data/movies.json', 'w') as f:
        json.dump(movies, f, indent=4)

    with open('data/in_theater_movies.json', 'w') as f:
        json.dump(in_theater_movies, f, indent=4)

    with open('data/tv_shows.json', 'w') as f:
        json.dump(tv_shows, f, indent=4)
