import random
import requests

from IPython import embed
from time import sleep 
from bs4 import BeautifulSoup 

BASE_URL = "http://sample-target-bucket-with-html-pages.s3-website-ap-southeast-1.amazonaws.com"

PAGES = [
	"group1/1.html", 
	"group1/2.html",
	"group1/3.html", 
	"group1/4.html", 
	"group1/5.html",
]

def delay(seconds): 
	print(f"Sleeping for {seconds} second(s)")
	sleep(seconds)

def get_random_number():
	return random.randint(1, 3)

def extract_html_content(target_url):
	response = requests.get(target_url)

	return response.txt

def extract_target_value_from_page(html_string):
	soup = BeautifulSoup(html_string, "html.parser")

	div_elements = soup.find_all("div", {"id": "target"})

	return div_elements

def main():
	for page in PAGES:
		target_page = BASE_URL + "/" + page
		html_content = extract_html_content(target_page)
		target_values = extract_target_value_from_page(html_content)

		for target_value in target_values:
			print(target_value.get_text())

		delay(get_random_number())


if __name__ == "__main__":
	main()