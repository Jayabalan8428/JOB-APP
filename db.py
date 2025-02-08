import sqlite3

def create_tables():
    conn = sqlite3.connect("jobs.db")
    c = conn.cursor()

    # Table for company URLs
    c.execute('''CREATE TABLE IF NOT EXISTS companies (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    careers_url TEXT NOT NULL)''')

    # Table for job listings
    c.execute('''CREATE TABLE IF NOT EXISTS jobs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    company TEXT NOT NULL,
                    role TEXT NOT NULL,
                    location TEXT NOT NULL,
                    apply_link TEXT NOT NULL)''')

    conn.commit()
    conn.close()

def insert_companies():
    conn = sqlite3.connect("jobs.db")
    c = conn.cursor()
    
    companies = [
        ("TCS", "https://www.tcs.com/careers"),
        ("HCL", "https://www.hcltech.com/careers"),
        ("Infosys", "https://www.infosys.com/careers"),
        ("Wipro", "https://careers.wipro.com"),
        ("Capgemini", "https://www.capgemini.com/careers")
    ]
    
    c.executemany("INSERT INTO companies (name, careers_url) VALUES (?, ?)", companies)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    insert_companies()
    print("Database setup complete with sample companies.")

