# Define a variable for the docker compose command
COMPOSE = docker compose

# Default target that runs 'clean' and then 'up'
all: clean up

# Build the images without starting the containers
build:
	$(COMPOSE) build

# Build and start the containers in detached mode
up:
	$(COMPOSE) up --build

# Stop and remove containers, networks, and volumes
down:
	$(COMPOSE) down -v

# Clean the project by running 'down' and removing the output directory
clean: down
	rm -rf out && mkdir -p out