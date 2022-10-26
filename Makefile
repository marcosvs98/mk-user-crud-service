tests:
	pytest tests/

up:
	docker-compose up -d

migrate-revision:
	export PYTHONPATH=$PWD
	alembic revision --autogenerate -m "Initial migration."

migrate-upgrade:
	export PYTHONPATH=$PWD
	alembic upgrade head