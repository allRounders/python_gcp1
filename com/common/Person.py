import logging

logging.basicConfig(level='INFO')


class Person(object):

    def __int__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __person_info(self):
        logging.info("Private method, Person details=" + self.fname + " " + self.lname)

    def person_info(self):
        logging.info("Public method, Person details=" + self.fname + " " + self.lname)
        return self.fname + "-" + self.lname;