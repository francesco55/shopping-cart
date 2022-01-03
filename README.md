# shopping-cart Project

The purpose of the given code is to act as a sort of register which produces a receipt of ordered items.

## Installation

To install all necessary documents: fork this repository, clone your fork and download it onto your computer. Navigate to the files from the command-line with the given code.

```sh
cd ~/Documents/GitHub/shopping-cart
```

## Set Up

### Conda Environment

In order for the code to run correctly, the environment in which the code runs in must be set up.

First, set up a conda environment:

```sh
conda create -n shopping-env python=3.7 # (first time only)
conda activate shopping-env
```

### .env File Installation

Second, create an env file and enable it in your environment

This .env file will allow you to set up environment variables and will be necessary for later steps in using a google sheet to store a product inventory. Create the file in your text editor.

Use the following command-line arguments

```sh
pip install python-dotenv
```

### Gspread Package

* This package has issues with the unit testing package, travis, it has been removed in this latest version of the program*

Third, install the gspread package which allows you to access a product inventory in google sheets:

```sh
pip install gspread oauth2client
```

You may have to create an account in order to get gspread API key, follow the following readme: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/gspread.md

### .env File Contents

Lastly, place the following contents inside the .env file:

```sh
tax_rate = "" #place tax rate in decimals within the quotes
GOOGLE_SHEET_ID = #insert your given API key here
SHEET_NAME = "products-custom"
```

## Usage

The code should be ready to run!

Use the following code in terminal:

```sh
python shopping_cart.py
```
