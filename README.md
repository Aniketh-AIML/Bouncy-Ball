# Bouncy Ball Game

A simple arcade-style bouncing ball game built with Python and Pygame.

## Features

* Smooth ball physics and wall collisions
* Player-controlled paddle
* Real-time collision detection
* Score tracking system
* Lives system with heart display
* Difficulty progression (ball speed increases over time)
* Sound effects for gameplay events
* Press SPACE to start gameplay
* Game over screen with restart button
* Custom game background
* 60 FPS gameplay

## Technologies Used

* Python
* Pygame

## How to Run

```bash
pip install pygame
python main.py
```

## Controls

* Left Arrow: Move paddle left
* Right Arrow: Move paddle right

## Project Structure

```text
game/
│
├── entities/
│   ├── ball.py
│   └── paddle.py
│
├── utils/
│   ├── assets.py
│   └── sounds.py
│
├── resources/
│   ├── background_yellow.jpg
│   └── sound_effects/
│       ├── paddle_hit.mp3
│       ├── wall_hit.mp3
│       ├── loose_heart.mp3
│       ├── score_up.mp3
│       └── game_over.mp3
│
├── game.py
├── settings.py
├── main.py
└── README.md
```

## Future Improvements

* High Score Saving
* Particle Effects

## Added Features

* Difficulty progression
* Game over screen
* Score system
* Sound effects
