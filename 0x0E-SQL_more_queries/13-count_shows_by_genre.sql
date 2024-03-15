-- import database dump from s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql
-- list all shows in hbtn_0d_tvshows & display number of shows linked to each
-- display genre, number_of_shows
-- don't display genres w/ no shows linked
-- sort results in descend order by number of shows linked
-- you can only use SELECT statement
-- db name will be passed as arg of mysql command

SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name ORDER BY number_of_shows DESC;
