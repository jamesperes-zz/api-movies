# Api-Movies

Api de listagem de filmes usando Flask com autenticação JWT

### Requisitos

  - Docker
  - Docker-compose
### EndPoints

  - v1/movies  - GET -  Retorna listagem de todos os filmes
  - v1/movies/<movie_id> - GET - Retorna filme pelo id ou 404
  - v1/movies/register - POST - Registra um Filme na listagem
  - v1/login - POST  - Login na api
  - v1/registration - POST - Registrar usuario

Exemplo de POST  movies
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

Exemplo de POST  Login/Registration
```console
{
    "username": "nome_teste",
    "password": "senha_teste"
}
```

### Autenticação
Resposta de Registro de usuario
```console
{
    "message": "User nome_teste was created",
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NTE5NDg0NzAsIm5iZiI6MTU1MTk0ODQ3MCwianRpIjoiZjMyNjFjMGYtMWNlOC00OTkxLWFhMzAtYjA2MzEyZTU1ZWU4IiwiZXhwIjoxNTUxOTQ5MzcwLCJpZGVudGl0eSI6ImphbWVzMSIsImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.O1g8u8DwZwtG2HYy-vNqK395GnCt3CzWFfW5eeoLiFA",

}
```
HEADER

        "key": "Authorization",
        "value": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NTE5MzgwNDYsIm5iZiI6MTU1MTkzODA0NiwianRpIjoiY2M1MjMyNjYtZTZmYy00OWEwLWEyZjQtMWI3Njc0MDMxNjc1IiwiZXhwIjoxNTUxOTM4OTQ2LCJpZGVudGl0eSI6ImphbWVzMiIsImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.m9K1Qp1Vi8n5kMPv16ApqMDzFuogIzJ0fXk-2DTh5u8",
        "type": "text"

### Como rodar o projeto

Rodar Local
```console
make run.local
```

Rodar Testes
```console
make test
```
