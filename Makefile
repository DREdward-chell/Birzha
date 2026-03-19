DEV  = docker compose -f docker-compose.yml -f docker-compose.dev.yml
PROD = docker compose -f docker-compose.yml -f docker-compose.prod.yml

.PHONY: dev dev-start dev-watch dev-down prod prod-start prod-down

# Development
dev:
	$(DEV) up -d --build

dev-start:
	$(DEV) up -d

dev-watch:
	$(DEV) up --watch --build

dev-down:
	$(DEV) down

# Production
prod:
	$(PROD) up -d --build

prod-start:
	$(PROD) up -d

prod-down:
	$(PROD) down
