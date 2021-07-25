# Notes

- docker --link to container hostname
- type cast of port number to int

# Build database
docker build -t db --file DockerfilePostgres .

# Start database
docker run --rm --name db db

# Build app

docker build -t app --file DockerfilePython .

# Run app

docker run --link db -e DB_HOST=db -e DB_PORT=5432 app

# Observe:

```
Connected OK
```
