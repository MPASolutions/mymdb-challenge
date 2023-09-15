# Istruzioni
## Note Improtanti:
## Api
Le api in generale sono all'indirizzo /api/. Per accedere alla documentazione recarsi a /api/docs.
### Movies
#### Links:
- ``` api/movies``` : ritorna tutti i Movie e permette l'aggiunta.
- ``` api/movie/< pk >``` : ritorna il singolo film con primary key < pk > e ne permette la modifica e la rimozione.
#### Parametri POST/PUT:
- ``` "title"```: titolo del film
- ```  "description"```  : descrizione del film
- ```  "director"```  : primary key del direttore del film
- ```   "scripts"```  : list delle primary key dei componenti del cast
#### Esempi:
```ruby
POST: /movies
{
  "title": "prova",
  "description": "questa è una prova",
  "director": 1,
  "scripts": [
      1,
      2,
      3
  ]
}
```

Response:

```json
201 Created
{
  "title": "prova",
  "description": "questa è una prova",
  "director": 1,
  "scripts": [
      1,
      2,
      3
  ]
}
```
 ### Person
#### Links:
- ``` api/people``` : ritorna tutte le Person presenti e permette l'aggiunta.
-```  api/person/< pk >``` : ritorna la singola Person con primary key < pk > e ne permette la modifica e la rimozione.
#### Parametri POST/PUT:
- ``` "first_name"```: nome della persona
- ```  "last_name"```  : cognome della persona
- ```  "biography"```  : biografia 
#### Esempi:
```ruby
POST: /persons
{
  "first_name": "Nome",
  "last_name": "Cognome",
  "biography": "Biografia"
}
```

Response:

```json
201 Created
{
  "id": 1,
  "first_name": "Nome",
  "last_name": "Cognome",
  "biography": "Biografia"
}
```

### Characater
#### Links:
- ``` api/characters``` : ritorna tutte i Charcter presenti e permette l'aggiunta.
-```  api/person/< pk >``` : ritorna il singolo Character con primary key < pk > e ne permette la modifica e la rimozione.
#### Parametri POST/PUT:
- ``` "person"```: primary key della persona che interpreta il personaggio
- ```  "character"```  : nome del personaggio
- ```  "movie"```  : primary key del film in cui appare il personaggio
#### Esempi:
```ruby
POST: /characters
{
  "person": 4,
  "character": "Personaggio",
  "movie": 1
}
```

Response:

```json
201 Created
{
  "id": 1,
  "person": 4,
  "character": "Personaggio",
  "movie": 1
}
```
### Reviews
#### Links:
- ``` api/reviews``` : ritorna tutte le Review e permette l'aggiunta.
- ``` api/person/< pk >``` : ritorna la singola Reviews con primary key < pk > e ne permette la modifica e la rimozione.
#### Parametri POST/PUT:
- ``` "review"```: corpo della recensione
- ```  "movie"```  : primary key del film recensito
#### Esempi:
```ruby
POST: /reviews
{
  "review": "Questa è una recensione",
	"movie": 1
}
```

Response:

```json
201 Created
{
  "id": 1,
  "review": "Questa è una recensione",
  "movie": 1
}
```
## Interfaccia
### Funzionamento:
Nell'intefaccia web appaiono due sezioni, una sulla parte destra e una sulla parte sinistra dello schermo. Cliccando sui titoli dei film presenti nella parte sinistra verrano mostrate le informazioni riuardanti il film selezionato.
