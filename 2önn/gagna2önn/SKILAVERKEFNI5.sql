drop database 0301865919_skilaverkefni_5;
create database 0301865919_skilaverkefni_5;
use 0301865919_skilaverkefni_5;



create table kaupandi
(
	
	kt char(10) primary key, 
    nafn_kaupanda varchar(35)
);

create table solumadur
(
	id int(11)PRIMARY KEY,
    nafn_solumadur varchar(30)
);

create table seljandi
(
	
	kt char(10) primary key, 
    nafn_seljanda varchar(35)
);



create table bill
(
	fastanumer char(5) PRIMARY KEY,
    tegund varchar(15),
    litur varchar(10),
    asett_verð double,
    seljandi_kt char(10),
    FOREIGN KEY(seljandi_kt) REFERENCES seljandi(kt)
);

create table sala
(
	Numer INT (11) PRIMARY KEY,
    bill_fastanumer char(5),
	kaupandi_kt char(10),
    solumadur_id int(11),
	FOREIGN KEY (bill_fastanumer) REFERENCES bill(fastanumer),
    FOREIGN KEY (kaupandi_kt) REFERENCES kaupandi(kt),
    FOREIGN KEY (solumadur_id) REFERENCES solumadur(id),
    verd double
);


INSERT INTO
kaupandi(KT,NAFN_kaupanda)
VALUES
("0102916765","will"),
("0105926765","ole"),
("0103976745","totti"),
("0102995731","smari"),
("0908988765","afei"),
("0102918619","elix"),
("0102981100","eina"),
("1202932222","ingvi"),
("2502906755","hannes"),
("1708988188","jon");


INSERT INTO
seljandi(KT,NAFN_Seljanda)
VALUES
("0102916765","esther"),
("0105926765","sofi"),
("0103976745","asdis"),
("0102995731","olafur"),
("0908988765","reuben"),
("0403903344","grimur"),
("0304941112","elsa"),
("0203922111","marin"),
("0102973331","elin"),
("1008895554","kali");


INSERT INTO
solumadur(id,NAFN_solumadur)
VALUES
(1,"david"),
(2,"arun"),
(3,"danni"),
(4,"gusti"),
(5,"tappa"),
(6,"safi"),
(7,"eva"),
(8,"hopni"),
(9,"petur"),
(10,"harry");

INSERT INTO
bill(fastanumer,tegund,litur,asett_verð,seljandi_kt)
VALUES
(2,"BMW","blue","900000","0102916765"),
(4,"Ford","red","450000","0105926765"),
(6,"renault","white","550000","0103976745"),
(8,"volkswagen","black","600000","0102995731"),
(10,"toyota","blue","300000","0908988765"),
(12,"honda","brown","200000","0403903344"),
(14,"mitsubuishi","blue","150000","0304941112"),
(16,"hyunda","grey","700000","0203922111"),
(18,"porch","blue","800000","0102973331"),
(20,"rangerover","blue","900000","1008895554");

INSERT INTO
sala(Numer,bill_fastanumer,kaupandi_kt, solumadur_id)
VALUES
(5,2,"0102916765",1),
(10,4,"0105926765",2),
(15,6,"0103976745",3),
(20,8,"0102995731",4),
(25,10,"0908988765",5),
(30,12,"0102918619",6),
(35,14,"0102981100",7),
(40,16,"1202932222",8),
(45,18,"2502906755",9),
(50,20,"1708988188",10);