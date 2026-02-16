# base-API-script
This repo can be used as a starting point for developing a Python script that utilizes the Plextrac API in some way. It acts as a mini framework with some helpful utilities that make endpoint calls easier. These utilities include a logger, authentication handler, API wrapper library that stores endpoint URLs, and other general utility function that revolve around user inputs, data sanitization, and data validation.

To get started make a copy of this repo and read through the main.py file which goes more in-depth about the utilities available. You can also run the script with the instructions below to see the output of the examples used when describing the utilities available. Once you know what's available, you can remove the examples, and start writing your script in the main.py file.

# Requirements
- [Python 3+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [pipenv](https://pipenv.pypa.io/en/latest/)

# Installing
After installing Python, pip, and pipenv, run the following commands to setup the Python virtual environment.
```bash
git clone this_repo
cd path/to/cloned/repo
pipenv install
```

# Setup
After setting up the Python environment the script will run in, you will need to setup a few things to configure the script before running.

## Credentials
In the `config.yaml` file you should add the full URL to your instance of Plextrac.

The config also can store your username and password. Plextrac authentication lasts for 15 mins before requiring you to re-authenticate. The script is set up to do this automatically through the authentication handler. If these 3 values are set in the config, and MFA is not enabled for the user, the script will take those values and authenticate automatically, both initially and every 15 mins. If any value is not saved in the config, you will be prompted when the script is run and during re-authentication.

# Usage
After setting everything up you can run the script with the following command. You should run the command from the folder where you cloned the repo.
```bash
pipenv run python main.py
```
You can also add values to the `config.yaml` file to simplify providing the script with custom parameters needed to run.

## Required Information
The following values can either be added to the `config.yaml` file or entered when prompted for when the script is run.
- PlexTrac Top Level Domain e.g. https://yourapp.plextrac.com
- Username
- Password

## Script Execution Flow
- Starts executing the main.py file
- Prints script info stored in settings.py
- Reads in values from config.yaml file
- Goes through list of examples to show the user current functionality that can be utilized
