# Unit Converter

Program capable of converting between a series of units, from mass, temperature, volume, ditance or currencies.

## Instructions

### Requirements

For the complete operation of this program a [Fixer.io](fixer.io) account is required, as well as its API Key. Python 3 is also required.

### Configuration

For the currency exchange function a config.json file needs to be on the same folder as the program with the following field:

* "key" - In here the API Key needs to be inserted

### Usage

To launch the program just type:

```sh
python3 unit_converter.py
```

Following the prompts, fistly the program will request what type of unit will be converted:

>"What type of unit you would like to convert? [M]ass [T]emperature, [L]ength, [V]olume or [C]urrency?"

Throughout the program options can be chosen by just selecting the letter highlighted and hitting Enter.
