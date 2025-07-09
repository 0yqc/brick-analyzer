# brick-analyzer
analyzes brick purchases before buying to see if their worth it.

## Install

1. Clone this repository using `git clone https://github.com/0yqc/brick-analyzer`
	- You need `git` installed for this to work, install using `sudo apt install git`.
2. change your current working directory using `cd ./brick-analyzer`
3. Set your Rebrickable API key in `./rb_api_key.txt`
4. Run the script in a terminal using `python ./main.py`

## Features

It will fetch different data to see if this deal is a good deal, currently this data is already being fetched to compare with:
- BrickLink Part Out Value, average price of the parts in this set when selling them
- BrickLink Price Guide, average price of whole sets sold on BrickLink