import random
import requests

from IPython import embed
from time import sleep
from bs4 import BeautifulSoup 

BASE_URL = "https://sample-target-bucket-with-html-pages-s3.ap-southeast-1.amazonaws.com"

def start_end_decorator(func):
	def wrapper(*args, **kwargs):
		print(f"[START {func.__name__}]")
		output = func(*args, **kwargs)
		print(f"[END {func.__name__}]")
		return output

	return wrapper


#start_end_decorator
def delay(seconds):
	print(f"Sleeping for {seconds} second(s)")
	sleep(seconds)

def get_random_number():
	return random.randint(1, 5)

#@start_end_decorator
def extract_html_content(target_url):
	print(f"Downloading HTML content of {target_url}")
	response = requests.get(target_url)
	return response.text

#@start_end_decorator
def extract_target_value_from_page(html_string):
	soup = BeautifulSoap(html_string, 'html.parser')
	target = soup.find(id="target")
	return target.get_text()

#@start_end_decorator 
def extract_links_from_page(html_string):
	soup = BeautifulSoap(html_string, 'html.parser')
	anchors = soup.find_all('a')
	return anchors

def main(): 
	delay(get_random_number())
	html_doc = extract_html_content(BASE_URL + '/' + 'group2/index.html')
	anchors = extract_links_from_page(html_doc)
	for anchor in anchors:
		delay(get_random_number())
		href_link = BASE_URL + anchor.get('href')
		link_content = extract_html_content(href_link)
		value = extract_target_value_from_page(link_content)
		print(value)


if __name__ == "__main__":
	main()


