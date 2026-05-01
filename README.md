# 👾 Alien Invasion

A classic arcade-style space shooter built with Python and Pygame, based on the project from *Python Crash Course* by Eric Matthes.

---

##  Gameplay

Control a spaceship at the bottom of the screen and shoot down waves of aliens before they reach you. Survive as long as possible and beat your high score!

---

##  Features

- Fullscreen mode
- Fleet of aliens moving and descending
- Bullet-alien collision detection
- Player lives system with HUD icons
- Difficulty selection (Easy / Medium / Hard)
- Scoreboard with real-time score display
- High score saved to JSON file
- Background music
- Increasing speed with each cleared wave

---

##  Controls

| Key | Action |
|-----|--------|
| `←` `→` | Move ship |
| `Space` | Fire bullet |
| `P` | Start / Restart game |
| `Q` | Quit |

---

##  Installation

```bash
git clone https://github.com/yourname/alien_invasion.git
cd alien_invasion
pip install -r requirements.txt
python alien_invasion.py
```

---

##  Requirements

- Python 3.12+
- Pygame

See `requirements.txt` for full list.

---

##  Project Structure

```
alien_invasion/
├── images/          # Sprites and UI icons
├── sounds/          # Background music and effects
├── alien.py         # Alien sprite class
├── alien_invasion.py # Main game loop
├── bullet.py        # Bullet sprite class
├── button.py        # UI button class
├── game_stats.py    # Game statistics
├── scoreboard.py    # Score display
├── settings.py      # Game configuration
├── ship.py          # Player ship class
├── storage.py       # High score persistence
└── high_score.json  # Saved high score
```

---

## 📖 Based On

*Python Crash Course, 3rd Edition* — Eric Matthes, No Starch Press
