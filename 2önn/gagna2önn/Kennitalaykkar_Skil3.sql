CREATE DATABASE 0301865919_Kennitalaykkar_Skil3;
USE 0301865919_Kennitalaykkar_Skil3;
CREATE TABLE Skuld_lanabok
(
Nafn VARCHAR(40) NOT NULL,
Kennitala VARCHAR(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
Netfang VARCHAR(50) NOT NULL ,
Heimilisfang VARCHAR(40) NULL,
Póstnúmer INT NULL,
Lán DECIMAL(7,2) NULL,
Skuld INT NULL
);

INSERT INTO skuld_lanabok
	(Nafn, Kennitala, Netfang, Heimilisfang, Póstnúmer, Lán, Skuld)
VALUES
	("livinus felix","0301865919","robertsonekat@yahoo.com","flúðaseli 76","109 reykjavik", "800000","0"),
    ("viljamur ferguson","0708907912","viljamurferguson@yahoo.com","vatnsgata 20","108 garðabær", "950000","0"),
    ("olafur  guðmunson","0202949591","olafurguðmunson@yahoo.com","skulagotu 36 ","101 reykjavik", "900000","0"),
    ("reuben lopez","0806955718","reubenlopez@yahoo.com","leisgata 37","10 reykjavik", "777000","0"),
    ("petur alexon","0909932219","peturalexon@yahoo.com","hanannes 13","102 reykjavik", "910000","0"),
    ("omar smari","0303986913","omarsmari@yahoo.com","flúðaseli 22","109 reykjavik", "510000","0"),
    ("svavar einarson","07059432829","svavareinarson@yahoo.com","jáðaseli 61","109 reykjavik", "690000","0"),
    ("jón elifson","05069563329","jónelifson@yahoo.com","jáðaseli 70","109 reykjavik", "900000","0"),
    ("ilmil gunnarson","0301865919","ilmilgunnarson@yahoo.com","flúðaseli 48","109 reykjavik", "931000","0"),
    ("gustaf andriasson","0406875729","gustafandriasson@yahoo.com","katrinatún 24","101 reykjavik", "990000","0"),
    ("safi thorasson","1104943115","safithorasson@yahoo.com","bortúnagata 82 ","101 reykjavik", "898000","0"),
    ("david thomason","2102895528","david thomasont@yahoo.com","skulagotu 59","101 reykjavik", "800000","0");
    

CREATE TABLE poststod
(
Póstnúmer INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
Sveitarfélag VARCHAR(40) NOT NULL
);

-- INSERT INTO Poststod();

select * from Skuld_Lanabok;
