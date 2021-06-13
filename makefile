up:
	docker-compose up -d

stop:
	docker-compose stop

build:
	docker-compose build

down:
	docker-compose down -v

up-show:
	docker-compose up

revise:
	docker-compose run --rm service sh -c "alembic revision --autogenerate"
	docker-compose stop
