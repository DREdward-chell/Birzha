DEV  = docker compose -f docker-compose.yml -f docker-compose.dev.yml
PROD = docker compose -f docker-compose.yml -f docker-compose.prod.yml

.PHONY: dev dev-build dev-watch dev-down prod prod-build prod-down

# Development
dev:
	$(DEV) up -d

dev-build:
	$(DEV) up -d --build

dev-watch:
	$(DEV) up --watch

dev-down:
	$(DEV) down

# Production
prod:
	$(PROD) up -d

prod-build:
	$(PROD) up -d --build

prod-down:
	$(PROD) down
