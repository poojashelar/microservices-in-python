import pandas as pd
from dbio.adminactions import AdminActions
from beans.Question import Question
'''
Title: LoadQuestions
Description: This class is responsible to read excel file, convert data to dataframe and load it in to db.
@author Pshelar
@version 1.0
'''
class LoadQuestions():
        
    def readExcel(self, filename):
        '''Read excel file and convert to Pandas dataframe'''
        dataFrame = pd.read_excel(filename)
        return dataFrame

    def __read_dataframe_list(self, df:pd.DataFrame)->list:
        '''Private method to convert excel data in to List(Question)'''
        return list(map(lambda x: Question(id=1,subjectname=x[0], question=x[1], answer=x[2], marks=x[3], options=x[4].split(',')),df.values.tolist()))

    def dumpQuestionsInDb(self, df:pd.DataFrame):
        ''' Read list and insert data in db and return count of rows inserted'''
        questionList = self.__read_dataframe_list(df)
        count = 0
        admin_actions = AdminActions()
        for que in questionList:
            #insert data in db
            if admin_actions.insert(que, 'questions') :
                count += 1
        return count

            

