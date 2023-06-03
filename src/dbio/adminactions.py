from flask import flash, session
from beans.Question import Question
from beans.Student import Student
from beans.Subject import Subject

from dbio.dbutils import DbUtils
'''
Title: AdminActions
Description: This class is responsible to perfrom database operations.
e.g insert, update, retrive, authenticate user etc
@author Pshelar
@version 1.0
'''
class AdminActions(DbUtils):

    def insert(self, obj, tablename):
        '''Add entry for Student in database'''
        db = DbUtils.get_db()
        try:
            if type(obj) is Student :
                db.execute(
                        "INSERT INTO " + tablename + " (username, password, email) VALUES (?, ?, ?)",
                        (obj.getName(), obj.getPassword(), obj.getEmail())
                        )
            elif type(obj) is Subject :
                db.execute(
                        "INSERT INTO " + tablename + " (subjectname, maxmarks) VALUES (?, ?)",
                        (obj.getName(), obj.getMaxMarks())
                        )
            elif type(obj) is Question :
                db.execute(
                        "INSERT INTO " + tablename + " (subjectname, question, answer, marks, options) VALUES (?, ?, ?, ?, ?)",
                        (obj.getSubjectname(), obj.getQuestion(), obj.getAnswer(), obj.getMarks(), ','.join(obj.getOptions()))
                        )

            db.commit()
            print('Record inserted successfully in', tablename)
        except db.IntegrityError:
            error = f"DB OPERATION ERROR"
            flash(error)
            return False
        else:
            return True

    def update(self, fields, tablename):
        pass

    def delete(self, id, tablename):
        pass

    def filterQuestions(self, subjectname):
        #WHERE subjectname = ' + subjectname + ' ORDER BY RANDOM()
        output_list = []
        sql_query = 'SELECT * FROM questions WHERE subjectname=\"' + subjectname + '\" ORDER BY RANDOM() LIMIT 5'
        rows = DbUtils.get_db().execute(sql_query)
        for row in rows:
                output_list.append(Question(row[0], row[1], row[2], row[3], row[4], row[5].split(',')))
        return output_list

    def retrieveAll(self, tablename):
        rows = DbUtils.get_db().execute('SELECT * FROM ' + tablename)
        output_list = []
        if tablename == 'students':
            for row in rows:
                st = Student(row[0], row[1], row[2], row[3], [], row[4])
                output_list.append(st)
        elif tablename == 'subjects':
            for row in rows:
                output_list.append(Subject(row[0], row[1], row[2]))
        elif tablename == 'questions':
            for row in rows:
                output_list.append(Question(row[0], row[1], row[2], row[3], row[4], row[5].split(',')))
        return output_list

    def authenticate(self, username, password):
        '''Authenticate user by matching username  & password against which stored in db'''
        db = DbUtils.get_db()
        student = db.execute('SELECT * FROM students WHERE username = ? ', (username,)).fetchone()

        if student is not None:
            if student['password'] == password :
                session.clear()
                session['student_id'] = student['id']
                session['loggedin'] = True
                session['isadmin'] = student['isadmin']
                return True
            else :
                return False
        else :
            return False
