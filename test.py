import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

x, y = 300, 10
vx, vy = 500,600
radius = 10


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Update
    x += vx
    y += vy
    if x - radius < 0 or x + radius > 800: vx = -vx
    if y - radius < 0 or y + radius > 600: vy = -vy

    # Draw
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 200, 50), (int(x), int(y)), radius)
    pygame.display.flip()
    clock.tick(60)









# import pygame
# import sys

# # Initialize Pygame
# pygame.init()

# # Setup display
# WIDTH, HEIGHT = 800, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Pygame Slider Example")

# # Colors and Background
# # Pre-loading a sky blue color as requested
# SKY_BLUE = (135, 206, 235)

# # Load Slider Assets
# # NOTE: You must crop the generated image into two files:
# # 1. 'slider_track.png' (the grey bar)
# # 2. 'slider_handle.png' (the orange knob)
# try:
#     track_img = pygame.image.load('slider_track.png').convert_alpha()
#     handle_img = pygame.image.load('slider_handle.png').convert_alpha()
# except pygame.error:
#     print("Please crop the generated image into 'slider_track.png' and 'slider_handle.png'")
#     sys.exit()

# # Slider Configuration
# # Position the track in the center-bottom of the screen
# track_rect = track_img.get_rect(center=(WIDTH // 2, HEIGHT - 100))

# # Define the boundaries for handle movement
# SLIDER_MIN_X = track_rect.left + 20 # Slight offset from the edge
# SLIDER_MAX_X = track_rect.right - 20
# SLIDER_Y = track_rect.centery

# # Initialize handle position
# handle_rect = handle_img.get_rect(center=(SLIDER_MIN_X, SLIDER_Y))

# # Game loop variables
# is_dragging = False
# current_value = 0.0 # Normalized value between 0.0 and 1.0

# # Main Game Loop
# running = True
# while running:
#     # 1. Event Handling
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
            
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             if event.button == 1: # Left click
#                 if handle_rect.collidepoint(event.pos):
#                     is_dragging = True
                    
#         elif event.type == pygame.MOUSEBUTTONUP:
#             if event.button == 1: # Left click release
#                 is_dragging = False
                
#         elif event.type == pygame.MOUSEMOTION:
#             if is_dragging:
#                 # Update handle position based on mouse X, clamped within boundaries
#                 new_x = max(SLIDER_MIN_X, min(event.pos[0], SLIDER_MAX_X))
#                 handle_rect.centerx = new_x
                
#                 # Calculate normalized value (0.0 to 1.0) for game logic
#                 total_length = SLIDER_MAX_X - SLIDER_MIN_X
#                 current_position = new_x - SLIDER_MIN_X
#                 current_value = current_position / total_length
                
#     # 2. Game Logic
#     # (Use current_value to update game state, e.g., paddle speed)

#     # 3. Drawing
#     screen.fill(SKY_BLUE) # Fill background
    
#     # Draw slider components
#     screen.blit(track_img, track_rect)
#     screen.blit(handle_img, handle_rect)
    
#     # Optional: Display value for debugging
#     font = pygame.font.Font(None, 36)
#     value_text = font.render(f"Value: {current_value:.2f}", True, (0, 0, 0))
#     screen.blit(value_text, (20, 20))

#     pygame.display.flip()

# pygame.quit()
# sys.exit()