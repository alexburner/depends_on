Run one:
```sh
docker compose up
```

Run both:
```sh
docker compose -f docker-compose.yaml -f docker-compose.fullstack.yaml up
```

Debug healthcheck:
```sh
docker inspect --format "{{json .State.Health }}" <container> | jq
```
