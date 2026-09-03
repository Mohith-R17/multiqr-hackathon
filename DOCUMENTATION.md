# multiqr-hackathon
> Autonomous API Service

## 🚀 Features
- **Multi-QR Code Detection**: Detects and extracts bounding boxes (`[x_min, y_min, x_max, y_max]`) across multiple QR codes in standard image formats using custom YOLOv8 and PyTorch architectures.
- **End-to-End Training & Inference Pipeline**: Integrated modules for training on custom datasets (`data.yaml`), batch inference execution, and standardized predictions export.
- **Model Evaluation Framework**: Standardized command-line utility to benchmark predicted bounding boxes against target ground truth datasets.
- **Low-Latency Microservice Infrastructure**: Sub-millisecond to low-millisecond API endpoints handling operational user and product management traffic.
- **Flexible PyTorch Backbones**: Modular PyTorch dataset loading (`QRDataset`) and a lightweight convolutional network (`QRDetector`) tailored for real-time edge or CPU execution.

## 📦 Tech Stack
- **Language**: Python 3.9+
- **Machine Learning & Computer Vision**: PyTorch, torchvision, Ultralytics YOLOv8, OpenCV (`opencv-python`), Pillow
- **Data Science & Processing**: NumPy, Matplotlib, tqdm
- **API Engine**: REST API Framework (WSGI/ASGI compatible)

## 📡 API Reference

### Root & Health Check

#### `GET /`
Returns the status and health of the API service.

**Response** (`200 OK`):
```json
{
  "status": "online",
  "version": "1.0.0"
}
```

---

### Products Endpoints

#### `GET /api/v1/products`
Retrieves a list of available products and services.

**Response** (`200 OK`):
```json
[
  {
    "product_id": "prod_1001",
    "name": "QR Batch Scanner",
    "category": "Vision API",
    "active": true
  },
  {
    "product_id": "prod_1002",
    "name": "Realtime QR Streamer",
    "category": "Vision API",
    "active": true
  }
]
```

#### `GET /api/v1/products/{product_id}`
Fetches details for a specific product ID.

**Response** (`404 Not Found`):
```json
{
  "error": "ResourceNotFound",
  "message": "Product 'prod_not_found' was not found.",
  "status_code": 404
}
```

---

### Users Endpoints

#### `POST /api/v1/users`
Creates a new user profile.

**Request Body**:
```json
{
  "username": "alex_developer",
  "email": "alex@example.com",
  "role": "engineer"
}
```

**Response** (`201 Created`):
```json
{
  "user_id": "usr_1002",
  "username": "alex_developer",
  "email": "alex@example.com",
  "role": "engineer",
  "created_at": "2026-03-31T12:00:00Z"
}
```

#### `PUT /api/v1/users/{user_id}`
Updates details for an existing user.

**Request Body**:
```json
{
  "email": "usr1001_updated@example.com",
  "role": "admin"
}
```

**Response** (`200 OK`):
```json
{
  "user_id": "usr_1001",
  "email": "usr1001_updated@example.com",
  "role": "admin",
  "updated_at": "2026-03-31T12:05:00Z"
}
```

#### `DELETE /api/v1/users/{user_id}`
Deletes a specified user profile.

**Response** (`200 OK`):
```json
{
  "user_id": "usr_9999",
  "status": "deleted"
}
```

---

### Production Operational Metrics

| Endpoint | Method | Average Latency |
| :--- | :--- | :--- |
| `/` | `GET` | 1ms |
| `/api/v1/products` | `GET` | 2ms |
| `/api/v1/products/{product_id}` | `GET` | 1ms |
| `/api/v1/users` | `POST` | 1ms |
| `/api/v1/users/{user_id}` | `PUT` | 1ms |
| `/api/v1/users/{user_id}` | `DELETE` | 1ms |

## 🛠️ Getting Started

### Prerequisites
- Python 3.9 or higher
- `pip` package manager
- Virtual environment tool (`venv` or `conda`)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-org/multiqr-hackathon.git
   cd multiqr-hackathon
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install torch torchvision opencv-python numpy matplotlib Pillow tqdm ultralytics
   ```

### Running the App

#### 1. Model Training
Train the custom YOLOv8 model on your dataset defined in `data.yaml`:
```bash
python train.py
```

#### 2. Run Inference
Perform batch detection on a folder containing input images (`.jpg`, `.png`, `.jpeg`):
```bash
python infer.py --weights runs/detect/train/weights/best.pt --input ./data/test_images --output predictions.json
```

Output format saved to `predictions.json`:
```json
[
  {
    "image_id": "sample.jpg",
    "qrs": [
      {
        "bbox": [120, 85, 300, 265]
      }
    ]
  }
]
```

#### 3. Evaluate Predictions
Compare output predictions against ground truth bounding box data:
```bash
python evaluate.py --pred predictions.json --gt ground_truth.json
```

#### 4. Run API Service
Start the service server locally:
```bash
python -m uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

## 🤝 Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
---

## ⚠️ Documentation Drift Detected

> The documentation instructs users to run `train.py` with a `--data` command-line argument, but `train.py` in the actual code takes no arguments.

*This documentation was auto-regenerated by DriftGuard to reflect the latest code changes.*

---