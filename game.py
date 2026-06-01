import pygame

from settings import *
from entities.ball import Ball
from entities.paddle import Paddle
from utils.assets import load_background


class Game:

    def __init__(self):

        pygame.init()
        pygame.display.set_caption("Bouncy Ball")

        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.background = load_background()

        self.paddle = Paddle()
        self.ball = Ball()

        self.lives = START_LIVES
        self.score = 0

        self.font = pygame.font.SysFont("arial", 40)

        self.game_over = False
        self.game_over_font = pygame.font.SysFont("Arial", 100, bold=True)
        self.score_font = pygame.font.SysFont("Arial", 28)

        self.button_rect = pygame.Rect(335, 380, 130, 50)

    def run(self):

        while True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if self.game_over:

                    if event.type == pygame.MOUSEBUTTONDOWN:

                        if self.button_rect.collidepoint(event.pos):

                            self.lives = START_LIVES
                            self.score = 0

                            self.ball.reset()

                            self.paddle.x = 340

                            self.game_over = False

            if not self.game_over:

                self.paddle.move()

                self.ball.update()

                # Paddle collision
                if (
                    self.ball.vy > 0
                    and self.ball.y + self.ball.radius >= self.paddle.y
                    and self.ball.y - self.ball.radius <= self.paddle.y + self.paddle.height
                    and self.ball.x + self.ball.radius >= self.paddle.x
                    and self.ball.x - self.ball.radius <= self.paddle.x + self.paddle.width
                ):

                    self.ball.vy = -self.ball.vy

                    self.score += 1

                    # Every 5 hits increase speed
                    if self.score % 5 == 0:
                        self.ball.increase_speed()

                # Ball missed
                if self.ball.y + self.ball.radius > HEIGHT:

                    self.lives -= 1

                    self.ball.reset()

                # Game Over
                if self.lives <= 0:
                    self.game_over = True

            # Background
            self.window.blit(self.background, (0, 0))

            # Ball
            self.ball.draw(self.window)

            # Paddle
            self.paddle.draw(self.window)

            # Score
            score_text = self.font.render(f"Score: {self.score}",True,(0, 0, 0))

            #testing
            #speed_text = self.font.render(f"Speed: {abs(self.ball.vx):.1f}",True,(0, 0, 0))

            self.window.blit(score_text, (20, 20))

            #testing
            #self.window.blit(speed_text, (20, 70))

            # Lives
            for i in range(3):

                if i < self.lives:
                    color = (255, 0, 0)
                else:
                    color = (150, 150, 150)

                heart = self.font.render("♥", True, color)

                self.window.blit(heart,(650 + i * 40, 20))

            # Game Over Screen
            if self.game_over:

                game_over_text = self.game_over_font.render("GAME OVER",True,(255, 0, 0))

                final_score_text = self.score_font.render(f"Final Score: {self.score}",True,(0, 0, 0))

                pygame.draw.rect(self.window,(0, 0, 0),self.button_rect,border_radius=10)

                button_font = pygame.font.SysFont("Arial", 26)

                button_text = button_font.render("Try Again",True,(255, 255, 255))

                game_over_rect = game_over_text.get_rect(center=(400, 250))

                self.window.blit(game_over_text,game_over_rect)

                score_rect = final_score_text.get_rect(center=(400, 350))

                self.window.blit(final_score_text,score_rect)

                button_text_rect = button_text.get_rect(center=self.button_rect.center)

                self.window.blit(button_text,button_text_rect)

            pygame.display.flip()
            self.clock.tick(FPS)