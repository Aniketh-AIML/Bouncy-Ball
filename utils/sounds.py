import pygame


class SoundManager:

    def __init__(self):

        pygame.mixer.init()

        self.paddle_hit = pygame.mixer.Sound("resources/sound_effects/paddle_hit.mp3")

        self.wall_hit = pygame.mixer.Sound("resources/sound_effects/wall_hit.mp3")

        self.loose_heart = pygame.mixer.Sound("resources/sound_effects/loose_heart.mp3")

        self.score_up = pygame.mixer.Sound("resources/sound_effects/score_up.mp3")

        self.game_over = pygame.mixer.Sound("resources/sound_effects/game_over.mp3")

        # Volume balancing

        self.wall_hit.set_volume(0.25)

        self.paddle_hit.set_volume(0.45)

        self.loose_heart.set_volume(0.45)

        self.score_up.set_volume(0.60)

        self.game_over.set_volume(0.70)

    def play_wall_hit(self):
        self.wall_hit.play()

    def play_paddle_hit(self):
        self.paddle_hit.play()

    def play_loose_heart(self):
        self.loose_heart.play()

    def play_score_up(self):
        self.score_up.play()

    def play_game_over(self):
        self.game_over.play()