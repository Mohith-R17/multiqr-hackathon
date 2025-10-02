
# Pharmacy Hackathon - Multi-QR Code Recognition

This repository contains a complete solution for the Pharmacy Hackathon. The project uses a custom-trained YOLOv8 model to detect multiple QR codes on images of medicine packs.

##  Setup and Installation

These instructions will guide you through setting up the environment and running the project.

**1. Prerequisites**
* Python 3.12+
* Git

**2. Environment Setup**
* **Clone the repository:**
    ```bash
    git clone <YOUR_GITHUB_REPO_URL_HERE>
    cd multiqr-hackathon
    ```

* **Create and activate a virtual environment:**
    ```bash
    # Create the environment
    python -m venv venv

    # Activate on Windows
    .\venv\Scripts\activate
    ```

* **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

##  Usage

Instructions on how to use the trained model and retrain it if needed.

**1. Run Training (Optional)**
The repository already includes a pre-trained model (`best.pt`). However, to retrain the model on the provided dataset, run the following command. The new model weights will be saved in a new directory inside the `runs/` folder.

python train.py

**2. Run Inference (Primary Task)**
To run detection on a folder of images and generate the submission JSON file, use the 

**infer.py script.**

**Command format:**

```bash

python infer.py --weights <path_to_model.pt> --input <path_to_images_folder> --output <output_file.json>
```
**Example using the included model and test images:**

```bash

python infer.py --weights best.pt --input test/images/ --output outputs/submission_detection_1.json
```
This will create the required submission file in the outputs folder.

**Repository Structure**

This project follows the recommended repository structure.

```bash
multiqr-hackathon/
│
├── README.md                # Setup & usage instructions 
├── requirements.txt         # Python dependencies 
├── train.py                 # Script to train the model 
├── infer.py                 # Script to run inference
├── best.pt                  # Final trained YOLOv8 model weights
├── data.yaml                # Dataset configuration file for YOLO
│
├── train/                   # Training images and labels
├── valid/                   # Validation images and labels
└── test/                    # Test images and labels
│
├── venv/                    # Virtual environment folder (ignored by git)
├── src/                     # Source code folder
└── outputs/                 # Folder for generated submission files
```

