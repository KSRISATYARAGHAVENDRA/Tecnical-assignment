SELECT t.species as wheat_type ,
		r.length as dna_sequence_length
FROM taxonomy t 
join rfamseq r
on t.ncbi_id = r.ncbi_id
where t.species like 'Triticum%'
order by r.length desc
limit 1;
