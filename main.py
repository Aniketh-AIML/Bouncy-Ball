import pygame

class Game:

    def __init__(self):
   
        pygame.init()
        pygame.display.set_caption("Bouncy Ball")

        self.window = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()

        #updating the bacground
        self.background = pygame.image.load(r"C:\Users\anike\Downloads\game\resources\background_yellow.jpg")
        self.background = pygame.transform.scale(self.background, (800,600))

        #slider values
        self.paddle_x = 340
        self.paddle_y = 550
        self.paddle_width = 180
        self.paddle_height = 10
        self.paddle_speed = 25

        #values of the ball
        self.x, self.y = 300, 100 #horizontal,vertical
        self.vx, self.vy = 10,11 #speed respectively
        self.radius = 10

        #lives
        self.lives = 3

        # score
        self.score = 0
        self.font = pygame.font.SysFont("arial", 40)

        #game over screen
        self.game_over = False
        self.game_over_font = pygame.font.SysFont("Arial", 100, bold=True)
        self.score_font = pygame.font.SysFont("Arial", 28)

        #try again button
        self.button_rect = pygame.Rect(335, 380, 130, 50)
        

    def run(self):

        # running the gameloop:
        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                #restart game
                if self.game_over:

                    if event.type == pygame.MOUSEBUTTONDOWN:

                        if self.button_rect.collidepoint(event.pos):

                            # Reset game
                            self.lives = 3
                            self.score = 0

                            self.x = 300
                            self.y = 100

                            self.vx = 10
                            self.vy = 11

                            self.paddle_x = 340

                            self.game_over = False

            if not self.game_over:

                #slider press
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    self.paddle_x -= self.paddle_speed
                if keys[pygame.K_RIGHT]:
                    self.paddle_x += self.paddle_speed

                #keep it in window
                if self.paddle_x < 0:
                    self.paddle_x = 0

                if self.paddle_x + self.paddle_width > 800:
                    self.paddle_x = 800 - self.paddle_width

                # Updateing the ball
                self.x += self.vx
                self.y += self.vy
                if self.x - self.radius < 0 or self.x + self.radius > 800: self.vx = -self.vx
                if self.y - self.radius < 0: self.vy = -self.vy

                #player miss ball
                if self.y + self.radius > 600:
                    self.lives -= 1

                    self.x = 300
                    self.y = 100
                    self.vx = 10
                    self.vy = 11
                    
                #game over
                if self.lives <= 0:
                    self.game_over = True

                # interaction with ball
                if self.vy > 0 and (self.y + self.radius >= self.paddle_y
                    and self.y - self.radius <= self.paddle_y + self.paddle_height
                    and self.x + self.radius >= self.paddle_x
                    and self.x - self.radius <= self.paddle_x + self.paddle_width):

                    self.vy = -self.vy
                    self.score += 1
        
            #drawing background
            self.window.blit(self.background, (0,0))

            # Draw ball
            pygame.draw.circle(self.window, (150, 75, 0), (int(self.x), int(self.y)), self.radius)

            # draw paddlepaddle
            pygame.draw.rect(self.window,(0, 0, 0),(self.paddle_x,self.paddle_y,self.paddle_width,self.paddle_height),border_radius=10)

            #score display
            score_text = self.font.render(f"Score: {self.score}",True,(0, 0, 0))
            self.window.blit(score_text, (20, 20))

            #draw lives 
            for i in range(3):

                if i < self.lives:
                    color = (255, 0, 0)      # red heart
                else:
                    color = (150, 150, 150)  # empty/used heart

                heart = self.font.render("♥", True, color)
                self.window.blit(heart,(650 + i * 40, 20))

            # Draw the Game Over screen
            if self.game_over:

                game_over_text = self.game_over_font.render("GAME OVER",True,(255, 0, 0))

                final_score_text = self.score_font.render(f"Final Score: {self.score}",True,(0, 0, 0))

                pygame.draw.rect(self.window,(0, 0, 0),self.button_rect,border_radius=10)

                button_font = pygame.font.SysFont("Arial", 26)
                button_text = button_font.render("Try Again",True,(255, 255, 255))

                game_over_rect = game_over_text.get_rect(center=(400, 250))
                self.window.blit(game_over_text, game_over_rect)
                
                score_rect = final_score_text.get_rect(center=(400, 350))
                self.window.blit(final_score_text, score_rect)

                button_text_rect = button_text.get_rect(center=self.button_rect.center)
                self.window.blit(button_text, button_text_rect)


            # Show everything
            pygame.display.flip()
            self.clock.tick(60)



if __name__ == '__main__':
    Game().run()