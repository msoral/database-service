import uvicorn
from fastapi import FastAPI

from database_service.api.api import api_router
from database_service.db.init_db import init_db

init_db()

app = FastAPI(
    title="Database Service",
    openapi_url="/api/v1/openapi.json",
    description="This api follows the guidelines specified in this [link](https://opensource.zalando.com/restful-api-guidelines/#).\
    Use this service to interact with the database. All get/delete requests parameters are query parameters.\
    All post/put request parameters are sent in the body of the request in json format.\
    `start_date` and `end_date` parameters expect datetime values that comply with ISO 8601.",
    version="1.0.0",
)

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
