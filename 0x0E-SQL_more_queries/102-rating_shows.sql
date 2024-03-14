-- 102-rating_shows.sql
-- Lists all shows from hbtn_0d_tvshows_rate by their rating

SELECT tv_shows.title, SUM(ratings.rating) AS rating_sum
FROM tv_shows
JOIN ratings ON tv_shows.id = ratings.show_id
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;
