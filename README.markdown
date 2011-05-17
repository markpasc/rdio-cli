# rdio-cli #

`rdio-cli` is a command line application for controlling some Rdio API functions. It can:

* search Rdio for tracks, albums, and artists
* show you tracks, albums, and artists by key (Rdio ID)
* list your playlists
* sort or shuffle a playlist
* create a new playlist based on a song (using the Echo Nest API)


## Installation ##

Install it as any other Python program:

    $ python setup.py install

If you don't want to install its dependencies system-wide, try installing it in a [virtual environment](http://www.virtualenv.org/). As the Rdio client library is distributed as an egg, installing it with `pip` doesn't work. You can manually install [the `rdio` dependency from github](https://github.com/rdio/rdio-python) if you must use `pip`.


## Configuring ##

First, you'll need a Rdio API key. You can [register and create a key at developer.rdio.com](http://developer.rdio.com/). Once you have a key, run the `configure` command:

    $ rdio configure
    Consumer token: urjECXo8luFeEKw1NrjioUbd
    Consumer secret: b0PZPLO9hb
    Open this URL in your web browser to get an API PIN:

         https://www.rdio.com/oauth/authorize?oauth_token=FGTgBlc5lLylBrOgWA37l4zP

    PIN: 7496
    Echo Nest API key (optional):
    Configured!

This saves an OAuth access token to your home directory in an `.rdio` file, so take care with it! Subsequent commands then use that access token to authenticate, so you need only configure the keys once.

As the Echo Nest API is only used with the `improvise` command, you only need to supply one to use that command. Sign up on [the Echo Nest developer site](http://developer.echonest.com/) to get an Echo Nest API key.


## Usage ##

See `rdio --help` for supported commands.

    $ rdio playlists 
    +--------------------------------------------------------------+--------------------+--------------+---------+
    |                             Name                             |       Owner        | Relationship |   Key   |
    +--------------------------------------------------------------+--------------------+--------------+---------+
    | ska                                                          | Mark Paschal       | Owner        | p113050 |
    | Minimix: Cervidae and their predators                        | Mark Paschal       | Owner        | p47494  |
    | Minimix: BBC Sound of 2009                                   | Mark Paschal       | Owner        | p18363  |
    | Like!                                                        | Masayoshi Sekimura | Subscriber   | p66901  |
    | 2010                                                         | Andre Torrez       | Subscriber   | p6557   |
    +--------------------------------------------------------------+--------------------+--------------+---------+

    $ rdio shuffle p113050
    100% |#######################################################################################################|

    $ rdio search moby south side
    +----------------------------------------+----------------------------+----------+----------+
    |                 Track                  |           Album            |  Artist  |   Key    |
    +----------------------------------------+----------------------------+----------+----------+
    | South side                             | Go - The Very Best of Moby | Moby     | t4104950 |
    | South Side (Pete Heller Park Lane Dub) | Go - The Very Best of Moby | Moby     | t4105406 |
    | South Side                             | Replay: A Tribute To Moby  | Tre' Lux | t1350298 |
    | South Side                             | Play                       | Moby     | t2495635 |
    +----------------------------------------+----------------------------+----------+----------+

    $ rdio configure
    Echo Nest API key (optional): va2SLf3lpGwEKYPxO
    Configured!

    $ rdio improvise t4104950
    100% |#######################################################################################################|
    Playlist improvised into http://rd.io/x/QV5FbjNes9U

    $
