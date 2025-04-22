import requests
from parser.models import JobListing, JobSource
from bs4 import BeautifulSoup

def scrape_greenhouse_jobs(base_url):
    jobs = []

    # Greenhouse job boards have JSON endpoints
    try:
        response = requests.get(f"{base_url.rstrip('/')}/jobs")
        soup = BeautifulSoup(response.text, "html.parser")
        job_cards = soup.select('.opening')

        for job in job_cards:
            title = job.find('a').text.strip()
            url = job.find('a')['href']
            location = job.find('span', class_='location').text.strip()
            company = base_url.split("//")[1].split(".")[0]

            external_id = url.split("/")[-1]
            full_url = f"{base_url.rstrip('/')}{url}"

            jobs.append({
                "external_id": external_id,
                "title": title,
                "company": company,
                "location": location,
                "url": full_url,
            })

    except Exception as e:
        print(f"Error scraping Greenhouse: {e}")

    return jobs