SELECT sum(similarity)
FROM(
	SELECT a.docid AS ID1, b.docid AS ID2, a.count * b.count AS similarity
	FROM frequency a, frequency b
	WHERE a.term = b.term
	AND a.docid = '10080_txt_crude'
	AND b.docid = '17035_txt_earn'
) c
GROUP BY ID1, ID2
;
