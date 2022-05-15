DROP TABLE hopper_user;

CREATE TABLE hopper_user (
    user_id SERIAL NOT NULL PRIMARY KEY,
    username VARCHAR(40) NOT NULL,
    password VARCHAR(80) NOT NULL,
    role VARCHAR(10) DEFAULT 'user'
);

INSERT INTO hopper_user (username, password, role) VALUES ('admin', 'test-admin', 'admin');
INSERT INTO hopper_user (username, password) VALUES ('kuzichkin2001', 'test-user');
INSERT INTO hopper_user (username, password) VALUES ('nyanturion', 'test-anot-user');