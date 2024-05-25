from bs4 import BeautifulSoup, SoupStrainer

class Report:
	def __init__(self, task: str, professor: str, status: str, score: str, date: str):
		self.task = task
		self.professor = professor
		self.status = status
		self.score = score
		self.date = date

class ReportsFromPage:
	def __init__(self, page: str):
		only_tr = SoupStrainer(name="tr")
		soup = BeautifulSoup(page, parse_only=only_tr, features="html.parser")
		self.tr = soup.tr.next_sibling

	def __iter__(self):
		return self

	def __next__(self):
		if self.tr is None:
			raise StopIteration()

		[_, _, task, professor, status, score, date] = self.tr.find_all('td')

		task = task.find('a').text.strip()
		professor = professor.find('a').text.strip()
		status = status.find('div').find('span').text.strip()
		score = score.find('div').find('span').text.strip()
		date = date.find('div').find('span').text.strip()

		self.tr = self.tr.next_sibling

		return Report(task, professor, status, score, date)
