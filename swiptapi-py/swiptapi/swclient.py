import logging
import requests

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] {%(filename)s} %(levelname)s - %(message)s')

class swiptapi_client:
	"""
	An object to streamline interactions against the Swiss Public Transit API.
	"""

	def __init__(self):
		logging.info("Client initialized")

	def search_around_point(self, lati: float, longi: float):
		"""
		Searches around a specified lat long pair for buses in switzerland
		"""
		query = self._construct_positional_search_query(lati, longi)
		return self._get_and_clean_request(query)

	def _construct_positional_search_query(self, x: float, y: float):
		"""
		Parses together the Swiss public transit API http request string
		"""
		base_string = 'http://transport.opendata.ch/v1/locations?'
		full_string = base_string + 'x=' + str(x) + '&y=' + str(y)
		return full_string

	def _get_and_clean_request(self, query: str):
		"""
		Procceses a http request and returns a json
		"""
		response = requests.get(query)
		return response.json()
