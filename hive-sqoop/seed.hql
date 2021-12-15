INSERT INTO TABLE work_dataeng.generation_hellen VALUES
 (1,"1996-02-27"),
 (2,"1999-11-21"),
 (3,"2002-11-21"),
 (4,"2006-09-28"),
 (5,"2010-09-18"),
 (6,"2010-12-13"),
 (7,"2016-11-18");
 
SELECT * FROM work_dataeng.generation_hellen;
 
CREATE EXTERNAL TABLE pokemon_hellen_ext (
    idnum int,
	name string, 
	hp int,
	speed int,
	attack int,
	special_attack int,
	defense int,
	special_defense int,
	generation int
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
TBLPROPERTIES ('skip.header.line.count'='1');

LOAD DATA INPATH '/user/2rp-hellen/pokemon.csv' INTO TABLE pokemon_hellen_ext

INSERT INTO TABLE work_dataeng.pokemon_hellen SELECT * FROM pokemon_hellen_ext

SELECT * FROM work_dataeng.pokemon_hellen LIMIT 100;
