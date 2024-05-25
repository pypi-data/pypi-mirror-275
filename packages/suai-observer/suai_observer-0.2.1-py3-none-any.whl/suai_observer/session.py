import pickle
import requests
import bs4

from suai_observer.report import ReportsFromPage

from bs4 import BeautifulSoup, SoupStrainer
from typing import Callable
from requests import Response

class SuaiSession:
	def __init__(self, timeout: int, cookiefile: str, username: str, password: str):
		self.timeout = timeout
		self.session = requests.Session()
		self.cookiefile = cookiefile
		try:
			with open(cookiefile, 'rb') as f:
				cookies = pickle.load(f)
				self.session.cookies.update(cookies)
		except:
			pass

		self.username = username
		self.password = password

	@staticmethod
	def login_redirected(response: Response) -> bool:
		return response.url.find("https://sso.guap.ru") != -1

	@staticmethod
	def form_url(login_page: str) -> str:
		only_form = SoupStrainer(name="form", attrs={'id': "kc-form-login"})
		soup = BeautifulSoup(login_page, parse_only=only_form, features="html.parser")
		url = soup.form.attrs['action']
		return url

	def update_login_cookies(self, form_url: str):
		form_data = {
			"username": self.username,
			"password": self.password,
			"credentialId": '',
		}
		self.session.post(form_url, data=form_data, timeout=self.timeout).raise_for_status()
		self.save_cookies()

	def save_cookies(self):
		with open(self.cookiefile, 'wb') as f:
			pickle.dump(self.session.cookies, f)

	def do_while_login(self, f: Callable[[requests.Session], Response]) -> Response:
		response = f(self.session)
		login_try_timeout = 0
		while SuaiSession.login_redirected(response):
			if login_try_timeout >= 5:
				raise TimeoutError("Way too much login attempts")
			login_try_timeout += 1

			self.update_login_cookies(SuaiSession.form_url(response.text))
			response = f(self.session)
		return response

	def get(self, *args, **kwargs) -> Response:
		return self.do_while_login(lambda s: s.get(timeout=self.timeout, *args, **kwargs))

	def post(self, *args, **kwargs) -> Response:
		return self.do_while_login(lambda s: s.post(timeout=self.timeout, *args, **kwargs))

	def reports(self) -> ReportsFromPage:
		response = self.get("https://pro.guap.ru/inside/student/reports?perPage=999999999&page=1")
		response.raise_for_status()
		return ReportsFromPage(response.text)
