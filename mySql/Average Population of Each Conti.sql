select c2.continent, floor(avg(c1.population))
from city c1, country c2
where c1.countrycode=c2.code
group by c2.continent