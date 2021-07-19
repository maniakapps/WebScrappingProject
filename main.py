from bs4 import BeautifulSoup
import requests

URL = "https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35"
html_text = requests.get(URL).text
soup = BeautifulSoup(html_text, 'lxml')
job_list = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")
for job in job_list:
    company_name = job.find('h3', class_="joblist-comp-name").text.replace(' ', '')
    skills = job.find('span', class_="srp-skills").text.replace(' ', '')
    published_date = job.find('span', class_="sim-posted").span.text.replace(' ','')
    print(f"Company name: {company_name.strip()}")
    print(f"Required skills: {skills.strip()}")
    print(f"Published date: {published_date.strip()}")
    print()

