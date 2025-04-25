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
    
import os

from fastapi import FastAPI
from src.imgmatch_api.routers.matchImageRouter import router

from src.imgmatch_api.services.matchImageService import create_face_database
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

print(str(os.getenv("FACES_DIR")))
print("========> Đang tiến hành khởi tạo")
create_face_database(os.getenv("FACES_DIR"))
print("========> Khởi tạo thành công")

app.include_router(router , prefix="/v1")