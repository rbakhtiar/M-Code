M- Syntax Specification

M- Programming Language — Technical Syntax Reference

Version: 0.1
Status: Early Development

---

1. Introduction

M- is a programming language designed around simple, readable syntax.

This document defines the syntax and behavior of M- 0.1.

The M- interpreter is currently implemented in Python through "m.py".

M- source files use the ".m" file extension.

Example:

program.m

---

2. Basic Structure

An M- program consists of one or more statements.

Example:

Save name = "Lionel Messi"
Save goals = 900

Write(name)
Write(goals)

Each statement normally occupies its own line.

Blank lines are allowed.

---

3. Comments

Comments begin with "#".

Everything after "#" on that line is ignored by the interpreter.

Example:

# This is a comment

Save name = "Messi"

# Display the name
Write(name)

Comments do not affect program execution.

---

4. Variables

4.1 Creating Variables

Variables are created using the "Save" keyword.

Syntax:

Save variable = value

Example:

Save name = "Lionel Messi"
Save goals = 900
Save age = 39

---

4.2 Variable Names

Variable names should:

- Start with a letter.
- Contain letters, numbers, or underscores.
- Not contain spaces.
- Not be a reserved M- keyword.

Valid:

Save name = "Messi"
Save player_name = "Messi"
Save goals2026 = 10

Invalid:

Save player name = "Messi"

---

5. Data Types

M- 0.1 supports basic values.

5.1 Strings

Strings contain text surrounded by double quotation marks.

Example:

Save name = "Lionel Messi"
Save team = "FC Barcelona"

Strings can be displayed using "Write()".

Write(name)

---

5.2 Integers

Whole numbers can be stored directly.

Example:

Save goals = 900
Save age = 39

---

6. Output

M- uses the "Write()" function to display information.

Syntax:

Write(value)

Examples:

Write("Hello!")
Write(name)
Write(goals)

Output:

Hello!
Lionel Messi
900

---

7. String Output

Text can be written directly inside "Write()".

Example:

Write("Welcome to M-!")

Output:

Welcome to M-!

---

8. Using Variables in Output

A variable can be passed directly to "Write()".

Example:

Save name = "Lionel Messi"

Write(name)

Output:

Lionel Messi

---

9. Input

User input is planned for a future version of M-.

The intended syntax is:

Write(Enter your name)

The exact input behavior is not part of the stable M- 0.1 specification yet.

Do not assume input functionality is available unless implemented by the current interpreter.

---

10. Operators

Basic mathematical and comparison operators are planned for future versions.

Planned operators include:

+
-
*
/
>
<
>=
<=
==
!=

Example of planned syntax:

Save total = 50 + 25

Operator support is currently under development.

---

11. Conditional Statements

Conditional statements are planned for M- 0.2.

The planned syntax is:

If score > 10 {
    Write("You win!")
}

An alternative condition can use "Else":

If score > 10 {
    Write("You win!")
}
Else {
    Write("Try again!")
}

This syntax is planned and is not guaranteed to work in M- 0.1.

---

12. Loops

Loops are planned for a future version.

The planned "Repeat" syntax is:

Repeat 10 {
    Write("M-")
}

This would execute the code inside the block 10 times.

---

13. Functions

Functions are planned for a future version.

Planned syntax:

Function greet(name) {
    Write("Hello " + name)
}

A function could later be called using:

greet("Harry")

Function behavior is not currently implemented in M- 0.1.

---

14. Code Blocks

Future M- versions will use "{" and "}" to define blocks of code.

Example:

If score > 10 {
    Write("Winner")
}

The opening "{" begins a block.

The closing "}" ends a block.

---

15. Reserved Keywords

The following keywords are reserved or planned for M-:

Save
Write
If
Else
Repeat
While
Function
Return
Game
Player
Ball

Additional keywords may be added in future versions.

---

16. File Structure

A basic M- project can contain:

M-Code/
│
├── m.py
├── program.m
├── README.md
│
└── docs/
    └── syntax.md

---

17. Interpreter

The current M- interpreter is:

m.py

Its job is to:

1. Read an M- source file.
2. Process each statement.
3. Identify M- commands.
4. Store variables.
5. Execute supported commands.
6. Display errors when unsupported syntax is encountered.

---

18. Error Handling

M- should provide readable errors.

Example:

M- Error: Unknown command

For an invalid "Save" statement:

M- Error: Save needs '='

Future versions should provide more detailed errors, including:

- Line number
- Error type
- Invalid syntax
- Suggested correction

Example planned error:

M- Error on line 5:
Unknown command "Wrtie"

Did you mean "Write"?

---

19. Syntax Philosophy

M- is designed around several principles:

Readability

Code should be understandable without extensive programming experience.

Simplicity

Common operations should use simple keywords.

Consistency

M- commands should follow consistent syntax.

Extensibility

The language should be capable of expanding into more advanced areas.

Cross-Platform Development

The long-term goal is for M- programs to work across multiple platforms.

---

20. Future M- Systems

The long-term M- ecosystem may include:

M- Language
    │
    ├── M- Interpreter
    ├── M- Compiler
    ├── M- Standard Library
    ├── M- Package Manager
    ├── M- IDE
    ├── M- Game Engine
    └── M- SDK

---

21. Game Development

Game development is planned for a future version of M-.

Potential syntax:

Game.Start("M-Pong")

Player.Create("Left")
Player.Create("Right")

Ball.Create()

Game.Run()

Potential future commands may include:

Game.Start()
Game.Run()
Game.Stop()

Player.Create()
Player.Move()

Ball.Create()
Ball.Move()
Ball.Bounce()

Score.Set()
Score.Add()

These commands are not currently supported in M- 0.1.

They are part of the future M- game-development specification.

---

22. Versioning

M- uses semantic-style versioning.

Example:

M- 0.1
M- 0.2
M- 0.3
M- 1.0

Major versions may introduce significant language changes.

Minor versions may introduce new functionality.

Patch versions may contain bug fixes.

---

23. Compatibility

Programs should be written according to the syntax supported by their M- version.

Example:

M- 0.1

means the program targets M- 0.1.

Future versions may introduce syntax that does not exist in older versions.

---

24. Current M- 0.1 Feature Set

Currently supported:

Save
Write()
Strings
Integers
Variables
Comments

Currently under development:

Input
Math
If
Else
Loops
Functions

Future:

Files
Networking
GUI
Games
AI
Web
System programming
Cross-platform compilation

---

25. Official Example

A complete M- 0.1 program:

# M- 0.1 Example

Save name = "Lionel Messi"
Save team = "FC Barcelona"
Save goals = 900

Write("Welcome to M-!")
Write(name)
Write(team)
Write(goals)

Expected output:

Welcome to M-!
Lionel Messi
FC Barcelona
900

---

26. Specification Status

This document describes M- 0.1.

M- is actively being developed.

Syntax marked as planned, future, or under development should not be considered part of the stable M- 0.1 language.

The specification will be updated as new M- features are implemented.
