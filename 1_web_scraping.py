import requests
import pandas as pd
from bs4 import BeautifulSoup

# URL of the BBC News homepage
url = "https://www.bbc.com/news"

# Send an HTTP GET request to the URL
response = requests.get(url)

#Check if the request was successful (status code 200) Status codes 204 and 400 indicate page error or page not found
if response.status_code==200:
    print("Request successful")
else:
    print("Request failed")

# with open('asvanth.html') as html_file:
#     soup=BeautifulSoup(html_file,'html.parser')
# print(soup)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.text, "html.parser")

# Extract news headlines and summaries
headlines = []
summaries=[]

for article in soup.select(".gs-c-promo-body"):
    headline = article.find("h3").text
    summary_elem = article.find("p")
    summary = summary_elem.text if summary_elem else "No summary available"
    headlines.append(headline)
    summaries.append(summary)

# Transform the extracted data into a Pandas DataFrame
news={
    "Headline":headlines,
    "Summary":summaries
}
news_df=pd.DataFrame(news)

# Display the transformed DataFrame
print("\nTransformed DataFrame:")
print(news_df)


print("\nNews:")
for i, (headline, summary) in enumerate(zip(headlines, summaries),start=1):
    print(f"{i}. {headline}\n{summary}\n")