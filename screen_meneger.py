import pyautogui

class ScreenMeneger:
    @staticmethod
    def get_all_matches_by_image(image_to_search: str):
        try:
            pyautogui.locateAllOnScreen(image=image_to_search, grayscale=True, confidence=0.9)
