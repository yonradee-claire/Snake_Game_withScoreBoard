# Snake_Game_with_ScoreBoard

Classic Snake Game with Scoreboard (using Python module "Turtle")
A simple Snake Game built using Python’s turtle graphics library, with an added scoreboard feature to track the current scores and highest scores.
----------------------------------------------------

Features:
- Control the snake using keyboard arrow keys
- Keep track of the current score and highest score
- Press Spacebar to pause/resume the game
- Simple collision detection and automatic game reset when the snake collides with itself
- Fully object-oriented design (Snake class & Scoreboard class)

How the game works:
- Creates a snake made of 3 square turtle segments. Each segment follows the previous one when the snake moves
- The snake's head can change direction using arrow keys
- A method add_seg() allows the snake to grow after eating food by adding new segments to the tail
- The game keeps track of the current score and highest score

How to Run the Game
1. Install Python
2. Clone this repository or download all the .py files.
3. Run main.py file
----------------------------------------------------

What This Project Demonstrates
- Python OOP: Custom classes with inheritance (Scoreboard inherits from Turtle)
- GUI Programming: Interactive graphics with the turtle module
- Event Handling: Real-time keyboard control
- Basic Game Loop Logic
