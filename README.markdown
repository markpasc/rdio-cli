# rdio-cli #

`rdio-cli` is a command line application for controlling some Rdio API functions.

Currently it supports listing your playlists and shuffling a playlist.


## Installation ##

Install it as any other Python program:

    $ python setup.py install

If you don't want to install its dependencies to your system, try installing it in a [virtual environment](http://www.virtualenv.org/). As the Rdio client library is distributed as an egg, installing it with `pip` doesn't work. You can manually install [the `rdio` dependency from github](https://github.com/rdio/rdio-python) if you must use `pip`.


## Configuring ##

First, you'll need a Rdio API key. You can [register and create a key at developer.rdio.com](http://developer.rdio.com/). Once you have a key, run the `configure` command:

    $ rdio configure
    Consumer token: urjECXo8luFeEKw1NrjioUbd
    Consumer secret: b0PZPLO9hb
    Open this URL in your web browser to get an API PIN:

         https://www.rdio.com/oauth/authorize?oauth_token=FGTgBlc5lLylBrOgWA37l4zP

    PIN: 7496
    Last.fm API key (optional):
    Configured!

This saves an OAuth access token to your home directory in an `.rdio` file, so take care with it! Subsequent commands then use that access token to authenticate, so you need only configure the keys once.


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

    $ rdio search moby sky is broken
    +--------------------+---------------------------+-------------------+----------+
    |       Track        |           Album           |       Artist      |   Key    |
    +--------------------+---------------------------+-------------------+----------+
    | The Sky Is Broken  | Replay: A Tribute To Moby | Aleister Einstein | t1350373 |
    | Sky Is Broken, The | Play                      | Moby              | t2496501 |
    +--------------------+---------------------------+-------------------+----------+

    $ rdio configure
    Last.fm API key (optional): va2SLf3lpGwEKYPxOW1DRKp6YzPhHiK4
    Configured!

    $ bin/rdio improvise t2496501
    WARNING:root:Can't stream If Things Were Perfect by Moby from Rdio, skipping
    WARNING:root:Can't stream My Weakness by Moby from Rdio, skipping
    WARNING:root:Couldn't find Turquoise Hexagon Sun by Boards of Canada on Rdio
    100% |#######################################################################################################|
    Playlist improvised into http://rd.io/x/QV5FbjNehwk

    $
