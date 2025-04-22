# FastAPI URL Shortener

## Develop

### Setup

Right click movie-catalog -> Mark Directory as -> Sources Root


### Install packages:

uv install

### Run

Go to workdir:
```shell
cd movie-catalog
```

Run dev server:
```shell
fastapi dev
```

### Snipets
```shell
python -c 'import secrets; print(secrets.token_urlsafe(16))'
```