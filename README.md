[<img src="https://mpasolutions.it/img/logo.png" alt="MPA Solutions" height="80"/>](https://mpasolutions.it)
[<img src="https://www.enogis.it/wp-content/uploads/2020/09/enogis_flat_logo.png" alt="Enogis" height="80"/>](https://enogis.it)

# Cerchiamo appassionati che lavorino con noi!

Ti interessa far parte di un gruppo di sviluppo innovativo e stimolante? Stiamo cercando persone originali, amanti della tecnologia, con voglia di innovare e mettersi in gioco. 
Per capire se sei il tipo adatto per entrare nel magico mondo degli ecotecnologi, sviluppa a modo tuo il progetto MyMDB. Fallo in modo veloce e pulito, se vuoi essere dei nostri!

# MyMDb (My Movie Database)
Creazione di una piattaforma per la gestione di film

## Requisiti

- L'applicazione dovrà essere scritta utilizzando il framework [Django](https://docs.djangoproject.com) versione > 4.1 con Python 3.10
- Utilizzo di un database [PostgreSQL](http://postgresql.org)
- Le varie funzionalità andranno sviluppate in branch separati per poi fare merge sul branch `main` solo a feature conclusa

## Definizione del progetto

- Creazione di un progetto `mymdb`
- Creazione delle applicazioni `cast`, `movies` e `reviews`
- Il progetto dovà gestire le seguenti entità (d'ora in poi indicate come modelli o models):
  - `Person`: anagrafica dei componenti del cast (registi, scenografi, attori, ecc.)
  - `Movie`: anagrafica del film con titolo, descrizione, ecc.
  - `Character`: attori che compaiono nel film, con foreignkey verso `Person` e `Movie` per indicare che un certo attore compare in un certo film con un nickname
  - `Review`: recensioni sia di `Film` che di `Person` e `Character` tramite una generic foreign key (limitata ai soli modelli sopra esplicitati)
- Tutti i modelli dovranno avere i due campi `created_at` e `updated_at` per conoscere la data di creazione e modifica del record
- Aggiunta di API rest per la gestione (crezione, modifica, modifica parziale, ecc.) delle varie entità di tutti i modelli e pubblicazione di una sezione di documentazione delle API tramite Swagger UI (si consiglia l'utilizzo di Django Rest Framework e di drf-spectacular o drf-yasg)
  - Le liste delle api dei modelli `Film`, `Person` e `Character` dovranno contenere una lista di recensioni
- Creazione di un'interfaccia frontend utilizzando il framework [Webix](https://webix.com) dove verranno mostrati i vari film presenti a catalogo e potranno essere aggiunti tramite form specifica

## Esempi API

### Creazione di un'anagrafica

```ruby
POST: /persons
{
  "first_name": "James",
  "last_name": "Cameron",
  "biography": "..."
}
```

Response:

```json
201 Created
{
  "id": 1,
  "first_name": "James",
  "last_name": "Cameron",
  "biography": "..."
}
```

### Creazione di un film

```ruby
POST: /movies
{
  "title": "Avatar - La via dell'acqua",
  "description": "Jake Sully vive con la sua nuova famiglia sulla luna extrasolare Pandora. Quando una minaccia ritorna per finire ciò che era stato iniziato in precedenza, lavora con Neytiri e l'esercito della razza Na'vi per proteggere la loro casa.",
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
  "id": 1,
  "title": "Avatar - La via dell'acqua",
  "description": "Jake Sully vive con la sua nuova famiglia sulla luna extrasolare Pandora. Quando una minaccia ritorna per finire ciò che era stato iniziato in precedenza, lavora con Neytiri e l'esercito della razza Na'vi per proteggere la loro casa.",
  "director": 1,
  "script": [
    1,
    2,
    3
  ]
}
```

### Creazione di un personaggio

```ruby
POST: /characters
{
  "person": 4,
  "character": "Jake",
  "movie": 1
}
```

Response:

```json
201 Created
{
  "id": 1,
  "person": 4,
  "character": "Jake",
  "movie": 1
}
```

### Creazione di una recensione

```ruby
POST: /reviews
{
  "review": "La mia recensione",
  "content_type": 8,
  "object_id": 1
}
```

Response:

```json
201 Created
{
  "id": 1,
  "review": "La mia recensione",
  "content_type": 8,
  "object_id": 1
}
```

#### Ricezione di tutti i film

```ruby
GET: /movies
```

Response:

```json
[
  {
    "id": 1,
    "title": "Avatar - La via dell'acqua",
    "description": "Jake Sully vive con la sua nuova famiglia sulla luna extrasolare Pandora. Quando una minaccia ritorna per finire ciò che era stato iniziato in precedenza, lavora con Neytiri e l'esercito della razza Na'vi per proteggere la loro casa.",
    "director": {
      "first_name": "James",
      "last_name": "Cameron"
    },
    "scripts": [
      {
        "first_name": "Sam",
        "last_name": "Sam Worthington"
      }
    ],
    "actors": [
      {
        "person": {
          "first_name": "Sam",
          "last_name": "Worthington"
        },
        "character": "Jake"
      },
      {
        "person": {
          "first_name": "James",
          "last_name": "Cameron"
        },
        "character": "string"
      }
    ],
    "reviews": [
      {
        "review": "La mia recensione"
      },
      {
        "review": "Un'altra recensione"
      }
    ]
  },
  // ...
]
```

## Extra avanzati

- Creazione di un immagine [Docker](http://docker.com) del progetto permettendo la configurazione tramite variabili d'ambiente 
- Suddivisione in microservizi (tramite [Docker Compose](https://docs.docker.com/compose/)) delle varie componenti create precedentemente (es. django, postgres, nginx, ecc.)
- Disaccoppiamento di frontend e backend in due microservizi separati, facendoli comunicare tramite api
- Ristrutturazione del frontend attraverso il framework [ReactJS](https://reactjs.org) o [AngularJS](http://angularjs.org)
- Aggiunta di Test Case per la validazione del codice

## Consegna del progetto

- Il progetto dovrà essere consegnato tramite una pull request sul branch `main`
- Verranno valutate solamente le funzionalità presenti sul branch `main`, quindi si ricorda di fare merge dei vari branch prima di aprire una pull request
- Sul progetto NON dovranno essere cancellati i vari branch contenenti le features
- Aggiungere un file `INSTRUCTIONS.md` alla cartella base del progetto dove verranno indicate le procedure per testare il software (che dovrà essere funzionante) e saranno descritte le varie funzionalità
- È gradito un dump del database contenente alcuni dati di esempio

## Valutazione

- Verrà valutato il tempo impiegato per lo svolgimento dell'esercizio a partire dal fork del progetto, fino alla richiesta di pull request
- Verrà inoltre valutata la pulizia del codice e l'ottimizzazione delle varie funzionalità
