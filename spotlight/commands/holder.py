import json
from os import sep
from datetime import datetime, timedelta
from definitions import CACHE_DIR


class CacheHolder:
    playlist_cache = {}
    song_cache = {}
    artist_cache = {}
    album_cache = {}
    last_refresh = datetime.now()

    @staticmethod
    def check_reload_time(_type: str):  # will refresh every 5 minutes (300 seconds)
        time_passed = (datetime.now() - CacheHolder.last_refresh).total_seconds()
        print("checking reload")
        if time_passed > 300:
            print("reload is a go")
            CacheHolder.last_refresh = datetime.now()
            CacheHolder.reload_holder(_type)

    @staticmethod
    def reload_holder(_type: str):
        '''
        Reloads data to static variables inside of this class
        :param _type: Either song, playlist, artist, album or all
        :return:
        '''
        # load cached songs
        try:
            if _type == "song" or _type == "all":
                with open(song_cache_file_path, 'r') as f:
                    CacheHolder.song_cache = json.load(f)
            # load cached artists
            if _type == "artist" or _type == "all":
                with open(artist_cache_file_path, 'r') as f:
                    CacheHolder.artist_cache = json.load(f)
            # load cached albums
            if _type == "album" or _type == "all":
                with open(album_cache_file_path, 'r') as f:
                    CacheHolder.album_cache = json.load(f)
            # load cached playlists
            if _type == "playlist" or _type == "all":
                with open(playlist_cache_file_path, 'r') as f:
                    CacheHolder.playlist_cache = json.load(f)
        except:
            None  # First time startup with no cache


# Cached file paths
song_cache_file_path = f"{CACHE_DIR}songs.json"
playlist_cache_file_path = f"{CACHE_DIR}playlists.json"
album_cache_file_path = f"{CACHE_DIR}albums.json"
artist_cache_file_path = f"{CACHE_DIR}artists.json"
album_art_path = f"{CACHE_DIR}art{sep}"