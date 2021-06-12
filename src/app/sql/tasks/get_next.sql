SELECT
	*
FROM
	tasks
WHERE
	status = 'Не выполнено' OR
	status = 'Ошибка'
LIMIT 1 OFFSET {offset};