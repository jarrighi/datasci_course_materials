SELECT max(similarity)
FROM (

SELECT ID1, ID2, sum(similarity) AS similarity
FROM(
        SELECT a.docid AS ID1, b.docid AS ID2, a.count * b.count AS similarity
        FROM (
		SELECT * FROM frequency
		UNION
		SELECT 'q' as docid, 'washington' as term, 1 as count
		UNION
		SELECT 'q' as docid, 'taxes' as term, 1 as count
		UNION
		SELECT 'q' as docid, 'treasury' as term, 1 as count

	) a, (
                SELECT * FROM frequency
                UNION
                SELECT 'q' as docid, 'washington' as term, 1 as count
                UNION
                SELECT 'q' as docid, 'taxes' as term, 1 as count
                UNION
                SELECT 'q' as docid, 'treasury' as term, 1 as count

        ) b

        WHERE a.term = b.term
        AND a.docid = 'q'
) c
GROUP BY ID1, ID2
)

;
