from fastapi import APIRouter, File, UploadFile
import shutil
import os
from ..services.matchImageService import matchImageService, addImageService, deleteImageService

router = APIRouter()

@router.post("/match-image")
async def match_image(file: UploadFile = File(...)):
    temp_dir = "temp_uploads"
    os.makedirs(temp_dir, exist_ok=True)

    temp_path = os.path.join(temp_dir, file.filename)

    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = matchImageService(temp_path)  # Truyền path vào dịch vụ xử lý
    # os.remove(temp_path)  # Xóa file sau khi dùng

    # return {"matched": result}
    return result


@router.post("/add-image")
async def add_image(filename : str):
    print(filename)
    flag = addImageService(filename)
    if flag:
        return {"status": "success", "name": filename}
    return {"status": "fail", "message": "Không phát hiện khuôn mặt nào."}


@router.post("/delete-image")
async def delete_image(filename : str):
    print(filename)
    flag = deleteImageService(filename)
    if flag:
        return {"status": "success", "name": filename}
    return {"status": "fail", "message": "Ảnh không tồn tại"}
