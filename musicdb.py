# -*- coding: utf-8 -*-
"""


@author: Wurood Mandawi
Samantha Hughson
Ziva Wernick
Lu Liu
"""
import sqlite3 as db

class MusicDB:
    def __init__( self):
      self.conn = db.connect("CSDepartmentDatabase.db")
      
    def __del__(self):
      self.conn.close()
      #query for viewing student
    def viewStudent(self, name):
        cur = self.conn.cursor()
        params = (name,)
        cur.execute("Select * from StudentDirectory as S where S.clarkID = ?", params)
        result = cur.fetchall()
        return(result)
    #query for deleting student
    def deleteStudent(self, studentID):
        cur = self.conn.cursor()
        params = (studentID)
        print("You deleted student " + studentID)
        cur.execute("Update CourseListings SET TAID = NULL WHERE TAID = ?", params)
        cur.execute("Delete From StudentDirectory WHERE clarkID = ?", params)
        cur.execute("Delete From ClassRoster WHERE studentID = ?", params)
        self.conn.commit()
    
    #query for uodating student's advisor
    def updateStudentAdvisor(self, name, advisorID):
        cur = self.conn.cursor()
        params = (advisorID, name)
        print("You updated " + name + "'s advisor to: " + advisorID)
        cur.execute("UPDATE StudentDirectory SET advisorID = ? WHERE clarkID = ?", params)
        self.conn.commit()
    
    #query for viewing professor
    def viewProf(self):
        cur = self.conn.cursor()
        cur.execute("Select * from ProfessorDirectory")
        return(cur)
    
    #query for updating professor's room number
    def updateProfOfficeNum(self, profID, officenum):
        cur = self.conn.cursor()
        params = (officenum, profID)
        print("You updated " + profID + "'s office number to: " + officenum)
        cur.execute("UPDATE ProfessorDirectory SET OfficeNumber = ? WHERE clarkID = ?", params)
        self.conn.commit()
     
    #query for updating course    
    def updateCourse(self, courseID, profID):
        cur = self.conn.cursor()
        params = (profID, courseID)
        print("You updated " + profID + "'s course to: " + courseID)
        cur.execute("Update CourseListings SET ProfessorID = ? WHERE courseID = ?", params)
        self.conn.commit()
    
    #query for viewing course
    def viewCourse(self, courseID):
        cur = self.conn.cursor()
        params = (courseID)
        cur.execute("SELECT * FROM CourseListings WHERE courseID = ?", params)
        result = cur.fetchall()
        return(result)
      
    #query for viewing lab schedule    
    def viewLabSchedule(self, courseID, semester, year):
        cur = self.conn.cursor()
        params = (courseID, semester, year)
        cur.execute("SELECT C.courseName, L.RoomNum, L.day, L.time FROM LabSchedule as L, CourseListings as C	WHERE L.courseID = ? and L.semester = ? and L.year = ? and C.courseID = L.courseID", params)
        result = cur.fetchall()
        return(result)
     
    #query for updating lab schedule    
    def updateLabSchedule(self, newday, newtime, classID, semester, year, day, time, roomNum):
        cur = self.conn.cursor()
        params = (newday, newtime, classID, semester, year, day, time, roomNum)
        print("You updated " + classID + "'s day and time to: " + newday + newtime)
        cur.execute("Update LabSchedule SET day = ?, time = ? WHERE courseID = ? and semester = ? and year = ? and day = ? and time = ? and RoomNum = ?", params)
        self.conn.commit()
      
       
    def selectIf(self, semester, year, day, time, roomNum):
        cur = self.conn.cursor()
        params = (semester, year, day, time, roomNum)
        cur.execute("SELECT COUNT(C.courseName) FROM LabSchedule WHERE semester = ? and year = ? and day = ? and time = ? and roomNum = ?", params)
        result = cur.fetchall()
        return(result)
    
    #query for viewing student details    
    def viewStudentDetails(self, courseID):
        cur = self.conn.cursor()
        params = (courseID)
        cur.execute("SELECT * FROM studentDirectory WHERE clarkID IN (Select studentID from ClassRoster where courseID = ?) Group By clarkID", params)
        result = cur.fetchall()
        return(result)
    
    #query for updating clicker
    def updateClicker(self, clickerID, clarkID):
        cur = self.conn.cursor()
        params = (clickerID, clarkID)
        print("You updated " + clarkID + "'s clickerID to: " + clickerID)
        cur.execute("UPDATE StudentDirectory SET clickerID = ? WHERE clarkID = ?", params)
        self.conn.commit()
    
    #query for updating grade
    def addGrade(self, grade, clarkID, courseID):
        cur = self.conn.cursor()
        params = (grade, clarkID, courseID)
        print("You updated " + clarkID + "'s grade to: " + grade)
        cur.execute("UPDATE ClassRoster SET grade = ? WHERE studentID = ?and courseID = ?", params)
        self.conn.commit()
        
    #query for viewing professors by last name    
    def viewAllProf(self, lName):
        cur = self.conn.cursor()
        params = (lName)
        cur.execute("Select * From ProfessorDirectory Where lastName = ?", params)
        result = cur.fetchall()
        return(result)
      
    #query for updating lab's room number    
    def updateRoomLab(self, newRoom, courseID, semester, year, day):
        cur = self.conn.cursor()
        params = (newRoom, courseID, semester, year, day)
        print("You updated " + courseID + "'s room to: " + newRoom)
        cur.execute("Update LabSchedule SET RoomNum = ? WHERE courseID = ? and semester = ? and year = ? and day = ? and type = 'TA Lab'", params)
        self.conn.commit()
     
    #query for deleting professor    
    def deleteProf(self, profID):
        cur = self.conn.cursor()
        params = (profID)
        print("You deleted professor " + profID)
        cur.execute("UPDATE StudentDirectory SET AdvisorID = 1 WHERE advisorID = ?", params)
        cur.execute("Delete From CourseListings WHERE ProfessorID = ?", params)
        cur.execute("Delete From ProfessorDirectory WHERE clarkID = ?", params)
        self.conn.commit()
     
    #query for deleting course    
    def deleteCourse(self, courseID):
        cur = self.conn.cursor()
        params = (courseID)
        print("You deleted course " + courseID)
        cur.execute("DELETE From CourseListings WHERE courseID = ?", params)
        cur.execute("DELETE From LabSchedule WHERE courseID = ?", params)
        cur.execute("DELETE From ClassRoster WHERE courseID = ?", params)
        self.conn.commit()
    
    

        
      
        
