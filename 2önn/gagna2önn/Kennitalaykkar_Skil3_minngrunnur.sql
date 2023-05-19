CREATE DATABASE 0301865919_Kennitalaykkar_Skil3_minngrunnur;
drop table Upplysingar_Starfsheiti_Hopa;

CREATE TABLE Upplysingar_Starfsheiti_Hopa
(
nafn VARCHAR(100),
kennitala CHAR(11),
netfang VARCHAR(50),
heimilisfang varchar(100),
póstnúmer INT,
sími varchar(100) NOT NULL
);


INSERT INTO Upplysingar_Starfsheiti_Hopa
	(nafn, kennitala, netfang, heimilisfang, póstnúmer, sími )
VALUES
	("svavar einarson","07059432829","svavareinarson@yahoo.com","jáðaseli 61",109, "8811234"),
    ("jón elifson","05069563329","jónelifson@yahoo.com","jáðaseli 70",109, "7733122"),
    ("ilmil gunnarson","0301865919","ilmilgunnarson@yahoo.com","flúðaseli 48",109, "7700654"),
    ("gustaf andriasson","0406875729","gustafandriasson@yahoo.com","katrinatún 24",109, "8899171"),
    ("safi thorasson","1104943115","safithorasson@yahoo.com","bortúnagata 82 ",101, "8809771"),
    ("david thomason","2102895528","david thomasont@yahoo.com","skulagotu 59",101, "8819992"),
    ("olafur  guðmunson","0202949591","olafurguðmunson@yahoo.com","skulagotu 36 ",101, "7790832"),
    ("reuben lopez","0806955718","reubenlopez@yahoo.com","leisgata 37",101, "7707665"),
    ("petur alexon","0909932219","peturalexon@yahoo.com","hanannes 13",102, "8677710"),
    ("omar smari","0303986913", "omarsmari@yahoo.com", "flúðaseli 22",109, "7788415");

select * from Upplysingar_Starfsheiti_Hopa;