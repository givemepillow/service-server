CREATE TABLE authentication_data(
    password_hash TEXT NOT NULL ,
    login varchar(25) NOT NULL UNIQUE ,
    email varchar(50) NOT NULL UNIQUE ,
    user_id SERIAL PRIMARY KEY
);