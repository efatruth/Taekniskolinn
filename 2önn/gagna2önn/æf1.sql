use 0301865919_taekniskolinn;
CREATE TABLE Highscores
(
	player CHAR(3),
	score INTEGER
);

INSERT INTO HighScores
	(player, score)
VALUES
	("EET", 12000),
	("HKS", 11000),
	("GUT", 10000),
	("HAJ", 9000),
	("JOH", 8000),
	("JTH", 7000),
	("PHS", 6000);
    drop table HighScores;