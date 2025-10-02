# infer.py (Final Version)

import json
import argparse
import os
from ultralytics import YOLO

def inference(weights_path, input_dir, output_file):
    # Load your custom-trained YOLOv8 model
    model = YOLO(weights_path)
    results_list = []

    image_files = [f for f in os.listdir(input_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    print(f"Found {len(image_files)} images. Starting inference...")

    for fname in image_files:
        img_path = os.path.join(input_dir, fname)

        # Run detection
        results = model(img_path)

        image_result = {"image_id": fname, "qrs": []}

        # Process the results for the current image
        for result in results:
            boxes = result.boxes.cpu().numpy() # get boxes on cpu in numpy format
            for box in boxes:
                # Get coordinates in [x_min, y_min, x_max, y_max] format
                r = box.xyxy[0].astype(int)
                # For the bonus challenge, you would add QR decoding logic here
                qr_data = {"bbox": r.tolist()}
                image_result["qrs"].append(qr_data)

        results_list.append(image_result)
        print(f"Processed {fname}, found {len(image_result['qrs'])} QR codes.")

    with open(output_file, "w") as f:
        json.dump(results_list, f, indent=2)

    print(f"\n✅ Inference complete. Results saved to {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Detect QR codes using a custom YOLOv8 model.")
    parser.add_argument("--weights", required=True, help="Path to the trained model weights (e.g., best.pt).")
    parser.add_argument("--input", required=True, help="Directory with input images.")
    parser.add_argument("--output", required=True, help="Output JSON file path.")
    args = parser.parse_args()

    inference(args.weights, args.input, args.output)