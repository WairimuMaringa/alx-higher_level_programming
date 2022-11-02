-- import the database dump of hbtn_0d_tvshows to your server, same as task ten
-- write a script containing all shows in that database with the given conditions
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
