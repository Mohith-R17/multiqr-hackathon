# train.py (Updated)

from ultralytics import YOLO

def train_model():
    # Load a pre-trained YOLOv8 model
    model = YOLO('yolov8n.pt')

    # We've added 'workers=0' to simplify data loading for CPU training
    results = model.train(data='data.yaml', epochs=50, imgsz=640, workers=0)

    print("Training complete. Model saved in the 'runs' directory.")

if __name__ == '__main__':
    train_model()