'''
Title: Student
Description: Its bean class which used to hold the student detail.
@author Pshelar
@version 1.0
'''
class Student():
    def __init__(self, id, name, email, password, subjects, isadmin):
        '''Constructor to create object and initialize it with defaults'''
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.subject = subjects if len(subjects) > 0 else []
        self.isadmin = isadmin

    ''' Getter & Setters for instance variables'''
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email

    def setPassword(self, password):
        self.password = password
    
    def getPassword(self):
        return self.password

    def setSubjects(self, subjects):
        self.subject = subjects if len(subjects) > 0 else []

    def addSubject (self, Subject):
        self.subject.append(Subject)

    def getSubjects(self):
        return self.subject
    



    