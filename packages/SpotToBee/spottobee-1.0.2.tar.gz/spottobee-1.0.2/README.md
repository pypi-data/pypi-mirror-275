# SpotToBee
SpotToBee is a command-line tool for converting Spotify and other CSV playlists to XML format. Fetching data from Spotify requires SpotifyClient Credentials from https://developer.spotify.com/dashboard. The tool can be used without credentials alongside https://exportify.net/. 

## Installation

    pip install SpotToBee

Running SpotToBee will automatically create a config file in its run directory. This can be manually reset by passing the --reconfigure argument.
## Usage/Examples

    SpotToBee path/to/playlist.csv

    SpotToBee https://open.spotify.com/playlist/37i9dQZF1DX9wa6XirBPv8

    SpotToBee path/to/playlist.csv --config path/to/config.ini

    SpotToBee --reconfigure

## License

[MIT](https://choosealicense.com/licenses/mit/)

