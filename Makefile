.PHONY: build-dev-image
build-dev-image:
	sudo docker compose -f ./docker/docker-compose.dev.yml build

.PHONY: build-prod-image
build-prod-image:
	sudo docker compose -f ./docker/docker-compose.prod.yml build

.PHONY: up
up:
  docker compose -f ./docker/docker-compose.dev.yml up -d

.PHONY: down
down:
  docker compose -f ./docker/docker-compose.dev.yml down