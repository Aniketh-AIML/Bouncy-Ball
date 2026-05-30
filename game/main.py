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
        

    def run(self):

        # running the gameloop:
        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

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
            if self.y - self.radius < 0 or self.y + self.radius > 600: self.vy = -self.vy


            # interaction with ball
            if self.vy > 0 and (
                self.y + self.radius >= self.paddle_y
                and self.y - self.radius <= self.paddle_y + self.paddle_height
                and self.x + self.radius >= self.paddle_x
                and self.x - self.radius <= self.paddle_x + self.paddle_width):self.vy = -self.vy
            
            

                    
            #drawing background
            self.window.blit(self.background, (0,0))

            # Draw ball
            pygame.draw.circle(self.window, (150, 75, 0), (int(self.x), int(self.y)), self.radius)

            # draw paddlepaddle
            pygame.draw.rect(self.window,(0, 0, 0),(self.paddle_x,self.paddle_y,self.paddle_width,self.paddle_height),border_radius=10)

           
            # Show everything
            pygame.display.flip()
            self.clock.tick(60)



if __name__ == '__main__':
    Game().run()