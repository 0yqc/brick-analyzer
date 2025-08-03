# brick-analyzer
analyzes brick purchases before buying to see if their worth it.

## Install

1. Clone this repository using `git clone https://github.com/0yqc/brick-analyzer`
	- You need `git` installed for this to work, install using `sudo apt install git`.
2. change your current working directory using `cd ./brick-analyzer`
3. Set your Rebrickable API key in `./rb_api_key.txt`
	- To get your API key, create a or login to your [Rebrickable](https://rebrickable.com/) account and get it vis the API settings.

### Dependencies

dependencies needed:
- CurrencyConverter, install via:
	1. `pip`
		- Run `pip install --user currencyconverter`
    2. from source
		- Clone the repo using `git clone https://github.com/alexprengere/currencyconverter.git`
        - Change your working directory using `cd ./currencyconverter/`
        - Install via `python ./setup.py install --user`

### Run

to run, simply change your working directory to the repo of brick-analyzer, then run `python ./main.py`

### Help

If you need help with the installation or setup process, reach out to me at [0yqc@duck.com](mailto:0yqc@duck.com?subject=Brick%20Analyzer%20-%20Installation%20Help)

## Features

It will fetch different data to see if this deal is a good deal, currently this data is already being fetched to compare with:
- BrickLink Part Out Value, average price of the parts in this set when selling them
- BrickLink Price Guide, average price of whole sets sold on BrickLink