USE mydb;
truncate table keyword_has_artwork;
delete from artwork;
delete from artist;
delete from keyword;

ALTER TABLE keyword_has_artwork AUTO_INCREMENT = 1;
ALTER TABLE artwork AUTO_INCREMENT = 1;
ALTER TABLE artist AUTO_INCREMENT = 1;
ALTER TABLE keyword AUTO_INCREMENT = 1;

INSERT INTO artist (`name`, `middle_name`, `artist_last_name`, `year_of_birth`,`year_of_death`,`country`,`local`) VALUES ('Vincent', '','van Gogh','1853','1890','France','n');
INSERT INTO artist (`name`,
`middle_name`,
`artist_last_name`,
`year_of_birth`,
`year_of_death`,
`country`,
`local`) VALUES ('Rembrandt', 'Harmenszoon','van Rijn','1606','1669','Netherlands','n');

INSERT INTO artist (`name`,
`middle_name`,
`artist_last_name`,
`year_of_birth`,
`year_of_death`,
`country`,
`local`) VALUES ('Leonardo', '','da Vinci','1452','1519','Italy','n');

INSERT INTO artist (`name`,
`middle_name`,
`artist_last_name`,
`year_of_birth`,
`year_of_death`,
`country`,
`local`) VALUES ('Venture', 'Lonzo','Coy',1965,0,'United States','y');

INSERT INTO artist (`name`,
`middle_name`,
`artist_last_name`,
`year_of_birth`,
`year_of_death`,
`country`,
`local`) VALUES ('Deborah', '','Gill',1970,0,'United States','y');

INSERT INTO artist (`name`,
`middle_name`,
`artist_last_name`,
`year_of_birth`,
`year_of_death`,
`country`,
`local`) VALUES ('Claude', '','Monet',1840,1926,'France','n');

INSERT INTO artist (`name`,
`middle_name`,
`artist_last_name`,
`year_of_birth`,
`year_of_death`,
`country`,
`local`) VALUES ('Pablo', '','Picasso',1904,1973,'Spain','n');

INSERT INTO artist (`name`,
`middle_name`,
`artist_last_name`,
`year_of_birth`,
`year_of_death`,
`country`,
`local`) VALUES ('Michelangelo', 'di Lodovico','Simoni',1475,1564,'Italy','n');

INSERT INTO keyword (keyword) VALUES('flowers');
INSERT INTO keyword (keyword) VALUES('blue');
INSERT INTO keyword (keyword) VALUES('landscape');
INSERT INTO keyword (keyword) VALUES('girl');
INSERT INTO keyword (keyword) VALUES('people');
INSERT INTO keyword (keyword) VALUES('battle');
INSERT INTO keyword (keyword) VALUES('boat');
INSERT INTO keyword (keyword) VALUES('water');
INSERT INTO keyword (keyword) VALUES('Christ');
INSERT INTO keyword (keyword) VALUES('food');
INSERT INTO keyword (keyword) VALUES('baby');

INSERT INTO artwork (artist_id, title, year, period, type, file)
SELECT (SELECT artist_id FROM artist WHERE name = 'Vincent' and middle_name = '' and artist_last_name = 'van Gogh'),
		'Irises', '1889', 'Impressionism', 'Oil', 'irises.jpg' ;
        
INSERT INTO artwork (artist_id, title, year, period, type, file)
SELECT (SELECT artist_id FROM artist WHERE name = 'Vincent' and middle_name = '' and artist_last_name = 'van Gogh'), 
	'The Starry Night', '1889', 'Post-Impressionism', 'Oil', 'starrynight.jpg' ;

INSERT INTO artwork (artist_id, title, year, period, type, file)
SELECT (SELECT artist_id FROM artist WHERE name = 'Vincent' and middle_name = '' and artist_last_name = 'van Gogh'), 
	'Sunflowers', '1888', 'Post-impressionism', 'Oil', 'sunflowers.jpg' ;
   
INSERT INTO artwork (artist_id, title, year, period, type, file)
SELECT (SELECT artist_id FROM artist WHERE name = 'Rembrandt' and middle_name = 'Harmenszoon' and artist_last_name = 'van Rijn'), '', '', '', '', '' ;
INSERT INTO artwork (artist_id, title, year, period, type, file)
SELECT (SELECT artist_id FROM artist WHERE name = 'Rembrandt' and middle_name = 'Harmenszoon' and artist_last_name = 'van Rijn'), 'Night Watch', '1642', 'Baroque', 'Oil', 'nightwatch.jpg'; 
INSERT INTO artwork (artist_id, title, year, period, type, file)
SELECT (SELECT artist_id FROM artist WHERE name = 'Rembrandt' and middle_name = 'Harmenszoon' and artist_last_name = 'van Rijn'), 'Storm on the Sea of Galilee', '1633', 'Dutch Golden Age', 'Oil', 'stormgalilee.jpg';

INSERT INTO artwork (artist_id, title, year, period, type, file)
SELECT (SELECT artist_id FROM artist WHERE name = 'Leonardo' and middle_name = '' and artist_last_name = 'da Vinci'), '', '', '', '', '' ;
INSERT INTO artwork (artist_id, title, year, period, type, file)
SELECT (SELECT artist_id FROM artist WHERE name = 'Leonardo' and middle_name = '' and artist_last_name = 'da Vinci'), 'Head of a Woman', '1508', 'High Renaissance', 'Oil', 'headwoman.jpg' ;
INSERT INTO artwork (artist_id, title, year, period, type, file)
SELECT (SELECT artist_id FROM artist WHERE name = 'Leonardo' and middle_name = '' and artist_last_name = 'da Vinci'), 'Last Supper', '1498', 'Renaissance', 'Tempra ', 'lastsupper.jpg' ;
INSERT INTO artwork (artist_id, title, year, period, type, file)
SELECT (SELECT artist_id FROM artist WHERE name = 'Leonardo' and middle_name = '' and artist_last_name = 'da Vinci'), 'Mona Lisa', '1517', 'Renaissance', 'Oil', 'monalisa.jpg' ;

INSERT INTO artwork (artist_id, title, year, period, type, file)
SELECT (SELECT artist_id FROM artist WHERE name = 'Venture' and middle_name = 'Lonzo' and artist_last_name = 'Coy'), 'Hillside Stream', '2005', 'Modern', 'Oil', 'hillsidestream.jpg' ;
INSERT INTO artwork (artist_id, title, year, period, type, file)
SELECT (SELECT artist_id FROM artist WHERE name = 'Venture' and middle_name = 'Lonzo' and artist_last_name = 'Coy'), 'Old Barn', '1992', 'Modern', 'Oil', 'oldbarn.jpg' ;

INSERT INTO artwork (artist_id, title, year, period, type, file)
SELECT (SELECT artist_id FROM artist WHERE name = 'Deborah' and middle_name = '' and artist_last_name = 'Gill'), 'Beach Baby', '1999', 'Modern', 'Watercolor', 'beachbaby.jpg' ;

INSERT INTO artwork (artist_id, title, year, period, type, file)
SELECT (SELECT artist_id FROM artist WHERE name = 'Claude' and middle_name = '' and artist_last_name = 'Monet'), 'Women in the Garden', '1866', 'Impressionism', 'Oil', 'womengarden.jpg' ;

INSERT INTO artwork (artist_id, title, year, period, type, file)
SELECT (SELECT artist_id FROM artist WHERE name = 'Pablo' and middle_name = '' and artist_last_name = 'Picasso'), 'Old Guitarist', '1904', 'Modern', 'Oil', 'guitarist.jpg' ;

Insert into keyword_has_artwork (keyword_id, artwork_id)
SELECT (SELECT keyword_id FROM keyword WHERE keyword = 'flowers'), (SELECT artwork_id FROM artwork WHERE title = 'Irises') ;

Insert into keyword_has_artwork (keyword_id, artwork_id)
SELECT (SELECT keyword_id FROM keyword WHERE keyword = 'blue'), (SELECT artwork_id FROM artwork WHERE title = 'The Starry Night') ;
Insert into keyword_has_artwork (keyword_id, artwork_id)
SELECT (SELECT keyword_id FROM keyword WHERE keyword = 'landscape'), (SELECT artwork_id FROM artwork WHERE title = 'The Starry Night') ;
Insert into keyword_has_artwork (keyword_id, artwork_id)
SELECT (SELECT keyword_id FROM keyword WHERE keyword = 'flowers'), (SELECT artwork_id FROM artwork WHERE title = 'Sunflowers') ;

Insert into keyword_has_artwork (keyword_id, artwork_id)
SELECT (SELECT keyword_id FROM keyword WHERE keyword = 'girl'), (SELECT artwork_id FROM artwork WHERE title = 'Night Watch') ;
Insert into keyword_has_artwork (keyword_id, artwork_id)
SELECT (SELECT keyword_id FROM keyword WHERE keyword = 'people'), (SELECT artwork_id FROM artwork WHERE title = 'Night Watch') ;
Insert into keyword_has_artwork (keyword_id, artwork_id)
SELECT (SELECT keyword_id FROM keyword WHERE keyword = 'battle'), (SELECT artwork_id FROM artwork WHERE title = 'Night Watch') ;

Insert into keyword_has_artwork (keyword_id, artwork_id)
SELECT (SELECT keyword_id FROM keyword WHERE keyword = 'boat'), (SELECT artwork_id FROM artwork WHERE title = 'Storm on the Sea of Galilee') ;
Insert into keyword_has_artwork (keyword_id, artwork_id)
SELECT (SELECT keyword_id FROM keyword WHERE keyword = 'water'), (SELECT artwork_id FROM artwork WHERE title = 'Storm on the Sea of Galilee') ;
Insert into keyword_has_artwork (keyword_id, artwork_id)
SELECT (SELECT keyword_id FROM keyword WHERE keyword = 'people'), (SELECT artwork_id FROM artwork WHERE title = 'Storm on the Sea of Galilee') ;
Insert into keyword_has_artwork (keyword_id, artwork_id)
SELECT (SELECT keyword_id FROM keyword WHERE keyword = 'Christ'), (SELECT artwork_id FROM artwork WHERE title = 'Storm on the Sea of Galilee') ;

Insert into keyword_has_artwork (keyword_id, artwork_id)
SELECT (SELECT keyword_id FROM keyword WHERE keyword = 'girl'), (SELECT artwork_id FROM artwork WHERE title = 'Head of a Woman') ;
Insert into keyword_has_artwork (keyword_id, artwork_id)
SELECT (SELECT keyword_id FROM keyword WHERE keyword = 'people'), (SELECT artwork_id FROM artwork WHERE title = 'Head of a Woman') ;

Insert into keyword_has_artwork (keyword_id, artwork_id)
SELECT (SELECT keyword_id FROM keyword WHERE keyword = 'food'), (SELECT artwork_id FROM artwork WHERE title = 'Last Supper') ;
Insert into keyword_has_artwork (keyword_id, artwork_id)
SELECT (SELECT keyword_id FROM keyword WHERE keyword = 'people'), (SELECT artwork_id FROM artwork WHERE title = 'Last Supper') ;
Insert into keyword_has_artwork (keyword_id, artwork_id)
SELECT (SELECT keyword_id FROM keyword WHERE keyword = 'Christ'), (SELECT artwork_id FROM artwork WHERE title = 'Last Supper') ;

Insert into keyword_has_artwork (keyword_id, artwork_id)
SELECT (SELECT keyword_id FROM keyword WHERE keyword = 'girl'), (SELECT artwork_id FROM artwork WHERE title = 'Mona Lisa') ;
Insert into keyword_has_artwork (keyword_id, artwork_id)
SELECT (SELECT keyword_id FROM keyword WHERE keyword = 'people'), (SELECT artwork_id FROM artwork WHERE title = 'Mona Lisa') ;

Insert into keyword_has_artwork (keyword_id, artwork_id)
SELECT (SELECT keyword_id FROM keyword WHERE keyword = 'water'), (SELECT artwork_id FROM artwork WHERE title = 'Hillside Stream') ;
Insert into keyword_has_artwork (keyword_id, artwork_id)
SELECT (SELECT keyword_id FROM keyword WHERE keyword = 'landscape'), (SELECT artwork_id FROM artwork WHERE title = 'Hillside Stream') ;

Insert into keyword_has_artwork (keyword_id, artwork_id)
SELECT (SELECT keyword_id FROM keyword WHERE keyword = 'landscape'), (SELECT artwork_id FROM artwork WHERE title = 'Old Barn') ;

Insert into keyword_has_artwork (keyword_id, artwork_id)
SELECT (SELECT keyword_id FROM keyword WHERE keyword = 'water'), (SELECT artwork_id FROM artwork WHERE title = 'Beach Baby') ;
Insert into keyword_has_artwork (keyword_id, artwork_id)
SELECT (SELECT keyword_id FROM keyword WHERE keyword = 'people'), (SELECT artwork_id FROM artwork WHERE title = 'Beach Baby') ;
Insert into keyword_has_artwork (keyword_id, artwork_id)
SELECT (SELECT keyword_id FROM keyword WHERE keyword = 'baby'), (SELECT artwork_id FROM artwork WHERE title = 'Beach Baby') ;

Insert into keyword_has_artwork (keyword_id, artwork_id)
SELECT (SELECT keyword_id FROM keyword WHERE keyword = 'landscape'), (SELECT artwork_id FROM artwork WHERE title = 'Women in the Garden') ;
Insert into keyword_has_artwork (keyword_id, artwork_id)
SELECT (SELECT keyword_id FROM keyword WHERE keyword = 'people'), (SELECT artwork_id FROM artwork WHERE title = 'Women in the Garden') ;
Insert into keyword_has_artwork (keyword_id, artwork_id)
SELECT (SELECT keyword_id FROM keyword WHERE keyword = 'flowers'), (SELECT artwork_id FROM artwork WHERE title = 'Women in the Garden') ;

Insert into keyword_has_artwork (keyword_id, artwork_id)
SELECT (SELECT keyword_id FROM keyword WHERE keyword = 'blue'), (SELECT artwork_id FROM artwork WHERE title = 'Old Guitarist') ;
Insert into keyword_has_artwork (keyword_id, artwork_id)
SELECT (SELECT keyword_id FROM keyword WHERE keyword = 'people'), (SELECT artwork_id FROM artwork WHERE title = 'Old Guitarist') ;



-- select * from artwork
-- select * from artist
-- select * from keyword
-- select * from keyword_has_artwork





