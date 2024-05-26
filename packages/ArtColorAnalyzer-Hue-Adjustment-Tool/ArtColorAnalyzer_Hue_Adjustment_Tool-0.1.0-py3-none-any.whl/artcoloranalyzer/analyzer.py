import cv2
import numpy as np
from tkinter import Tk, Button, filedialog
import subprocess
import os

class ArtColorAnalyzer:
    def __init__(self, image_path):
        self.image_path = image_path
        self.root = Tk()
        self.root.title("Art Color Analyzer")

        self.button1 = Button(self.root, text="Overall Hue Adjustment", command=self.run_overall_hue_adjustment)
        self.button1.pack(pady=10)

        self.button2 = Button(self.root, text="Object-Specific Hue Adjustment", command=self.run_object_specific_hue_adjustment)
        self.button2.pack(pady=10)

        self.root.mainloop()

    def run_overall_hue_adjustment(self):
        subprocess.run(["python", os.path.join(os.path.dirname(__file__), "overall_hue_adjustment.py"), self.image_path])

    def run_object_specific_hue_adjustment(self):
        subprocess.run(["python", os.path.join(os.path.dirname(__file__), "object_specific_hue_adjustment.py"), self.image_path])

