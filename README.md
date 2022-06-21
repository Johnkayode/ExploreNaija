
# Explore Naija

API for Nigerian states and capitals, cities, towns and tourist centres.

Built with [Django](https://www.djangoproject.com/) and [Django Rest Framework](https://www.django-rest-framework.org/) (DRF)

## Installation

install docker from [here](https://www.docker.com/get-started)

create docker image

```bash
docker build .
```

## API Reference

Check out the full API docs [here](https://explore-naija.herokuapp.com/v1/docs/)

#### List all states Get a particular city or state

```http
  GET /v1/cities-towns/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `name` | `string` (query) | Get a particular Nigerian city or town by its name |


#### List all states Get a particular state

```http
  GET /v1/states/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name` | `string` (query) | Get a particular Nigerian state by its name |


#### Get all tourist centres Get a particular tourist centre

```http
  GET /v1/tourist-centres/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name` | `string` (query) | Get a particular Nigerian tourist centre by its name(s) |
| `town` | `string` (query) | Filter the tourist centres by the name of a Nigerian town |
| `state` | `string` (query) | Filter the tourist centres by the name of a Nigerian state |

