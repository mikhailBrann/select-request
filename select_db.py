from lib.db_class import music_shop
# инициализирую подключениe к БД в другом файле через класс
connection = music_shop.connection()


# название и год выхода альбомов, вышедших в 2018 году;
albums_query = connection.execute("""
    SELECT title, album_year
    FROM albums
    WHERE album_year = '2018';
""").fetchall()

print(albums_query)

# название и продолжительность самого длительного трека;
longest_track_query = connection.execute("""
    SELECT title, track_length
    FROM tracks
    ORDER BY track_length DESC
    LIMIT 1;
""").fetchall()

print(longest_track_query)

# название треков, продолжительность которых не менее 3,5 минуты;
tracks_longs_three_half_minuts_query = connection.execute("""
    SELECT title
    FROM tracks
    WHERE track_length >= '3.30';
""").fetchall()

print(tracks_longs_three_half_minuts_query)

# названия сборников, вышедших в период с 2018 по 2020 год включительно;
collections_query = connection.execute("""
    SELECT title
    FROM collections
    WHERE collection_year BETWEEN '2018' AND '2020';
""").fetchall()

print(collections_query)

# исполнители, чье имя состоит из 1 слова;
authors_query = connection.execute("""
    SELECT author_name
    FROM authors
    WHERE author_name NOT LIKE '%% %%';
""").fetchall()

print(authors_query)

# название треков, которые содержат слово "мой"/"my".
tracks_query = connection.execute("""
    SELECT title
    FROM tracks
    WHERE title ILIKE '%%my%%' OR title ILIKE '%%мой%%';
""").fetchall()

print(tracks_query)
