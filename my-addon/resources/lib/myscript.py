import xbmcplugin
import xbmcgui
import xbmcaddon
import sys
import json
import os

# Paths to JSON files
MOVIES_PATH = os.path.join(xbmcaddon.Addon().getAddonInfo('path'), 'data', 'movies.json')
THEATER_PATH = os.path.join(xbmcaddon.Addon().getAddonInfo('path'), 'data', 'in_theater_movies.json')
TVSHOWS_PATH = os.path.join(xbmcaddon.Addon().getAddonInfo('path'), 'data', 'tv_shows.json')

def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def list_items(items):
    for item in items:
        li = xbmcgui.ListItem(label=item['title'])
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=item['streaming_link'], listitem=li, isFolder=False)
    xbmcplugin.endOfDirectory(addon_handle)

if __name__ == '__main__':
    addon_handle = int(sys.argv[1])
    args = xbmcaddon.Addon().getAddonInfo('args')
    mode = args.get('mode', None)

    if mode is None:
        # Display main menu
        li = xbmcgui.ListItem(label='Most Watched Movies')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url='?mode=movies', listitem=li, isFolder=True)
        
        li = xbmcgui.ListItem(label='In Theater Movies')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url='?mode=theater', listitem=li, isFolder=True)
        
        li = xbmcgui.ListItem(label='Most Watched TV Shows')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url='?mode=tvshows', listitem=li, isFolder=True)
        
        xbmcplugin.endOfDirectory(addon_handle)
    elif mode == 'movies':
        # Load and display most watched movies
        movies = load_data(MOVIES_PATH)
        list_items(movies)
    elif mode == 'theater':
        # Load and display in theater movies
        theater_movies = load_data(THEATER_PATH)
        list_items(theater_movies)
    elif mode == 'tvshows':
        # Load and display most watched TV shows
        tv_shows = load_data(TVSHOWS_PATH)
        list_items(tv_shows)
