SELECT count(distinct species) "Acacia Types"
FROM taxonomy
WHERE species LIKE 'Acacia %';
