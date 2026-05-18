from ultralytics import YOLO

# Load trained model
model = YOLO("model/best.pt")

def yolocoords(target_object,screen):

    # Predict
    results = model(
        screen,
        conf=0.30
    )

    # Show result
    #results[0].show(labels=False)

    boxes = results[0].boxes

    best_box = None
    best_conf = 0

    # Find most confident matching object
    for box in boxes:

        cls = int(box.cls[0])

        label = model.names[cls]

        conf = float(box.conf[0])

        # Match target object
        if label == target_object:

            # Keep highest confidence object
            if conf > best_conf:

                best_conf = conf
                best_box = box

    # Object found
    if best_box is not None:

        x1, y1, x2, y2 = best_box.xyxy[0]

        # Center coordinates
        center_x = int((x1 + x2) / 2)
        center_y = int((y1 + y2) / 2)
        print(center_x,center_y)
        return center_x, center_y

    else:

        return None


# Example
#x,y = yolocoords("discord_logo")

