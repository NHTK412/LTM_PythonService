import os

from fastapi import FastAPI
from src.imgmatch_api.routers.matchImageRouter import router

from src.imgmatch_api.services.matchImageService import create_face_database
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

print("========> Đang tiến hành khởi tạo")
create_face_database(os.getenv("FACES_DIR"))
print("========> Khởi tạo thành công")

app.include_router(router , prefix="/v1")