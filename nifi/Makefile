build:
	docker compose build

build-service:
	docker compose build ${SERVICE}

build-no-cache:
	docker compose build --no-cache

build-service-no-cache:
	docker compose build --no-cache ${SERVICE}

pull:
	docker compose pull

up:
	docker compose up -d

up-service:
	docker compose up -d ${SERVICE} 

down:
	docker compose down 

down-service:
	docker compose down ${SERVICE}

# make logs SERVICE=service-name
logs:
	docker compose logs -f --tail 40 ${SERVICE}

# make network-create NETWORK=external-network-name
network-create:
	docker network create ${NETWORK}

# make network-remove NETWORK=external-network-name
network-remove:
	docker network rm ${NETWORK}

# make console SERVICE=service-name
console:
	docker compose exec ${SERVICE} bash

nifi-config:
	docker cp nifi:/opt/nifi/nifi-current/conf ./configs

nifi-registry-config:
	docker cp nifi-registry:/opt/nifi-registry/nifi-registry-current/conf ./configs/nifi_registry_current
	docker cp nifi-registry:/opt/nifi-registry/nifi-registry-current/database ./configs/nifi_registry_current
	docker cp nifi-registry:/opt/nifi-registry/nifi-registry-current/flow_storage ./configs/nifi_registry_current