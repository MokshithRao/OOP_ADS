class Song:
    def __init__(self, title, artist, album, genre, duration) -> None:
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.duration = duration

    
    def display_details(self):
        return f"Title: {self.title}, Artist: {self.artist}, Album: {self.album}, Genre: {self.genre}, Duration: {self.duration}"
    

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        
    def get_songs(self):
        return self.songs
   

    def remove_song(self, identifier):
        for i in self.songs:
            if i.title == identifier:
                self.songs.remove(i)
                return True
        return False


    def filter_songs(self, criteria, value):
        filter = []
        if criteria == 'genre':
            for i in self.songs:
                if value.lower() in i.genre.lower():
                    filter.append(i)
        
        elif criteria == 'artist':
            for i in self.songs:
                if value.lower() in i.artist.lower():
                    filter.append(i)
        return filter


    def search_songs(self, keyword):
        search = []
        for i in self.songs:
            if keyword.lower() in i.title.lower() or keyword.lower() in i.artist.lower() or keyword.lower() in i.album.lower() or keyword.lower() in i.genre.lower():
                search.append(i)
        return search




class PlaylistManager:
    def __init__(self):
        self.playlists = []
       

    def create_playlist(self, name):
        self.playlists.append(Playlist(name))
    
    def list_playlists(self):
        return self.playlists

    def get_playlist(self, name):
        for i in self.playlists:
            if i.name == name:
                return i
        return None
    

    def delete_playlist(self, name):
        for i in self.playlists:
            if i.name == name:
                self.playlists.remove(i)
                return True
        return False
        
        
    def cross_playlist_search(self, keyword):
        songs = []
        for i in self.playlists:
            songs.extend(i.search_songs(keyword))
        return songs
            
