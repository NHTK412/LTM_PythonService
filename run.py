import uvicorn
from dotenv import load_dotenv
import os

# Tải biến môi trường từ file .env
load_dotenv()

# Lấy giá trị HOST và PORT từ biến môi trường
host = os.getenv("HOST", "127.0.0.1")  # Giá trị mặc định nếu không tìm thấy
port = int(os.getenv("PORT", 8000))    # Chuyển đổi sang số nguyên

if __name__ == "__main__":
    # Chạy ứng dụng FastAPI của bạn với host và port từ .env
    uvicorn.run("main:app", host=host, port=port, reload=True)