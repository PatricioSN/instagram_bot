import logging
import cv2
import pyautogui

class ScreenMeneger:
    @staticmethod
    def get_all_matches_by_image(image_to_search: str):
        try:
            return pyautogui.locateAllOnScreen(image=image_to_search, grayscale=True, confidence=0.9)
        except Exception as e:
            logging.info(f"Error: {e}")