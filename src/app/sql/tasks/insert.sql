INSERT INTO tasks(
	quantity_posts
,	profile
)
VALUES(
	{quantity_posts}
,	{profile}
)
RETURNING id;