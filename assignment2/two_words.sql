SELECT count(*)
FROM frequency a, frequency b
WHERE 
	a.term = 'transactions' AND
	b.term = 'world' AND
	a.docid = b.docid
;
