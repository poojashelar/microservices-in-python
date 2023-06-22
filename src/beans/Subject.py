
'''
Title: Subject
Description: Its bean class which used to hold the subject detail.
@author Pshelar
@version 1.0
'''
class Subject():
    def __init__(self, id, subjectname, maxmarks):
        self.id = id
        self.name = subjectname
        self.maxmarks = maxmarks
    
    ''' Getter & Setters for Subject class variables'''
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def setMaxMarks(self, marks):
        self.maxmarks = marks

    def getMaxMarks(self):
        return self.maxmarks
