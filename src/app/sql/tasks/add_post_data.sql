WITH add_post AS (
	INSERT INTO posts(
		likes
	,	post_time
	,	url
	)
	VALUES(
        {likes}
	,	{post_time}
	,	{url}
	)
	RETURNING
		id
)
INSERT INTO profile_posts(
	profile_id
,	posts_id
)
VALUES(
	(
		SELECT
			id
		FROM
			tasks
		WHERE
			profile = {profile}
	)
,	(
		SELECT
			id
		FROM
			add_post
	)
);