<div align="center">

![](.media/icon-128x128_round.png)

# `steamleaderboards`

Retrieve and parse Steam leaderboards

</div>

## Links

[![PyPI](https://img.shields.io/pypi/v/steamleaderboards)](https://pypi.org/project/steamleaderboards)

## History

It was created with the Isaac Daily Run scoreboards in mind, but it can be used for other games that have a public leaderboard as well.

## Usage

### In code

To use `steamleaderboards`, first install it via PyPI:

```console
$ # If you're using pip in a venv on 
$ .venv/bin/pip install steamleaderboards --upgrade
```

```console
$ # If you're using poetry 
$ poetry add steamleaderboards
```

Then, create a `LeaderboardGroup` for the desired game.

```python
import steamleaderboards as sl
lbgroup = sl.LeaderboardGroup(STEAM_APP_ID)
```

Once you have created the `LeaderboardGroup`, you can retrieve the desired leaderboards by using the `LeaderboardGroup.get` method.  
You can specify the name, the display name or the id of the leaderboard to retrieve.

```python
leaderboard_a = lbgroup.get(name=LEADERBOARD_NAME)
leaderboard_b = lbgroup.get(lbid=LEADERBOARD_ID)
leaderboard_c = lbgroup.get(display_name=LEADERBOARD_DISPLAY_NAME)
```

When you have the `Leaderboard` object, you can find all the entries in the `Leaderboard.entries` field, or you can search for a specific one through the `Leaderboard.find_entry` method.

```python
all_scores = leaderboard_a.entries
my_score = leaderboard_a.find_entry(MY_STEAMID_1)
first_place_score = leaderboard_a.find_entry(rank=1)
last_place_score = leaderboard_a.find_entry(rank=-1)
```

### In the terminal

To use `steamleaderboards`, first install it via PyPI:

```console
$ # Using pipx
$ pipx install steamleaderboards
```

Then, you can use it to retrieve leaderboards for one or more Steam games via the terminal:

```console
$ steamleaderboards --output_dir="./data" 440
```

This will download all leaderboards for Team Fortress 2, the game with the app id `440`, to the `./data` directory.

App ids for games can be found via [SteamDB](https://steamdb.info/).
