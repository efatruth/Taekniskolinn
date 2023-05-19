#LIVINUS FELIX BASSEY
#SKILAVERKEFNI 4
#Country töfluna
#1. 
  SELECT Name
      FROM country
      WHERE continent = "Europe";

#2.  
 SELECT SUM(population) AS "Heildar íbúafjöldi"
      FROM country;

#3.
   SELECT Name
      FROM country
      WHERE SurfaceArea >600000;

#4.
   SELECT Name
      FROM country
      WHERE indepYear > 1920;

#5.
   SELECT Name
      FROM country
      WHERE population > 10000000 and population < 20000000;

#6.
   SELECT Name
      FROM country
      WHERE GNPOld != "NULL";
#7.
    SELECT Name
      FROM country
      WHERE Name != LocalName;


#8.
   SELECT COUNT(Name)AS "Fjöldi landa"
           FROM country
           GROUP BY Continent;

#9.
   SELECT ROUND(AVG(LifeExpectancy),3)AS "Meðal lífslíkur í heiminum "
      FROM country;

#10.
   SELECT SUM(GNP)AS "Heildar GNP í heiminum"
         FROM country;

#11.
     SELECT COUNT(Name)AS "Fjöldi landa í Asíu"
           FROM country
           GROUP BY Continent
           HAVING Continent = "Asia";

#12.
     SELECT Name
           FROM country
           WHERE Continent = "Asia" AND Population >= 10000000;

#13.
     SELECT Name
           FROM country
           WHERE GovernmentForm = "Constitutional Monarchy";

#14.
     SELECT Name
	FROM country
	WHERE GNPOld > GNP;



#15.
      SELECT GovernmentForm, COUNT(Name) AS "Fjöldi landa"
	FROM country
	GROUP BY GovernmentForm;

#16.
     SELECT Continent, Name
	FROM country
	WHERE Continent = "Asia" OR Continent = "Europe"
	ORDER BY Continent;

#17.
     SELECT Continent, COUNT(Name) AS "Fjöldi landa"
	FROM country
	GROUP BY Continent
	ORDER BY COUNT(Name);

#18.
     SELECT Continent, COUNT(Name) AS "Fjöldi landa"
	FROM country
	GROUP BY Continent
	HAVING COUNT(Name) > 20;


#Countrylanguage

#1.
	SELECT Language
	FROM countryLanguage
	WHERE CountryCode = "ARG";

#2.
	SELECT Language
	FROM countryLanguage
	 WHERE CountryCode = "ARG" AND IsOfficial = "T";



#3.
	SELECT Language
	FROM countrylanguage
	WHERE CountryCode = "ARG" AND IsOfficial = "T";

#4.
	SELECT CountryCode
	FROM countrylanguage
	WHERE Percentage < 50;

#5.
	SELECT CountryCode
	FROM countrylanguage
	WHERE percentage < 50
	GROUP BY CountryCode;


#6.
	SELECT CountryCode, Language
	FROM countrylanguage
	WHERE Percentage > 90;

#7.
	SELECT CountryCode, Language
	FROM countrylanguage
	WHERE Percentage < 5;

#8.
	SELECT CountryCode, Language
	FROM countrylanguage
	WHERE Language = "English" AND IsOfficial = "T";

#9.
	SELECT Language, COUNT(CountryCode) AS "Hversu mörgum löndum tungumálið er talað"
	FROM countrylanguage
	GROUP BY Language;


#10.
	SELECT CountryCode,Language 
	FROM countrylanguage
	WHERE CountryCode
	GROUP BY Language > 5;


















