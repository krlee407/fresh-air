import pandas as pd
import datetime

'''
	LastYearModel : 날짜를 입력 받아, 전 해에 동일한 날짜의 값을 출력해줌
'''
class LastYearModel:

	''' Legacy
	def __init__(self, year=2017):
		self.model = pd.DataFrame(columns=['date', 'value'])
		self.model['date'] = [datetime.strptime('2017-01-01 00:00:00', '%Y-%m-%d %H:%M:%S') + 
							  timedelta(hours=i) for i in range(365*24)]

	def train(self, train_data):
		self.model['value'] = train_data



	def predict(self, date):
		if len(date) < 6:
			date = '2017-' + date
		return self.model[self.model['date'] == date]['value'].values[0]
	'''

	def __init__(self):
		self.model = {}

	def train(self, X, y):
		# exception
		if len(X) != len(y):
			raise CustomError("need 'len(X) == len(y)'")

		for x_value, y_value in zip(X, y):
			self.model[x_value] = y_value

	def predict(self, x):
		key = datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S') + datetime.timedelta(days=-365)
		key = key.isoformat(' ')
		return self.model[key]

class CustomError(Exception):
	def __init__(self, msg):
		self.msg = msg

	def __str__(self):
		return self.msg