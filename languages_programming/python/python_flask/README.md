# Coding Challenge

![9Untitled Diagram drawio](https://github.com/nicolascorchuelo/portfolio/assets/90802118/1928848b-b503-40dd-bed8-b6d193de0da4)

## 1. API

### Load Large CSV File Using Flask (Python) to Postgres

* departments.csv
* hired_employees.csv
* jobs.csv

### Postgres docker

* Change the PATH as appropriate

```python
docker run -d --name services_db -p 8009:5432 -e POSTGRES_PASSWORD=1234 -v <PATH>:/var/lib/postgres/data postgres
```
### Environment Python

```python
python3 -m venv etl_env
source etl_env/bin/activate
python -m pip install --upgrade pip
deactivate
```

## Explanation
---
* **.gitignore:** 
* **connections.py:** 
* **etl.py:** 
* **etl_api_call.py:** 
* **flask_env:** 
* **prueba.py:** 
* **static/swagger.json:** 

## Database questions

```sql
SELECT de.department,j.job,
    SUM(CASE WHEN EXTRACT(quarter FROM he.datetime) = 1 THEN 1 ELSE 0 END) AS Q1,
    SUM(CASE WHEN EXTRACT(quarter FROM he.datetime) = 2 THEN 1 ELSE 0 END) AS Q2,
    SUM(CASE WHEN EXTRACT(quarter FROM he.datetime) = 3 THEN 1 ELSE 0 END) AS Q3,
    SUM(CASE WHEN EXTRACT(quarter FROM he.datetime) = 4 THEN 1 ELSE 0 END) AS Q4
FROM 
    hired_employees as he inner join jobs as j on he.job_id = j.id
    inner join departments de on  department_id = de.id
where EXTRACT(YEAR FROM datetime) = 2021
GROUP BY j.job,de.department
order by de.department asc, j.job asc
```

![image](https://github.com/nicolascorchuelo/portfolio/assets/90802118/2a17f5ca-8c2c-4e82-855d-82a4b56ee69e)

```sql
SELECT de.id,
       de.department,
       Count(0) hired
FROM   hired_employees he
       INNER JOIN departments de
               ON he.department_id = de.id
WHERE  Extract(year FROM datetime) = 2021
GROUP  BY de.id,
          de.department
ORDER  BY Count(0) DESC 
```
![image](https://github.com/nicolascorchuelo/portfolio/assets/90802118/34c73c84-b073-4529-b61c-de56ed9c4e2f)

