import random
import time
import keyboard
from screen_meneger import ScreenMeneger

def run():
    total_follows = 0

    while True:
        if ScreenMeneger.is_app_focused(app_title_name="instagram"):
            coordinates = ScreenMeneger.search_image_on_screen(image_to_search=r'.\img.png')
            for coordinate in coordinates:
                ScreenMeneger.click_on_screen(coordinate)
                time.sleep(random.randint(1, 2))
                total_follows += 1

            ScreenMeneger.scroll_on_screen(value_to_scroll=-400)
            time.sleep(random.randint(1, 2))
            print(f"total follows: {total_follows}")

        if keyboard.is_pressed("esc"):
            print("leaving app...")
            break
run()
