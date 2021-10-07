import requests
from contextlib import closing
from bs4 import BeautifulSoup

page = None  # Variable to hold the html script retrieved from the url
url = "http://lgs.gov.gh/"

'''
This block of code is for downloading the page found in the url and storing it in a variable called page 
'''
try:
    with closing(requests.get(url, stream=True)) as response:  # Get request for the data linked to url
        content_type = response.headers['Content-Type'].lower()
        if (response.status_code == 200
        and content_type is not None
        and content_type.find('html') > -1):  # If request is successful store content in page variable
            page = response.content

except requests.RequestException as e:  # Handle exception created by unsuccessful get request
    print('Error during requests to {0} : {1}'.format(url, str(e)))

'''
This part of the code is where you use Beautiful Soup to read the content of the page
the get_text function we're using gets all the text on the page
It leaves spaces where there were spaces and images and any other media
'''
if page:
    html = BeautifulSoup(page, 'html.parser')  # Format the html script for beautiful soup module
    print(html.get_text())
