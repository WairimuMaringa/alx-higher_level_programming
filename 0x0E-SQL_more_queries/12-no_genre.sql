-- import database dump hbtn_0d_tvshows, same as task eleven
-- write a script that lists all shows in this database without a genre linked
-- use the given requirements in the task
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id is NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
