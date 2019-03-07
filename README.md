# Api-Movies

Api de listagem de filmes usando Flask

### Requisitos

  - Docker
  - Docker-compose
### EndPoints

  - v1/movies  - GET -  Retorna listagem de todos os filmes
  - v1/movies/<movie_id> - GET - Retorna filme pelo id ou 404
  - v1/movies/register - POST - Registra um Filme na listagem
  
Exemplo de POST  
```console
     {
        "title": "11 Minut",
        "brazilian_title": "11 Minutos",
        "year_of_production": "2015",
        "director": "Jerzy Skolimowski",
        "genre": "Suspense dramâtico",
        "cast": [{
            "role": "Jonh",
            "name": "Richard Dormer"
        }, {
            "role": "Mary",
            "name": "Paulina Chapko"
        }, {
            "role": "Jimmy",
            "name": "Wojciech Mecwaldowski"
        }]
    }
```

### Como rodar o projeto

Rodar Local
```console
make run.local
```

Rodar Testes
```console
make test
```

Usar Dataset do Telecine (1100 filmes)
```console
make populate.db
```
