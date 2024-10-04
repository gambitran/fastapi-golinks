# Golinks API

For backend of [https://github.com/gambitran/react-ts-golinks](https://github.com/gambitran/react-ts-golinks)

Built using FastAPI.

## Dependencies

- fastapi[standard]
- sqlalchemy
- asyncpg

## Development

Run `fastapi dev`

## Deploy

docker-compose.yaml in deploy for local testing. It will load some initial basic records from init/init.sql.

## TODO

- Turn Dockerfile into multistage build to reduce image size
- Implement poetry for dev dependencies
- Implement authz
