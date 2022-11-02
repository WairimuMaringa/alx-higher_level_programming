-- import the database dump hbtn_0d_tvshows to your MySQL server like in task 14
-- write a script that lists all comedy shows in this database according to the given requirements
SELECT tv_shows.title
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
INER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_genres.name = "Comedy"
ORDER BY tv_shows.title;
