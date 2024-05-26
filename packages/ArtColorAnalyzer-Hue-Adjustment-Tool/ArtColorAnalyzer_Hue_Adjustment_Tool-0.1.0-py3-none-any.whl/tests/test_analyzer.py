import unittest
import subprocess
import os

class TestArtColorAnalyzer(unittest.TestCase):
    def setUp(self):
        self.test_image = 'test_image.jpg'
        # Create a dummy image for testing
        dummy_image = np.zeros((100, 100, 3), dtype=np.uint8)
        cv2.imwrite(self.test_image, dummy_image)

    def tearDown(self):
        os.remove(self.test_image)

    def test_overall_hue_adjustment_script(self):
        result = subprocess.run(["python", "overall_hue_adjustment.py", self.test_image])
        self.assertEqual(result.returncode, 0)

    def test_object_specific_hue_adjustment_script(self):
        result = subprocess.run(["python", "object_specific_hue_adjustment.py", self.test_image])
        self.assertEqual(result.returncode, 0)

if __name__ == '__main__':
    unittest.main()

