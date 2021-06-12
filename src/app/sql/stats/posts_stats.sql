WITH get_user_posts AS (
	SELECT
		t.profile
	,	count(p.*) quantity_posts
	,	sum(p.likes) sum_likes
	FROM
		profile_posts
	LEFT JOIN
		posts p
			ON p.id = profile_posts.posts_id
	LEFT JOIN
		tasks t
			ON t.id = profile_posts.profile_id
	GROUP BY
		t.profile
)
SELECT
    *
FROM
    get_user_posts gup
ORDER BY gup.sum_likes DESC;