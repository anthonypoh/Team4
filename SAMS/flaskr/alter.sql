

CREATE TABLE class (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  student_id INTEGER UNIQUE NOT NULL,
  class_id TEXT UNIQUE NOT NULL,
  batch INTEGER NOT NULL,
  attended INTEGER NOT NULL,
  late INTEGER,
  outside INTEGER,
  FOREIGN KEY (student_id) REFERENCES user (id)
);

insert into class (student_id, class_id, batch, attended, late, outside)
values (2, 'CE291', 3, 0, 0, 0);