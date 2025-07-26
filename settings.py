class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """"Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1366
        self.screen_height = 720
        self.bg_color = (230, 230, 230) # Setting background color

        # Ship settings
        self.ship_speed = 1.5
