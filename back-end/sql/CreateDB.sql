CREATE TABLE Hopper_WorkSpace (
    workspace_id SERIAL,
    fixed_jumps VARCHAR(200),
    random_jumps VARCHAR(200),
    code_input TEXT
);

CREATE TABLE Hopper_Session (
    session_id SERIAL NOT NULL PRIMARY KEY,
    name VARCHAR(200) NOT NULL DEFAULT '',
    kuz_place INTEGER NOT NULL DEFAULT 0,
    code TEXT DEFAULT '',
    creation_date TIME DEFAULT now()
);

CREATE TABLE Hopper_User (
    user_id SERIAL NOT NULL PRIMARY KEY,
    username VARCHAR(30) NOT NULL,
    password VARCHAR(80) NOT NULL,
    role VARCHAR(80) NOT NULL DEFAULT 'user',
);