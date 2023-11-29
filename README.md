# pokemon-team-api

The purpose of this project is to experiment with sending 'GET' request to public APIs
to retrieve the necessary required data for our script.

In this case, we are creating a list of our favourite Pokémon characters and iterating
that list and constructing the necessary URL to be fetched. For that data to then list:

- Name
- Type
- Abilities
- Weight
- Height

The list of Pokémon can be as lenghty as you wish for it to be, but with 'import random'
module being within the code, it will only sample six Pokémon from that list. The sample
can be increased or reduced, dependent on your desired field. However, to be considerate
to the function costs of the API, it has been kept minimal.

All that is required for the code to work, is for you to have a working Python environment
with `pip` installed, to install the necessary package dependencies. In this case, we are
only using one package and that is 'requests' so that the correct instructions can be
sent to the API.

### Instructions

Navigate to your desired location on your system to `git pull` the repository.

Once there, you can perform the following steps:

```
# This collects this repository and downloads it to your system.
https://github.com/leepatrickworrall/pokemon-team-api.git

# Install the necessary dependencies.
pip install -r requirements.txt
```

Alternatively, if you are using Windows, Mac, or Linux, you can install the `requests` 
module manually by doing:

```
pip install requests
```

Or,

```
pip3 install requests
```

If you don't wish to alter the 'fav-pokemon.txt' list file, you can simply just open
up your terminal or shell window and type:

```
python main.py
```

Or again, dependent on the system you are using:

```
python3 main.py
```

### Additional Information

If there are any issues with this project, feel free to let me know, and the credits go
to Paul Hallett and other PokéAPI contributors around the world for making this API
be possible.

If you would like to access additional date using PokéAPI, you can do by going to:
https://pokeapi.co/