DROP TABLE IF EXISTS players;
CREATE TABLE players(
   id INTEGER PRIMARY KEY AUTOINCREMENT, 
   firstName TEXT,
   lastName TEXT,
   stableford INTEGER, --index in french
   sex INTEGER -- 0 female 1 male 
);

DROP TABLE IF EXISTS golf_courses;
CREATE TABLE golf_courses(
   name TEXT PRIMARY KEY, 
   slope INTEGER,
   sss INTEGER, 
   handicap_hole_1 INTEGER,
   handicap_hole_2 INTEGER,
   handicap_hole_3 INTEGER, 
   handicap_hole_4 INTEGER,
   handicap_hole_5 INTEGER,
   handicap_hole_6 INTEGER,
   handicap_hole_7 INTEGER,
   handicap_hole_8 INTEGER,
   handicap_hole_9 INTEGER,
   handicap_hole_10 INTEGER,
   handicap_hole_11 INTEGER,
   handicap_hole_12 INTEGER,
   handicap_hole_13 INTEGER,
   handicap_hole_14 INTEGER,
   handicap_hole_15 INTEGER,
   handicap_hole_16 INTEGER,
   handicap_hole_17 INTEGER,
   handicap_hole_18 INTEGER, 
   par_hole_1 INTEGER,
   par_hole_2 INTEGER,
   par_hole_3 INTEGER, 
   par_hole_4 INTEGER,
   par_hole_5 INTEGER,
   par_hole_6 INTEGER,
   par_hole_7 INTEGER,
   par_hole_8 INTEGER,
   par_hole_9 INTEGER,
   par_hole_10 INTEGER,
   par_hole_11 INTEGER,
   par_hole_12 INTEGER,
   par_hole_13 INTEGER,
   par_hole_14 INTEGER,
   par_hole_15 INTEGER,
   par_hole_16 INTEGER,
   par_hole_17 INTEGER,
   par_hole_18 INTEGER
);

DROP TABLE IF EXISTS games;
CREATE TABLE games(
	id INTEGER PRIMARY KEY AUTOINCREMENT, 
	id_player INTEGER 
	date_game TEXT, 
	golf TEXT, 	
	score_brut INTEGER, -- (total of ) for the game
	score_net INTEGER, --(total of )  for the game
	stableford INTEGER, -- (only for 18 holes)
	FOREIGN KEY(id_player) REFERENCES players(id),
	FOREIGN KEY(golf) REFERENCES golf(name)
);

DROP TABLE IF EXISTS hole;
CREATE TABLE holes(
   id INTEGER PRIMARY KEY AUTOINCREMENT, 
   id_player INTEGER, -- maybe useless can be find with game
   id_game TEXT, 
   hole_number INTEGER, -- in order to have handicap and par
   bunker INTEGER, -- 0 yes 1 no
   fairway INTEGER, -- 0 yes 1 no 2 green (green only for par 3)
   nb_puts INTEGER, 
   score_brute INTEGER, -- number of (coup joué ) for the hole
   score_net INTEGER, -- number of (coup au dessus du par) for the hole
   FOREIGN KEY(id_player) REFERENCES players(id)
   FOREIGN KEY(id_game) REFERENCES game(id)
);

