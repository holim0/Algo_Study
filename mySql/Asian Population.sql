select sum(c1.population)
from city c1, country c2
where c1.countrycode=c2.code
and c2.continent= "Asia"