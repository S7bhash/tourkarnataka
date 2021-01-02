create table places(
  name varchar(64) primary key,
  latitude varchar(15),
  longitude varchar(15),
  climate varchar(16),
  language varchar(20),
  description text

);
create table reviews(
  name varchar(64) references places,
  username varchar(64),
  rating integer,
  comments text,
  dates datetime
);
