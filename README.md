# geolocation API

### How to build and run `geolocation API` on your local machine:
 - Naviagte to project root and perform
 ```
 docker compose build
 ```
 to build youl local environment
 ```
 docker compose up
 ```
 to run it

- Or to do it in one step
```
docker-compose up --build
```

After all is done navigate to `http://localhost:8000/`

## production 
App is hosted on Heroku and can be found here `https://geo-location-storage.herokuapp.com`


## NOTE

- I commited `.env` file only to simplify building this project for local development. For real life project this file should be part for `.gitignore`
- Please do not abuse this API because ipstack API Key is limited to only 100 requestes per month. If you want to test how it works you should register on `https://ipstack.com/` page and provide your own API KEY to the `.env` file and play with it on your local machine.
