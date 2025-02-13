import subprocess
import time

def run_yolo():
    """ Chạy YOLO trong 10 giây rồi tự dừng """
    print("🚀 Đang chạy YOLO...")

    # Lệnh chạy YOLO
    process = subprocess.Popen(
        ["python", "F:\\SmartTrashCan\\yolov5\\detect.py",
         "--weights", "F:\\SmartTrashCan\\yolov5\\best.pt",
         "--img", "640", "--conf", "0.25", "--source", "0"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    # Chạy trong 10 giây
    time.sleep(10)

    # Dừng tiến trình YOLO
    process.terminate()
    print("⏹️ YOLO đã dừng sau 10 giây.")

# Gọi thử YOLO
if __name__ == "__main__":
    run_yolo()
