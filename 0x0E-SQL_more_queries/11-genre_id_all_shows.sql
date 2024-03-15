-- import database dump from s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql
-- list all shows in hbtn_0d_tvshows
-- display tv_shows.title, tv_show_genres.genre_id
-- sort results in ascend order by tv_shows.title and tv_show_genres.genre.id
-- if a show doesn't have a genre, display NULL
-- you can only use SELECT statement
-- db name will be passed as arg of mysql command

SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
