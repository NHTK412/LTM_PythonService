import face_recognition  # Thư viện xử lý nhận diện khuôn mặt
import numpy as np       # Thư viện xử lý toán học, đặc biệt là mảng
import os                # Thư viện thao tác với hệ thống tệp

# Hàm tạo cơ sở dữ liệu khuôn mặt từ thư mục ảnh mẫu
def create_face_database(faces_dir):
    known_face_encodings = []  # Danh sách vector đặc trưng (embedding) của khuôn mặt
    known_face_names = []      # Danh sách tên tương ứng với mỗi vector đặc trưng

    # Duyệt tất cả file ảnh trong thư mục
    for filename in os.listdir(faces_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(faces_dir, filename)  # Lấy đường dẫn đầy đủ đến ảnh
            face_image = face_recognition.load_image_file(image_path)  # Tải ảnh
            face_encodings = face_recognition.face_encodings(face_image)  # Trích xuất vector khuôn mặt

            if face_encodings:  # Kiểm tra xem ảnh có khuôn mặt không
                known_face_encodings.append(face_encodings[0])  # Lưu vector khuôn mặt đầu tiên
                known_face_names.append(os.path.splitext(filename)[0])  # Lưu tên file (không đuôi) làm tên người

    return known_face_encodings, known_face_names  # Trả về danh sách vector và tên


# Hàm nhận diện khuôn mặt trong ảnh đầu vào
def recognize_faces_in_image(image_path, known_face_encodings, known_face_names):
    image = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)

    if not face_encodings:
        return {"status": "fail", "message": "Không phát hiện khuôn mặt nào."}

    for face_encoding in face_encodings:
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)

        THRESHOLD = 0.45

        if face_distances.size > 0:
            best_match_index = np.argmin(face_distances)
            best_distance = face_distances[best_match_index]
            confidence = 1 - best_distance  # Đảo ngược khoảng cách → độ tin cậy

            if best_distance < THRESHOLD:
                name = known_face_names[best_match_index]
                return {
                    "status": "success",
                    "name": name,
                    "confidence": round(confidence, 2)
                }

    return {"status": "success", "name": "Unknown", "confidence": 0.0}


# Hàm chính chạy chương trình
def matchImageService(image_path):
    faces_dir = 'D:/Programming_Language/Python/LearingFastAPI/imgmatch_api/Data'

    if not os.path.exists(faces_dir):
        os.makedirs(faces_dir)
        print(f"Đã tạo thư mục '{faces_dir}'. Vui lòng thêm ảnh mẫu.")
        return None

    image_count = sum(1 for f in os.listdir(faces_dir)
                      if f.endswith('.jpg') or f.endswith('.png'))
    if image_count == 0:
        print(f"❌ Không có ảnh mẫu trong thư mục '{faces_dir}'.")
        return None

    known_face_encodings, known_face_names = create_face_database(faces_dir)
    print(f"📦 Đã nạp {len(known_face_encodings)} khuôn mặt.")
    result = recognize_faces_in_image(image_path, known_face_encodings, known_face_names)
    return result

