import os
from flask import Blueprint, app, current_app, flash, redirect, render_template, request, session, url_for
from beans.Question import Question
from dbio.LoadQuestions import LoadQuestions
from beans.Subject import Subject
from beans.Student import Student
from dbio.adminactions import AdminActions

# Create blueprint for authentication , url_prefix='/auth'
bp = Blueprint('McqExamCenterServices', __name__)

# Get object of AdminActions
admin_actions = AdminActions()
'''
Title: Services
Description: This class is responsible for create bluprint and routes to application.
@author Pshelar
@version 1.0
'''
class Services():
    questionList = []

    @bp.route("/login", methods = ["GET", "POST"])
    def login():
        ''' Perform login functionality.'''
        if request.method == 'POST':
            username  = request.form.get('uname')
            password  = request.form.get('psw')
            if admin_actions.authenticate(username, password):
                if session['isadmin'] is not None and session['isadmin'] > 0 :
                    return redirect(url_for('McqExamCenterServices.adminPage'))
                return redirect (url_for('McqExamCenterServices.studentPage'))
            else:
                error = 'Incorrect username/password.'
                flash(error)

        return render_template('login.html')

    @bp.route("/signup", methods = ["GET", "POST"])
    def signup():
        '''Perform signup functionality.'''
        if request.method == 'POST' and 'uname' in request.form and 'psw' in request.form and 'email' in request.form :
            student_obj = Student(0, request.form.get('uname'), request.form.get('email'), request.form.get('psw'), [], 0)
            if admin_actions.insert(student_obj, 'students') :
                return redirect(url_for("McqExamCenterServices.login"))
            else:
                error = 'Internal Server Error.'
                flash(error)
        return render_template('signup.html')

    @bp.route("/logout")
    def logout():
        ''' Clear session when logout by user.'''
        session.pop('loggedin', None)
        session.pop('student_id', None)
        session.pop('isadmin', None)
        return redirect(url_for('McqExamCenterServices.login'))

    @bp.route("/student", methods = ["GET", "POST"])
    def studentPage():
        ''' Student page to see details related to subject and enrollment.'''
        if request.method == 'POST' and 'subjects' in request.form:
            subject = request.form.get('subjects')
            Services.questionList = admin_actions.filterQuestions(subject)
            if len(Services.questionList) > 0 :
                return render_template('startExam.html', questionLst=Services.questionList )

        sublist = admin_actions.retrieveAll('subjects')
        return render_template('student.html', sublist=sublist)

    @bp.route("/score", methods = ["GET", "POST"])
    def getscore():
        score  = 0
        outof = 0
        if request.method == 'POST':
            for que in Services.questionList:
                choosen = request.form.get(str(que.id))
                outof += que.marks
                if choosen is not None and choosen == que.answer :
                    score += que.marks
        if score > 0 :
            scorepercent = (score / outof) * 100
        return render_template('score.html', score=round(scorepercent, 2))

    @bp.route("/admin", methods = ["GET", "POST"])
    def adminPage():
        ''' Admin page to perform admin operations.'''
        obj_list = []
        obj_name = ''
        if request.form.get('getallstudents') == 'List all registered Students' :
            obj_list = admin_actions.retrieveAll('students')
            obj_name = 'students'
        elif request.form.get('getsubjects') == 'List all Subjects' :
            obj_list = admin_actions.retrieveAll('subjects')
            obj_name = 'subjects'
        elif request.form.get('getquestions') == 'List all Questions' :
            obj_list = admin_actions.retrieveAll('questions')
            obj_name = 'questions'
        elif request.form.get('addsubject') == 'Add New Subject' :
            return render_template('addsubject.html')
        elif request.form.get('loadquestions') == 'Add Questions' :
            return render_template('loadquestions.html')
        return render_template('admin.html', objlist=obj_list, obj=obj_name)

    @bp.route("/addsubject", methods = ["GET", "POST"])
    def addsubject():
        if request.method == 'POST' and 'name' in request.form and 'marks' in request.form :
            sub = Subject (1, request.form.get('name'), request.form.get('marks'))
            if admin_actions.insert(sub, 'subjects') :
                return redirect(url_for('McqExamCenterServices.adminPage'))
            else:
                flash('Internal Server Error')
        return render_template('addsubject.html')

    @bp.route("/loadquestions", methods = ["GET", "POST"])
    def loadquestions():
        if request.method == 'POST':
            file = request.files['xlsxfile']
            if file.filename != '':
                filePath = os.path.join(current_app.config ['TEMPFILE'], file.filename)
                file.save(filePath)

                load_ques_obj = LoadQuestions()
                count = load_ques_obj.dumpQuestionsInDb(load_ques_obj.readExcel(filePath))
                if count > 0:
                    flash(str(count) + 'questions loaded in db')
                    return redirect(url_for('McqExamCenterServices.adminPage'))
            else :
                flash('Please choose file')

        return render_template('loadquestions.html')
