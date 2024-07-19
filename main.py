import cv2
import numpy as np

# Replace with your downloaded YOLOv4-tiny file paths
config_path = '/home/dsd/yolo/yolov4-tiny.cfg'
weights_path = '/home/dsd/yolo/yolov4-tiny.weights'
labels_path = '/home/dsd/yolo/coco.names'  # Assuming you have class labels

def detect_objects(frame, net, output_layer_names, class_labels):
    # Process the frame
    blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    outputs = net.forward(output_layer_names)  # Get detections

    # Process detections (refer to YOLOv4 output format for details)
    bbox, label, conf = [], [], []  # Initialize lists
    h, w = frame.shape[:2]
    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = int(np.argmax(scores))
            confidence = scores[class_id]

            if confidence > 0.5:  # Filter by confidence score (adjust threshold as needed)
                center_x, center_y, box_w, box_h = (detection[0:4] * np.array([w, h, w, h])).astype('int')
                x = int(center_x - (box_w / 2))
                y = int(center_y - (box_h / 2))
                bbox.append([x, y, box_w, box_h])
                label.append(class_labels[class_id])
                conf.append(float(confidence))

    return bbox, label, conf

def main():
    # Load YOLOv4-tiny model
    net = cv2.dnn.readNetFromDarknet(config_path, weights_path)
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_DEFAULT)  # Adjust if needed
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)        # CPU execution

    # Names of output layers
    output_layer_names = net.getLayerNames()
    output_layer_names = [output_layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

    # Load class labels
    with open(labels_path, "r") as f:
        class_labels = [line.strip() for line in f.readlines()]

    # Use your webcam device path
    video_capture = cv2.VideoCapture("/dev/video0")

    while video_capture.isOpened():
        ret, frame = video_capture.read()
        if not ret:
            break

        bbox, label, conf = detect_objects(frame, net, output_layer_names, class_labels)  # Perform detection

        # Draw bounding boxes and labels (adjust as needed)
        for l, c, b in zip(label, conf, bbox):
            cv2.rectangle(frame, (b[0], b[1]), (b[0] + b[2], b[1] + b[3]), (0, 255, 0), 2)
            cv2.putText(frame, f'{l}: {c:.2f}', (b[0], b[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('Object Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
