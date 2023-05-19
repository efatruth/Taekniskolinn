CREATE DATABASE 0301865919_lokaverkefni;
use 0301865919_lokaverkefni;

CREATE TABLE tegund
(
	ID INT PRIMARY KEY,
    nafn varchar(255)
);


CREATE TABLE flokkur
(
	ID INT PRIMARY KEY,
    nafn varchar(255)
);


CREATE TABLE utgefandi
(
	ID INT PRIMARY KEY,
    nafn varchar(255)
);

CREATE TABLE flytjandi
(
	ID INT(11) PRIMARY KEY,
    nafn varchar(255),
    faedingardagur date NOT NULL,
    lysing TEXT,
    danardagur date NULL,
    flokkur_flytjanda INT,
    FOREIGN KEY (flokkur_flytjanda) REFERENCES flokkur(ID)
);


CREATE TABLE diskur
(
	ID INT PRIMARY KEY,
    nafn varchar(255),
    utgafudagur date NOT NULL,
    tegund_disks int,
    flytjandi_disks int,
    utgefandi_disks int,
    FOREIGN KEY (tegund_disks) REFERENCES tegund(ID),
    FOREIGN KEY (utgefandi_disks) REFERENCES utgefandi(ID)
);


CREATE TABLE lag
(
	ID INT PRIMARY KEY,
    nafn varchar(255),
    texti varchar(255),
    lengd char(255),
    flytjandi int,
    diskur int,
    FOREIGN KEY (flytjandi) REFERENCES flytjandi(ID),
    FOREIGN KEY (diskur) REFERENCES diskur(ID)
);


INSERT INTO
tegund(ID,nafn)
VALUES
(1998,"Pop"),
(2010,"Rock"),
(2012,"Jazz"),
(2014,"Disco"),
(2016,"Pop");


INSERT INTO
flokkur(ID,nafn)
VALUES
(1,"solo"),
(2,"band"),
(3,"choir"),
(4,"duo");


INSERT INTO
utgefandi(ID,nafn)
VALUES
(4,"blessrecords"),
(8,"goodrecords"),
(16,"musicrecords"),
(32,"divinerecords");


INSERT INTO
flytjandi(ID,nafn,faedingardagur,lysing,danardagur,flokkur_flytjanda)
VALUES
(1,"Ajosh","1966-10-23","Snillingur","2012-06-08",1),
(2,"Awilos","1960-11-24","Rokkarinn mikli",null,1),
(3,"tosh","1967-09-25","Snillingur","2011-05-06",4),
(4,"marley","1980-07-22","Snillingur","2010-07-09",2),
(5,"jackson","1963-09-20","Rokkarinn mikli",null,3);

INSERT INTO
diskur(ID,nafn,utgafudagur,tegund_disks,flytjandi_disks,utgefandi_disks)
VALUES
(1,"repent","1998-06-03",1998,30,4),
(2,"thekingdom","2010-04-02",2010,40,8),
(3,"midnightcry","2012-05-01",2012,50,16),
(4,"prophecy","2014-07-04",2014,60,32),
(5,"thegreatday","2016-08-05",2016,70,64),
(6,"dreadfulday","2010-09-06",2010,80,128),
(7,"ofthelord","2017-02-07",2017,90,256);

INSERT INTO
lag(ID,nafn,texti,lengd,flytjandi,diskur)
VALUES
(2,"thanks","paiseGOD","fiveminuites",30,4),
(4,"praise","paises","fourminuites",30,4),
(6,"three","his","threeminuites",30,4),
(8,"four","Goodness","twominuites",30,4),
(10,"five","forhis","sixminuites",30,4),
(12,"six","mercies","sevenminuites",30,4),
(14,"seven","endures","eightminuites",30,4),
(16,"eight","forever","nineminuites",30,4),
(18,"nine","iwill","tenminuites",30,4),
(20,"ten","sing","elevenminuites",30,4),
(22,"eleven","unto","fiveminuites",30,4),
(24,"twelve","thelord","sixminuites",30,4),
(26,"thirteen","for","sevenminuites",30,4),
(28,"fourteen","hisgoodness","eightminuites",30,4),
(30,"fifteen","great","nineminuites",30,4),
(32,"sixteen","isthe","tenminuites",30,4),
(34,"seventeen","mystery","elevenminuites",30,4),
(36,"eighteeen","ofgodliness","twominuites",30,4),
(38,"nineteen","manifested","threeminuites",30,4),
(40,"twenty","intoflesh","fourminuites",30,4);

select nafn,texti from lag where ID = 4

select nafn,lysing from flytjandi where ID >= 4

select nafn,texti from lag where ID = 12

select * from lag where ID >= 10 and ID <= 20

select * from diskur where ID > 2

select diskur.nafn, utgefandi.nafn, flytjandi.nafn
from ((diskur
inner join utgefandi on diskur.utgefandi_disks = utgefandi.ID)
inner join flytjandi on diskur.ID = flytjandi.ID);

select lag.lengd, flytjandi.nafn, utgefandi.nafn
from ((lag
inner join flytjandi on lag.ID = flytjandi.ID)
inner join utgefandi on lag.ID = utgefandi.ID);

select lengd from lag
union
select nafn from flytjandi;


select nafn, faedingardagur
from flytjandi;

select ID from tegund
union
select nafn from utgefandi;

