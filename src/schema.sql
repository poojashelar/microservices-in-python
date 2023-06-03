CREATE TABLE IF NOT EXISTS students (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  email TEXT NOT NULL,
  isadmin INTEGER DEFAULT 0
);

INSERT INTO students (username, password, email, isadmin) values ("admin", "admin@123", "admin@mcqcenter.com", 1);

CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subjectname TEXT UNIQUE NOT NULL,
    maxmarks INTEGER
);

CREATE TABLE IF NOT EXISTS student_enrollment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    studentid INTEGER,
    subjectid INTEGER,
    score INTEGER,
    attempts INTEGER,
    FOREIGN KEY (studentid) REFERENCES students (id),
    FOREIGN KEY (subjectid) REFERENCES subjects (id)
);

CREATE TABLE IF NOT EXISTS  questions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  subjectname TEXT NOT NULL,
  question TEXT UNIQUE NOT NULL,
  answer TEXT NOT NULL,
  marks INTEGER NOT NULL,
  options TEXT NOT NULL,
  FOREIGN KEY (subjectname) REFERENCES subjects (subjectname)
);