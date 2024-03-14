-- 11-genre_id_all_shows.sql
-- Lists all shows contained in hbtn_0d_tvshows with associated genre ID, displaying NULL for shows without a genre

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
