import requests
from bs4 import BeautifulSoup
import sqlite3

def scrape_jobs():
    conn = sqlite3.connect("jobs.db")
    c = conn.cursor()

    # Get stored company career page URLs
    c.execute("SELECT name, careers_url FROM companies")
    companies = c.fetchall()

    for company, url in companies:
        print(f"Scraping {company} careers page...")

        try:
            response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
            if response.status_code != 200:
                print(f"Failed to access {url}")
                continue

            soup = BeautifulSoup(response.text, "html.parser")
            
            # Modify these selectors based on company website structure
            job_elements = soup.find_all("div", class_="job-listing")  

            for job in job_elements:
                title = job.find("h2").text.strip()
                location = job.find("span", class_="location").text.strip()
                link = job.find("a", class_="apply")["href"]

                # Store in database
                c.execute("INSERT INTO jobs (company, role, location, apply_link) VALUES (?, ?, ?, ?)",
                          (company, title, location, link))

        except Exception as e:
            print(f"Error scraping {company}: {e}")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    scrape_jobs()

