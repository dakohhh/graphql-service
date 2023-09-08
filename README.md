# A Graphql service with basic Auth endpoints(e.g. Signup & Login).


## Installation

```
$ pip install poetry
```




Install Python requirements

```bash
poetry install 
```





# Setup
Follow these commands to clone project

```bash
git clone https://github.com/dakohhh/graphql-service.git

```


```bash
cd graphql-service

```



# Environment Variables

```
DB_CONFIG = "{MONGO_DB_URL}"

SECRET_KEY = ""
```


And then run using

```bash
uvicorn app:app --reload --port=8000 
```
Now open your browser to localhost:8000!

Then open your browser to `localhost:8000/graphql` or `127.0.0.1:8000/graphql`. to open strawberry graphl editor


