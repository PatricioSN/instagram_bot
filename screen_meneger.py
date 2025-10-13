import logging
import cv2
import pyautogui
import pyscreeze


class ScreenMeneger:

    @staticmethod
    def get_all_matches_by_image(image_to_search: str):
        try:
            return list(pyautogui.locateAllOnScreen(image=image_to_search, grayscale=True, confidence=0.9))
        except pyscreeze.ImageNotFoundException:
            return []
        except Exception as e:
            logging.info(f"Error: {e}")
            return []
