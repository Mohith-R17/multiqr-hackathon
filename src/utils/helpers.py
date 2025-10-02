def draw_bbox(image, bbox, color=(0,255,0), thickness=2):
    import cv2
    x1, y1, x2, y2 = bbox
    return cv2.rectangle(image, (x1, y1), (x2, y2), color, thickness)
