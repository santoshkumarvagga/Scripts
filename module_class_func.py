'''This Script helps to retrive the module name, class name and function name'''

import re
import logging
import unittest

logging.basicConfig(filename='log_module_class_function_names.txt', format='%(asctime)s : %(filename)s : %(funcName)s : %(levelname)s :  %(lineno)d - %(message)s', level = logging.DEBUG)

class Myclass(unittest.TestCase):
	def setUp(self):
		pass

	def test_get_current_class_module_name(self):
		# gives module name
		self.mat_obj = re.search('(\w|\d)+.py$', str(__file__))
		logging.debug('in module ')
		if self.mat_obj:
			logging.debug('Retrieving class module name..')
			logging.debug('Current module name is: {}'.format(self.mat_obj.group()))
		else:
			logging.error('Error in retrieving module name!!')

	def test_get_current_class_name(self):
		'''Shortcut: self.__class__.__name__'''

		obj = self.test_get_current_class_module_name.__func__
		mat_obj = re.search('function (\w|\d|_)+\.',str(obj))
		logging.debug('in class ')
		if mat_obj:
			logging.debug('Current class name is: {}'.format(mat_obj.group().split()[1].split('.')[0]))
		else:
			logging.error('Error in retrieving class name')

	def test_get_current_function(self):
		obj = self.test_get_current_class_name.__func__
		mat_obj = re.search('\.(\w|\d|_)+ at', str(obj))
		if mat_obj:
			logging.debug('Current fuunction name is : {}'.format(mat_obj.group().split()[0][1:]))
		else:
			logging.error('Error in retrieving function name!!')

	def tearDown(self):
		logging.info('execution finfished..!!')

unittest.main()
