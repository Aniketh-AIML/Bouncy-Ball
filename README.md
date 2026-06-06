# Bouncy Ball Game

A simple arcade-style bouncing ball game built with Python and Pygame.

## Features

* Smooth ball physics and wall collisions
* Player-controlled paddle
* Real-time collision detection
* Score tracking system
* Persistent high score saving
* Lives system with visual heart indicators
* Progressive difficulty scaling
* Dynamic ball speed progression
* Sound effects for paddle hits, wall bounces, scoring, life loss, and game over
* Press SPACE to start gameplay
* Game over screen with restart button
* Multiple background themes
* Clean modular project structure
* 60 FPS smooth gameplay

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
│   ├── __init__.py
│   ├── ball.py
│   └── paddle.py
│
├── utils/
│   ├── __init__.py
│   ├── assets.py
│   ├── sounds.py
│   └── highscore.py
│
├── resources/
│   ├── backgrounds/
│   │   ├── background_blue.jpg
│   │   ├── background_brown.jpg
│   │   └── background_yellow.jpg
│   │
│   ├── sound_effects/
│   │   ├── paddle_hit.mp3
│   │   ├── wall_hit.mp3
│   │   ├── loose_heart.mp3
│   │   ├── score_up.mp3
│   │   └── game_over.mp3
│   │
│   └── highscore.txt
│
├── game.py
├── settings.py
├── main.py
├── README.md
└── .gitignore
```

## Future Improvements

* Particle Effects
* Pause mechanic 
* levels

## Added Features

* Difficulty progression
* Game over screen
* Score system
* Sound effects
* High Score Saving
