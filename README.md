## Welcome to my rock-paper-scissors game. Follow the instructions below to play.

## Setup

Create a virtual environment:

```sh
conda create -n RPS-game python=3.8
```

Activate the virtual environment:

```sh
conda activate RPS-game
```

Install package dependencies (mainly for testing):

```sh
pip install -r requirements.txt
```

## Usage

Run the rock paper scissors game:
The user can enter his or her username. "Jon Snow" is the example where the user would type. Remember to include quotes around the username.


```sh
PLAYER_NAME="Jon Snow" python game.py
```

Or, the user can use the default username:

```sh
python game.py
```

## Testing

To run tests using Pytest:

```sh
pytest
```
