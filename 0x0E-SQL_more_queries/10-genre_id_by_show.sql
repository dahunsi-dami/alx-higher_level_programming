-- import database dump from s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql
-- list all shows in hbtn_0d_tvshows having at least 1 genre linked
-- display tv_shows.title, tv_show_genres.genre_id
-- sort results in ascend order by tv_shows.title and tv_show_genres.genre.id
-- you can only use SELECT statement
-- db name will be passed as arg of mysql command

SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
