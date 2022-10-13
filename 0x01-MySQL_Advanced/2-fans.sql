-- ranks country of origin of bands ordered fans
SELECT origin, SUM(fans) AS nb_fans GROUP BY origin ORDER BY nb_fans
