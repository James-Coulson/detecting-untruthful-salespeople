# Untruthful salespeople and detecting them using Gen AI

## Inital set up

Prior to running the API you will first need to set up a virtual environment to run the API within. THis can be performed by running the below sequence of commands

	python3 -m venv venv
	source ./venv/bin/activate

Once this has been completed you can then install the necessary requirements

	pip install -r requirements.txt

You will also need to set the openai API key. This can be done as follows

	export OPENAI_API_KEY={ paste api key here }

## Running example test cases

The test cases can be run using the following command,

	python3 ./gpt/main.py
