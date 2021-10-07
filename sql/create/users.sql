CREATE SEQUENCE user_id_sequence
  start 1000
  increment 1;

DROP TABLE users;
CREATE TABLE users(
    login varchar(25) NOT NULL UNIQUE ,
    email varchar(50) NOT NULL UNIQUE ,
    first_name varchar(50) ,
    last_name varchar(50) ,
    user_id INT primary key DEFAULT nextval('user_id_sequence'),
    CONSTRAINT login_minimum_size CHECK ( length(login) > 2 ),
    CONSTRAINT minimum_size CHECK ( length(email) > 6 and length(first_name) > 1 and length(last_name) > 1)
);