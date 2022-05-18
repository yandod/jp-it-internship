install:
	docker compose run python pip install -r requirements.txt --user
download:
	docker compose run python python3 retrieve_csv.py
url:
	docker compose run python python3 retrieve_url.py
internship:
	docker compose run python python3 retrieve_internship.py
convert:
	docker compose run python python3 convert_csv.py

