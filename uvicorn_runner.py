import uvicorn
import os
# Cấu hình xem server sẽ chạy ở host nào port nào có thể dùng .env để cấu hình động
from dotenv import load_dotenv

load_dotenv()

def run():
    # uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
    uvicorn.run("main:app" , host = os.getenv("HOST"), port=int(os.getenv("PORT")), reload=True)
