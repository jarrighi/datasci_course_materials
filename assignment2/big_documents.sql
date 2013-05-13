SELECT count(docid)
FROM(
	SELECT docid, sum(count) AS num_words
	FROM frequency
	GROUP BY docid
)
WHERE num_words > 300
;
