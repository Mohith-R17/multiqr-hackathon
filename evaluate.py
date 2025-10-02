import json
import argparse

def evaluate(pred_file, gt_file):
    with open(pred_file) as f:
        preds = json.load(f)
    with open(gt_file) as f:
        gts = json.load(f)

    print("Evaluation placeholder: compare predictions and ground truth here.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pred", required=True)
    parser.add_argument("--gt", required=True)
    args = parser.parse_args()

    evaluate(args.pred, args.gt)
