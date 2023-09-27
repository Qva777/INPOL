import pyautogui
import time
from env_config import API_KEY


class ActivateExtension:
    def __init__(self):
        self.confidence_threshold = 0.9  # Percentage of matches

    def wait_for_element(self, image_path, timeout=10):
        start_time = time.time()
        while time.time() - start_time < timeout:
            location = pyautogui.locateOnScreen(image_path, confidence=self.confidence_threshold)
            if location:
                return location
            time.sleep(1)
        return None

    def run(self):
        button_locations = {
            'Photo/1.png': "Clicked on the extension button",
            'Photo/2.png': "Clicked on the extension",
            'Photo/3.png': "Input API_KEY",
            'Photo/4.png': "Enter",
            'Photo/5.png': "Close the extension"
        }

        for image_path, message in button_locations.items():
            location = self.wait_for_element(image_path)
            if location:
                # For Basic display
                pyautogui.moveTo(location)
                pyautogui.click()
                print(message)

                # For Retina display
                # x, y, width, height = location
                # center_x = (x + width / 2) / 2
                # center_y = (y + height / 2) / 2
                # pyautogui.click(center_x, center_y)

                if image_path == 'Photo/3.png':
                    pyautogui.write(API_KEY)
            else:
                print(f"{message} not found")


activate_extension = ActivateExtension()

if __name__ == '__main__':
    activate_extension.run()
