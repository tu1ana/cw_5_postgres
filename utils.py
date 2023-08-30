import psycopg2

from api_class import HeadHunterAPI
from config import config


params = config()
conn = psycopg2.connect(**params)
cur = conn.cursor()


cur.execute('''
    CREATE TABLE employers 
        (
            employer_id serial PRIMARY KEY,
            employer_name varchar(255) NOT NULL
        )
        ''')

cur.execute('''
    CREATE TABLE jobs 
        (job_id serial PRIMARY KEY,
        job_title varchar(255) NOT NULL,
        employer_id int NOT NULL,
        salary_from int,
        salary_to int,
        url varchar(255) NOT NULL,
        FOREIGN KEY (employer_id) REFERENCES employers(employer_id)
        )
        ''')

hh_api = HeadHunterAPI()
employer_data = hh_api.get_employer_data(HeadHunterAPI.employer_list)

for employer, jobs in employer_data.items():
    cur.execute('''
        INSERT INTO employers (employer_name)
        values (%s)
        RETURNING employer_id
        ''', (employer,)
                )
    employer_id = cur.fetchone()[0]

    for job in jobs:
        job_title = job.get('name')
        salary_from = job.get('salary', {}).get('from', 0) if job.get('salary') else 0
        salary_to = job.get('salary', {}).get('to', 0) if job.get('salary') else 0
        url = job.get('alternate_url')

    cur.execute('''
        INSERT INTO jobs (job_title, employer_id, salary_from, salary_to, url)
        VALUES (%s, %s, %s, %s, %s)
        ''', (job_title, employer_id, salary_from, salary_to, url))

conn.commit()
cur.close()
conn.close()
