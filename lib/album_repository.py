from lib.album import Album

class AlbumRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all artists
    def all(self):
        rows = self._connection.execute('SELECT * from albums')
        album = []
        for row in rows:
            item = Album(row["id"], row["title"], row["release_year"], row["artist_id"])
            album.append(item)
        return album 