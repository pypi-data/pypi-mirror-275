import cv2
import numpy as np
from tkinter import Tk, Canvas
from PIL import Image, ImageTk
from skimage.color import rgb2hsv, hsv2rgb
from skimage.util import img_as_ubyte

class OverallHueAdjustment:
    def __init__(self, image_path):
        self.image_path = image_path
        self.original_image = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)
        self.adjusted_image = self.original_image.copy()
        self.hue_shift_value = 0

        self.average_hue = self.calculate_average_hue(self.original_image)
        self.setup_gui()

    def setup_gui(self):
        self.root = Tk()
        self.root.title("Overall Hue Adjustment")

        self.canvas = Canvas(self.root, width=700, height=100)
        self.canvas.pack()

        self.hue_bar = self.create_hue_bar(700, 100)
        self.hue_bar_image = ImageTk.PhotoImage(image=self.hue_bar)
        self.canvas.create_image(0, 0, anchor='nw', image=self.hue_bar_image)

        original_hue_x = int(self.average_hue * 700)
        self.original_hue_position = self.canvas.create_oval(
            original_hue_x - 5, 45,
            original_hue_x + 5, 55,
            outline="white", width=2
        )

        self.pointer = self.canvas.create_line(0, 0, 0, 100, fill="white", width=2)
        self.canvas.bind("<Button-1>", self.update_hue_shift)

        self.show_image(self.adjusted_image)

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

    def calculate_average_hue(self, image):
        hsv_image = rgb2hsv(image)
        hue_channel = hsv_image[:, :, 0]
        average_hue = np.mean(hue_channel)
        return average_hue

    def show_image(self, image):
        bgr_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        cv2.imshow('Overall Hue Adjustment', bgr_image)

    def update_hue_shift(self, event):
        hue = event.x / 700.0
        self.hue_shift_value = (hue * 360.0) - (self.average_hue * 360.0)
        self.preview_hue_shift()
        self.update_pointer(event.x)

    def update_pointer(self, x):
        self.canvas.coords(self.pointer, x, 0, x, 100)

    def preview_hue_shift(self):
        if self.hue_shift_value == 0:
            self.adjusted_image = self.original_image.copy()
        else:
            self.adjusted_image = self.adjust_hue(self.original_image, self.hue_shift_value)
        self.show_image(self.adjusted_image)

    def adjust_hue(self, image, hue_shift):
        hsv_image = rgb2hsv(image)
        hsv_image[:, :, 0] = (hsv_image[:, :, 0] + hue_shift / 360.0) % 1.0
        adjusted_rgb_image = hsv2rgb(hsv_image)
        return img_as_ubyte(adjusted_rgb_image)

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: overall_hue_adjustment <path_to_image>")
        sys.exit(1)
    image_path = sys.argv[1]
    OverallHueAdjustment(image_path)

if __name__ == "__main__":
    main()

