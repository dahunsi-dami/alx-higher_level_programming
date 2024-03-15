-- import database dump from s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql
-- list all comedy shows in the database hbtn_0d_tvshows
-- tv_shows contains only 1 record where `name` = `Comedy`, but id can be different
-- each record should display tv_genres.title
-- sort results in ascend order by genre name
-- you can only use SELECT statement
-- db name will be passed as arg of mysql command

SELECT tv_shows.title FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title;
