# DRF_REST_API

API-REST build with Django Rest Framework

 
## Endpoints

The API has the following endpoints:

* `POST /trades` handles the creation of a new trade
* `GET /trades` returns a collection of all trades
* `GET /trades/<id>` returns a trade with the given id
* `DELETE /trades/<id>` removes a trade with the given id

## Data JSON object: 

```json
{
    "id": 1,
    "type": "buy",
    "user_id": 23,
    "symbol": "ABX",
    "shares": 30,
    "price": 134,
    "timestamp": 1531522701000
}
```