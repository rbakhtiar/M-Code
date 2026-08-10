# M- Game Development Specification

Version: 1.0

## Purpose

The M- Game API provides syntax for creating 2D games.

The first target game is Pong.

---

# Game

## Game.Start()

Creates and starts a game window.

Syntax:

Game.Start("Game Name")

Example:

Game.Start("M-Pong")

---

## Game.Run()

Starts the game loop.

Syntax:

Game.Run()

---

## Game.Stop()

Stops the game.

Syntax:

Game.Stop()

---

# Window

## Window.Size()

Sets the game window size.

Syntax:

Window.Size(width, height)

Example:

Window.Size(800, 600)

---

## Window.Title()

Sets the window title.

Syntax:

Window.Title("M-Pong")

---

# Player

## Player.Create()

Creates a player.

Syntax:

Player.Create("name")

Example:

Player.Create("Left")
Player.Create("Right")

---

## Player.Position()

Sets the player's position.

Syntax:

Player.Position("name", x, y)

Example:

Player.Position("Left", 40, 250)

---

## Player.Size()

Sets the player's dimensions.

Syntax:

Player.Size("name", width, height)

Example:

Player.Size("Left", 20, 100)

---

## Player.Speed()

Sets player movement speed.

Syntax:

Player.Speed("name", speed)

Example:

Player.Speed("Left", 7)

---

## Player.Move()

Moves a player.

Syntax:

Player.Move("name", direction)

Directions:

Up
Down
Left
Right

Example:

Player.Move("Left", Up)

---

# Keyboard

## Key.Bind()

Connects a keyboard key to an action.

Syntax:

Key.Bind("key", action)

Example:

Key.Bind("W", Player.Move("Left", Up))
Key.Bind("S", Player.Move("Left", Down))

---

# Ball

## Ball.Create()

Creates a ball.

Syntax:

Ball.Create("name")

Example:

Ball.Create("Ball")

---

## Ball.Position()

Sets the ball position.

Syntax:

Ball.Position("name", x, y)

Example:

Ball.Position("Ball", 400, 300)

---

## Ball.Size()

Sets the ball size.

Syntax:

Ball.Size("name", size)

Example:

Ball.Size("Ball", 15)

---

## Ball.Speed()

Sets the ball speed.

Syntax:

Ball.Speed("name", speed)

Example:

Ball.Speed("Ball", 8)

---

## Ball.Bounce()

Makes the ball bounce from a surface.

Syntax:

Ball.Bounce("name", surface)

Example:

Ball.Bounce("Ball", Wall)

---

# Collision

## Collision.Enable()

Enables collision detection.

Syntax:

Collision.Enable(object1, object2)

Example:

Collision.Enable("Ball", "Left")
Collision.Enable("Ball", "Right")

---

# Score

## Score.Create()

Creates a score.

Syntax:

Score.Create("name")

Example:

Score.Create("Left")
Score.Create("Right")

---

## Score.Add()

Adds points.

Syntax:

Score.Add("name", amount)

Example:

Score.Add("Left", 1)

---

## Score.Display()

Displays a score.

Syntax:

Score.Display("name", x, y)

Example:

Score.Display("Left", 300, 30)

---

# M-Pong Example

A complete M-Pong program should eventually look like:

Game.Start("M-Pong")

Window.Size(800, 600)
Window.Title("M-Pong")

Player.Create("Left")
Player.Create("Right")

Player.Position("Left", 40, 250)
Player.Position("Right", 740, 250)

Player.Size("Left", 20, 100)
Player.Size("Right", 20, 100)

Player.Speed("Left", 7)
Player.Speed("Right", 7)

Ball.Create("Ball")
Ball.Position("Ball", 400, 300)
Ball.Size("Ball", 15)
Ball.Speed("Ball", 8)

Collision.Enable("Ball", "Left")
Collision.Enable("Ball", "Right")

Score.Create("Left")
Score.Create("Right")

Score.Display("Left", 300, 30)
Score.Display("Right", 500, 30)

Game.Run()
