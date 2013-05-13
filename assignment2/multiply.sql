SELECT c.row_num, c.col_num, sum(c.value)
FROM(
	SELECT a.row_num AS row_num, b.col_num AS col_num, a.value * b.value AS value
	FROM a, b
	WHERE a.col_num = b.row_num
) c
GROUP BY c.row_num, c.col_num;


