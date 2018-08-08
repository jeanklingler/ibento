.PHONY: up
up: redis

.PHONY: redis
redis:
	docker run -p 6379:6379 redis
