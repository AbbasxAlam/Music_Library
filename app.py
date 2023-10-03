from lib.database_connection import DatabaseConnection
from lib.album_repository import AlbumRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/music_library.sql")

# Retrieve all artists
album_repository = AlbumRepository(connection)
album = album_repository.all()

# List them out
for album in album:
    print(album)
