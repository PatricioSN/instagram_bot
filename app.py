from screen_meneger import ScreenMeneger


def run():
    while True:
        coordinates = ScreenMeneger.get_all_matches_by_image(image_to_search=r".\foxy.png")
        for coordinate in coordinates:
            print(coordinate)


run()