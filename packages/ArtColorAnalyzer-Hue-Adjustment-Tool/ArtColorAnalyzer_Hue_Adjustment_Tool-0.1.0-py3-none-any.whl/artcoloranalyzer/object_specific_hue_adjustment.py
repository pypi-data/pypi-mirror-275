import cv2
import numpy as np
from tkinter import Tk, Canvas
from PIL import Image, ImageTk
from skimage.color import rgb2hsv, hsv2rgb
from skimage.util import img_as_ubyte
import os

class ObjectSpecificHueAdjustment:
    def __init__(self, image_path):
        self.image_path = image_path
        if not os.path.isfile(image_path):
            raise FileNotFoundError(f"The specified image path does not exist: {image_path}")

        self.original_image = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)
        self.adjusted_image = self.original_image.copy()
        self.hue_shift_value = 0
        self.selection_start = None
        self.selection_end = None
        self.dragging = False
        self.detected_boxes = []
        self.selected_box = None
        self.original_hue_value = None

        self.net = cv2.dnn.readNet(os.path.join(os.path.dirname(__file__), "yolov3/yolov3.weights"), 
                                   os.path.join(os.path.dirname(__file__), "yolov3/yolov3.cfg"))
        with open(os.path.join(os.path.dirname(__file__), "yolov3/coco.names"), "r") as f:
            self.classes = [line.strip() for line in f.readlines()]
        self.layer_names = self.net.getLayerNames()
        self.output_layers = [self.layer_names[i - 1] for i in self.net.getUnconnectedOutLayers()]

        self.detect_objects(self.original_image)
        self.setup_gui()

    def setup_gui(self):
        self.root = Tk()
        self.root.title("Object-Specific Hue Adjustment")

        self.canvas = Canvas(self.root, width=700, height=100)
        self.canvas.pack()

        self.hue_bar = self.create_hue_bar(700, 100)
        self.hue_bar_image = ImageTk.PhotoImage(image=self.hue_bar)
        self.canvas.create_image(0, 0, anchor='nw', image=self.hue_bar_image)

        self.pointer = self.canvas.create_line(0, 0, 0, 100, fill="white", width=2)
        self.canvas.bind("<Button-1>", self.update_hue_shift)

        self.show_image(self.adjusted_image)

        cv2.imshow('Select Object', cv2.cvtColor(self.adjusted_image, cv2.COLOR_RGB2BGR))
        cv2.setMouseCallback('Select Object', self.select_object)

        self.root.mainloop()

    def create_hue_bar(self, width, height):
        hue_bar = Image.new("RGB", (width, height))
        for x in range(width):
            hue = x / width
            rgb = hsv2rgb(np.array([[[hue, 1.0, 1.0]]]))[0][0]
            color = tuple(int(c * 255) for c in rgb)
            for y in range(height):
                hue_bar.putpixel((x, y), color)
        return hue_bar

    def show_image(self, image, window_name='Object-Specific Hue Adjustment'):
        bgr_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if window_name == 'Select Object':
            if self.selected_box is not None:
                x, y, w, h = self.selected_box
                cv2.rectangle(bgr_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            elif self.selection_start is not None and self.selection_end is not None:
                x1, y1 = self.selection_start
                x2, y2 = self.selection_end
                x_min, x_max = min(x1, x2), max(x1, x2)
                y_min, y_max = min(y1, y2), max(y1, y2)
                cv2.rectangle(bgr_image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
        cv2.imshow(window_name, bgr_image)

    def update_hue_shift(self, event):
        hue = event.x / 700.0
        self.hue_shift_value = hue * 360.0
        self.preview_hue_shift()
        self.update_pointer(event.x)

    def update_pointer(self, x):
        self.canvas.coords(self.pointer, x, 0, x, 100)

    def preview_hue_shift(self):
        if self.selected_box is not None:
            self.adjusted_image = self.adjust_hue(self.original_image, self.hue_shift_value, self.selected_box)
        elif self.selection_start is not None and self.selection_end is not None:
            self.adjusted_image = self.adjust_hue(self.original_image, self.hue_shift_value, self.selection_start, self.selection_end)
        self.show_image(self.adjusted_image)
        self.show_image(self.original_image, window_name='Select Object')

    def adjust_hue(self, image, hue_shift, *box):
        hsv_image = rgb2hsv(image)
        if len(box) == 2:  # If box is a tuple, it means it's a manual selection
            x1, y1 = box[0]
            x2, y2 = box[1]
            x_min, x_max = min(x1, x2), max(x1, x2)
            y_min, y_max = min(y1, y2), max(y1, y2)
            self.original_hue_value = np.mean(hsv_image[y_min:y_max, x_min:x_max, 0])
            hsv_image[y_min:y_max, x_min:x_max, 0] = (hsv_image[y_min:y_max, x_min:x_max, 0] + hue_shift / 360.0) % 1.0
        else:  # Otherwise, it's a detected box
            x, y, w, h = box[0]
            self.original_hue_value = np.mean(hsv_image[y:y+h, x:x+w, 0])
            hsv_image[y:y+h, x:x+w, 0] = (hsv_image[y:y+h, x:x+w, 0] + hue_shift / 360.0) % 1.0

        adjusted_rgb_image = hsv2rgb(hsv_image)
        return img_as_ubyte(adjusted_rgb_image)

    def detect_objects(self, image):
        height, width, channels = image.shape
        blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        self.net.setInput(blob)
        outs = self.net.forward(self.output_layers)

        class_ids = []
        confidences = []
        boxes = []

        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        self.detected_boxes = [boxes[i] for i in indices.flatten()] if len(indices) > 0 else []

    def select_object(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.selection_start = (x, y)
            self.dragging = True
        elif event == cv2.EVENT_MOUSEMOVE and self.dragging:
            self.adjusted_image = self.original_image.copy()
            cv2.rectangle(self.adjusted_image, self.selection_start, (x, y), (0, 255, 0), 2)
            self.show_image(self.adjusted_image)
        elif event == cv2.EVENT_LBUTTONUP:
            self.selection_end = (x, y)
            self.dragging = False
            self.selected_box = None
            for box in self.detected_boxes:
                bx, by, bw, bh = box
                if bx <= x <= bx + bw and by <= y <= by + bh:
                    self.selected_box = box
                    break
            if not self.selected_box:
                self.update_original_hue_pointer(self.selection_start, self.selection_end)
                self.preview_hue_shift()
            else:
                self.update_original_hue_pointer((self.selected_box[0], self.selected_box[1]),
                                                (self.selected_box[0] + self.selected_box[2], self.selected_box[1] + self.selected_box[3]))
            self.show_image(self.adjusted_image)
            self.show_image(self.original_image, window_name='Select Object')

    def update_original_hue_pointer(self, start, end):
        hsv_image = rgb2hsv(self.original_image)
        x1, y1 = start
        x2, y2 = end
        x_min, x_max = min(x1, x2), max(x1, x2)
        y_min, y_max = min(y1, y2), max(y1, y2)
        selected_region = hsv_image[y_min:y_max, x_min:x_max, 0]
        self.original_hue_value = np.mean(selected_region)
        if self.original_hue_value is not None:
            original_hue_x = int(self.original_hue_value * 700)
            self.update_pointer(original_hue_x)

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: object_specific_hue_adjustment <path_to_image>")
        sys.exit(1)
    image_path = sys.argv[1]
    ObjectSpecificHueAdjustment(image_path)

if __name__ == "__main__":
    main()




