SELECT IF (Grades.Grade > 7, Students.Name, NULL) AS Sname, Grades.Grade, Students.Marks FROM Students 
INNER JOIN Grades ON Students.Marks BETWEEN Grades.Min_Mark AND Max_Mark
ORDER BY Grades.Grade DESC, Sname ASC, Students.Marks ASC;