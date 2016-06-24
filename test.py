# simple test class to be run by Travis build

import datetime

class TravisTest:

    def __init__(self):
        pass

    def echofile(self, filename):
         
        print datetime.datetime.now()
        f = open(filename, 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()

if __name__ == "__main__":
    t = TravisTest()
    t.echofile('testdata.txt')
