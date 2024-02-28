# My data journey
💫 The following section provides information related to my experience in data engineering, including the technologies and methodologies I have used. In the below repositories, the following topics are illustrated:

#### Algorithm / Theorems & Topics
---
* Search and sort algorithms
* Design patterns
* Architectural patterns
* Data structures

   * Arrangements
   * Strings
   * Chained Lists
   * Hash Tables and Hash Sets
   * Stacks
   * Queues
   * Trees
   * Networks
   * Tries

* CAP Theorem for database
* Database Optimization & Performance

![Untitled Diagram drawio](https://github.com/nicolascorchuelo/portfolio/assets/90802118/7768c278-3a6c-4d55-a1a8-54de6b03071b)

   
#### CI/CD
---
* Docker
* Terraform
* Azure DevOps
* Jenkins
* Git Actions
* Kubernetes
* Prometheus
* Grafana

#### Cloud Processing
---
 * [AWS](https://github.com/nicolascorchuelo/portfolio/tree/main/cloud_processing/aws)
 * [Azure](https://github.com/nicolascorchuelo/portfolio/tree/main/cloud_processing/aws)

#### Data Architecture Diagram
---
  * [RDBMS Relational Database](https://github.com/nicolascorchuelo/portfolio/blob/main/data_architecture_diagram/)
  * [Data warehouse](https://github.com/nicolascorchuelo/portfolio/blob/main/data_architecture_diagram/)
    
    *   Database specialist, specializing in the implementation of the **Kimball dimensional model**, including Type 1 and Type 2 dimensions, as well as a **snowflake dimension** and factless fact tables. Experienced in implementing **change data capture (CDC) processes** to efficiently track and manage data updates and modifications.
      
  * [Datalake](https://github.com/nicolascorchuelo/portfolio/blob/main/data_architecture_diagram/)
  * [Lakehouse](https://github.com/nicolascorchuelo/portfolio/blob/main/data_architecture_diagram/)
  * [Databricks](https://github.com/nicolascorchuelo/portfolio/blob/main/data_architecture_diagram/)
  * [Snowflake](https://github.com/nicolascorchuelo/portfolio/blob/main/data_architecture_diagram/)
  * [Kafka architecture](https://github.com/nicolascorchuelo/portfolio/blob/main/data_architecture_diagram/)

#### [Data Governance](https://github.com/nicolascorchuelo/portfolio/tree/main/data_governance)
---
* Policy Management
* Data Quality
* Master Data Management
* Metadata Management
* Data Security & Privacy
  
#### Languages Programming
---
* [SQL](https://github.com/nicolascorchuelo/portfolio/tree/main/languages_programming/sql)
* [Python](https://github.com/nicolascorchuelo/portfolio/tree/main/languages_programming/python)

   * Best practices
   * Python for data
   * Python for data application (Airflow, Spark..etc)
  
* [Apache Spark with Scala](https://github.com/nicolascorchuelo/portfolio/tree/main/languages_programming/scala)

#### Reporting
---
https://public.tableau.com/app/profile/nicolas.corchuelo

#### Tools & More
---
* ##### SSIS (Integration Services)
* ##### ADF (Azure Data Facture)
* ##### Power BI
   * DAX
* ##### Microsoft Purview

## Projects
---
![Untitled Diagram drawio](https://github.com/nicolascorchuelo/portfolio/assets/90802118/58e8a255-6ccc-476e-a0ab-f08230487b72)

##### [Load Large CSV File Using Python to Postgres](https://github.com/nicolascorchuelo/portfolio/tree/main/languages_programming/python/python_for_data/etl_file_to_db)

###### Source (3.08 GB - The dataset has 4496055 rows and 18 columns)

[https://www.kaggle.com/datasets/anoopjohny/consumer-complaint-database/data](https://www.kaggle.com/datasets/anoopjohny/consumer-complaint-database/data)

###### Postgres docker

```python
docker run -d --name services_db -p 8009:5432 -e POSTGRES_PASSWORD=1234 -v /Users/nicolascorchuelo/data/db_pg:/var/lib/postgres/data postgres
```
###### Environment Python

```python
python3 -m venv etl_env
source etl_env/bin/activate
python -m pip install --upgrade pip
deactivate
```
###### Outcome
Insert time: 124.409982919693 seconds
