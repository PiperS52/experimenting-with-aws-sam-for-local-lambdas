# experimenting-with-aws-sam-for-local-lambdas

Investigating the use of AWS SAM CLI to run lambdas locally against local postgres database.


## Generating and running migrations

- Add/Update any model in env.py
- Create a migration script with:

```bash
$ alembic revision -m "<MIGRATION NAME>"
```

- Edit the new migration file
- Run the migration with:

```bash
$ alembic upgrade head
```


## Using the local database

```bash
$ docker exec -it <container_name> psql -U postgres -d tickets
```

## Seeding the tickets table

Run the seed script to insert sample data:

```bash
$ python seed_db.py
```

## Running the lambdas locally

To build the postgres container locally:

```bash
$ docker-compose up --build -d
```

- Install AWS SAM CLI 
- Build the dependencies:

```bash
$ cd backend
$ sam build --use-container
```

- Create a shared Docker network as defined in the docker-compose.yml so the lambdas can make requests against the local postgres database:

```bash
$ docker network create sam-local
```

- Start the SAM local api:

```bash
$ sam local start-api --docker-network sam-local
```

It is then possible to invoke the lambdas by calling the mock API Gateway at e.g. ```http://localhost:3000/tickets```