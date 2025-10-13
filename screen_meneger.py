import logging
import cv2
import pyautogui
import pyscreeze
import win32gui


class ScreenMeneger:

    # The method tries to find the image on the screen and returns the coordinates of the found image.
    @staticmethod
    def get_all_matches_by_image(image_to_search: str):
        try:
            return list(pyautogui.locateAllOnScreen(image=image_to_search, grayscale=True, confidence=0.9))
        except pyscreeze.ImageNotFoundException:
            return []
        except Exception as e:
            logging.info(f"Error: {e}")
            return []


    # The method checks if the application is focused.
    @staticmethod
    def is_app_focused(app_title_name: str):
        active_window_title = win32gui.GetWindowText(win32gui.GetForegroundWindow()).lower()
        return app_title_name in active_window_title
