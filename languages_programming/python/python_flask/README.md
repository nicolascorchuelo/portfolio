# Coding Challenge

![9Untitled Diagram drawio](https://github.com/nicolascorchuelo/portfolio/assets/90802118/1928848b-b503-40dd-bed8-b6d193de0da4)

##### Load Large CSV File Using Flask (Python) to Postgres

###### Source (3.08 GB - The dataset has 4496055 rows and 18 columns)

###### Postgres docker

Change the PATH as appropriate

```python
docker run -d --name services_db -p 8009:5432 -e POSTGRES_PASSWORD=1234 -v <PATH>:/var/lib/postgres/data postgres
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
