from common.Person import Person
import logging


logging.basicConfig(level='INFO')


class Student (Person):

    def __init__(self, fName, lName, schoolName):
        logging.info('Input values %r, %r %r' % (fName, lName, schoolName))
        super().__int__(fName, lName)
        self.schoolName = schoolName

    def get_info(self):
        #Access Public method
        super().person_info()

        #Access Private method
        super()._Person__person_info()

        logging.info("Student School Name=" + self.schoolName)

    def create_read_file(self):
        file = open("/Users/v.bq.kumar/vijay/python_projects/demofile2.txt", "w")
        file.write("Now the file has more content!\n")
        file.write(super().person_info())
        file.close()

        # open and read the file after the appending:
        file = open("/Users/v.bq.kumar/vijay/python_projects/demofile2.txt", "r")
        print(file.read())


student_obj = Student("jai", "raj", "dav")
student_obj.create_read_file()



# pandas,numpy,scikitlearn