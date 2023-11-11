## goal of this fork currently
* add an option to "import" ratings using some generic field either already in beets library or in the files
    * my specific use case is having plex ratings saved to its own flexattr already and I want those written to a format usable by players. i.e. just write the plex flexattr to a new flex attr that this plugin can then write to files.     


# User rating support for Beets

The *beet userrating* plugin reads and manages a `userrating` tag on
your music files.

## Installation

Install package and scripts.

    $ pip install https://github.com/jphautin/beets-userrating/archive/master.zip

Add the plugin to beets configuration file.

```
plugins: (...) userrating
```

## Usage

    beet userrating -h
    Usage: beet userrating [options]
    Options:
     -h, --help   show this help message and exit

## FAQ

### Why not `beet rating`?

It turns out that the `mpdstats` plugin was already maintaining a
`rating` attribute.  It seemed easier to just adopt the `userrating`
nomenclature.

### What are the differences with Michael Alan Dorman repository ?

Major changes are:
- added support for WMA
- added a test suite
- add notion of scaler to be able to adapt value for any players
- add an import function (you can import rating on existing item of the library)

### Players supported

Players that are supported when importing ratings :

|           Player        | mp3 | wma | flac |
| ------------------------|-----|-----|------|
| Windows Media Player 9+ |  X  |     |      | 
| Banshee                 |  X  |     |      | 
| Media Monkey            |  X  |     |      | 
| Quod libet              |  x  |     |      | 
| Winamp                  |  x  |     |      | 


