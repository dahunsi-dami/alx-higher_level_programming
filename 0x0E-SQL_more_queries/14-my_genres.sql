-- import database dump from s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql
-- list all genres of the show `Dexter`
-- tv_shows contains only 1 record where `title` = `Dexter`, but id can be different
-- each record should display tv_genres.name
-- sort results in ascend order by genre name
-- you can only use SELECT statement
-- db name will be passed as arg of mysql command

SELECT tv_genres.name FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name;
