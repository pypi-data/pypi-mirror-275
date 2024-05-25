import re
from bs4 import BeautifulSoup, SoupStrainer

class Report:
	def __init__(self, id: int, task: str, professor: str, status: str, score: str, date: str):
		self.id = id
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

	REPORT_ID_RE = re.compile(r'/inside/student/reports/([0-9]+)/download')

	def __next__(self):
		if self.tr is None:
			raise StopIteration()

		[link, _, task, professor, status, score, date] = self.tr.find_all('td')

		link = link.find(name='a', attrs={'title': 'Скачать отчет'}).attrs['href']
		task = task.find('a').text.strip()
		professor = professor.find('a').text.strip()
		status = status.find('div').find('span').text.strip()
		score = score.find('div').find('span').text.strip()
		date = date.find('div').find('span').text.strip()

		id = int(ReportsFromPage.REPORT_ID_RE.match(link).group(1))

		self.tr = self.tr.next_sibling

		return Report(id, task, professor, status, score, date)
