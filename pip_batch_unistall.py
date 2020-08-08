'''This script will detect all(except default ones) packages installed in a virtual environment(virtualenv) 
and uninstalls them at once, in windows.

* pre-requisites:

1) keep requirements.txt(can be empty) and in same folder as of code.
2) virtual enviroment should be created using virtualenv package, from within the directory where code.py resides.

NOTE: a handy log file 'log_pip_batch_uninstall' will be generated in same folder for debug purposes '''


import os
import logging
import unittest

logging.basicConfig(filename='log_pip_batch_uninstall.txt',format='%(asctime)s : %(filename)s : %(funcName)s : %(levelname)s :  %(lineno)d - %(message)s', level = logging.DEBUG)

class Testcase1(unittest.TestCase):
    def test_mycase(self):
        print('Testcase-1 started..!!')
        
        # take venv name
        venv_name = input('Enter name of venv\n')

        # store path to root dir 
        my_dir = os.getcwd()

        # cd to virtual env
        os.chdir('{}\\Scripts\\'.format(venv_name))

        # activate your venv
        os.system('activate')

        # come back to root dir
        os.chdir(my_dir)

        # prepare requirements.txt file
        print('checking requirements file..')
        os.system('pip freeze > requirements.txt')

        # begin uninstalling
        self.inputfile = open('requirements.txt')
        
        # view currently installed packages
        self.packages = self.inputfile.readlines()
        for i in self.packages:
                print(i)
        
        print('beginging uninstalling..')
        # begin uninstalling of venv packages
        for i in self.packages:
            print('\n\ncurrent Package under work: {}'.format(i))
            try:
                os.system('pip uninstall -y {}'.format(i))
            except Exception as e:
                logging.error('unexpected exception occured: {}'.format(e))

        self.inputfile.close()

unittest.main()
