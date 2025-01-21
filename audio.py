import pygame

# Initialize pygame mixer for sound
pygame.mixer.init()

class BeepSoundManager:
    def __init__(self, sound_file="beep.wav"):
        """Load the beep sound."""
        try:
            self.beep_sound = pygame.mixer.Sound(sound_file)
        except pygame.error as e:
            print(f"Error loading sound file: {e}")

    def play_beep(self):
        """Play the beep sound."""
        try:
            self.beep_sound.play()
            print("Beep sound played.")
        except Exception as e:
            print(f"Error playing beep sound: {e}")
