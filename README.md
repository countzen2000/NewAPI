# Problem Statement
* Build a news Aggregator using Gnew as source
  * Search by Keyword in title
  * Search by keyword in title, content, description
  * Get top n # of articles

## Quickstart
* You need a .env file with GnewsAPI in it. It is not committed to git for security reasons.
  * You can follow the .env_sample for formatting
* Setup your env, and install the Pip requirements from requirements.txt
* Then, if you launch main.py, it should just start the service
* I recommend using the SWAGGER docs to help you; it is below.

## TechStack
* FastAPI
* Uvicorn
* Cache tool (https://pypi.org/project/cachetools/) It's a simple improvement over the built-in cache in Python
* httpx to do async rest calls to speed this up a bit
* Custom middleware: just addes process tiem for testing cache and async
  * looks like this in the response headers: 'x-process-time: 0.5520238876342773 '
* Schemas (inside the api folder) is for checking responses. it becomes more useful once we get into more CRUD
## API docs
* http://127.0.0.1:8000/redoc
* http://127.0.0.1:8000/docs

## End points
* / 
* /top
  * optional query params count=?
* /key/{keyword}
  * optional query params count=?
* /search{keyword}
  * optional query params count=?