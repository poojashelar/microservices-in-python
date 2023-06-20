'''
Title: Question
Description: Its bean class which used to hold the question details.
@author Pshelar
@version 1.0
'''
class Question():
    def __init__(self, id, subjectname, question, answer, marks, options = []):
        self.id = id
        self.subjectname = subjectname
        self.question = question
        self.answer = answer
        self.marks = marks
        self.options = options

    # Getters for instance fiels
    def getId(self):
        return self.id
    
    def getSubjectname(self):
        return self.subjectname
    
    def getQuestion(self):
        return self.question
    
    def getAnswer(self):
        return self.answer
    
    def getMarks(self):
        return self.marks
    
    def getOptions(self):
        return self.options
    
