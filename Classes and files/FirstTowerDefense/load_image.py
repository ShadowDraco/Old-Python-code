from pygame.image import load

def load_sprite(name, with_alpha=False):
    path = "Classes and files/FirstTowerDefense/assets/images/" + name + ".png"
    loaded_sprite = load(path)

    if with_alpha:
        return loaded_sprite.convert_alpha()
    else:
        return loaded_sprite.convert()