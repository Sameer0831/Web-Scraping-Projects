'''
Let's try to scrape a real world job website like "timesjobs.com"
and get data from it related to our job requirements 
and then lets store it in a file

'''


import requests
from bs4 import BeautifulSoup
import time

print("Provide Some Unfamiliar skills to filter out")
unfamiliar_skills = input('>') # This will take 1 skill as input at a time. If we give multiple inputs using comma then we can convert it to a list using split() and then do our filtering
print(f"filtering out {unfamiliar_skills}")

#First making a connection to website and getting raw html text from it using requests library 
html_text= requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=")
soup = BeautifulSoup(html_text.content, "lxml")


''' 
Selecting a single job first
job = soup.find('li', class_ = "clearfix job-bx wht-shd-bx") # We will use this job object to extract different informations about the job like company name, skills....
# from the job object we are extracting company_name
company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ','')
# from the job object we are extracting different skills
skills = job.find('span','srp-skills').text.replace(' ','')
published_date = job.find('span','sim-posted').span.text #inside of a span we are selecting other span element then converting to text 
'''


# Based on the above logic, we will find each and every job related things by looping through the job objects using find_all()

def finding_jobs():
    jobs = soup.find_all('li', class_ = "clearfix job-bx wht-shd-bx") # We will use this job object to extract different informations about the job like company name, skills....
    for index, job in enumerate(jobs):
        base_path = r'C:\Users\samee\OneDrive\Desktop\JobPostings' # Define the base directory path that remains constant
        file_path = fr'{base_path}\file{index}' # Construct the file path with the index dynamically inserted
        published_date = job.find('span','sim-posted').span.text #filtering out the jobs based on the posted date
        #extracting only those jobs which are posted few days ago (not so long)
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ','') # from the jobs object we'll iterate through it and extract company_name and skills
            skills = job.find('span','srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            if unfamiliar_skills not in skills:
                with open(file_path, 'w') as f:
                    f.write(f"Company Name : {company_name.strip()} \n")
                    f.write(f"Required Skills : {skills.strip()} \n")
                    f.write(f"Copy & Paste the link For More Info : {more_info} \n")
                print(f"File Saved: {index}")   

if __name__ == '__main__':
    while True:
        finding_jobs()
        time_wait = 5
        print(f'Waiting {time_wait} minutes to update.....')
        time.sleep(time_wait * 60)
        
