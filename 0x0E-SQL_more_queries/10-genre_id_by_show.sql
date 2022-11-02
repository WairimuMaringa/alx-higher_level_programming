-- import the database dump from hbtn_0d_tvshows to your MySQL server
-- write a script displaying all shows in that database that have at least one genre linked
-- each record should display tv_shows.title tv_show_genres.genre.id and sorted in ascending order
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_shows_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
