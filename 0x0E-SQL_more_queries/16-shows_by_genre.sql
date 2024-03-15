-- import database dump from s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql
-- list all shows & all genres linked to that show from database hbtn_0d_tvshows
-- if a show doesn't have a genre, display NULL in genre column
-- each record should display tv_shows.title, tv_genres.name
-- sort results in ascend order by show title and genre name
-- you can only use SELECT statement
-- db name will be passed as arg of mysql command

SELECT tv_shows.title, tv_genres.name FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title, tv_genres.name;
