# from fastapi import FastAPI

# app = FastAPI()

# users = {
#     "Id" : "058205002155",
#     "Name" : "Nguyễn Hữu Tuấn Khang",
#     "Class" : "CN2407CLCB"
# }

# @app.get("/")
# def helloWorld():
#     return {
#         "Mess" : "Hello World"
#     }

# @app.get("/user")
# async def getUser(q : str | None = None):
#     if q is not None:
#         if q == users["Id"]:
#             return users
#     else:
#         return {
#             "message": "User not found"
#         }
    


from fastapi import FastAPI
from src.imgmatch_api.routers.matchImageRouter import router


app = FastAPI()

app.include_router(router , prefix="/v1")