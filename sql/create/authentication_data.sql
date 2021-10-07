DROP TABLE authentication_data;
CREATE TABLE authentication_data(
    password_hash TEXT NOT NULL ,
    user_id INT NOT NULL UNIQUE ,
    CONSTRAINT unique_user_id FOREIGN KEY(user_id) REFERENCES users(user_id)
);

