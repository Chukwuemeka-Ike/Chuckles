# Fitbit Data Extractor

The script allows us to download a person's Fitbit data.

I make no claims on the originality of the code here. All the code is based on the work by Michael Galarnyk in this [Medium article](https://towardsdatascience.com/using-the-fitbit-web-api-with-python-f29f119621ea). It's here to make my life easier.

## Usage
To use the script, we need the [python-fitbit](https://github.com/orcasgit/python-fitbit) code.
```bash
git clone https://github.com/orcasgit/python-fitbit.git .
```
Install the requirements for the project.
```bash
pip3 install -r requirements/base.text
pip3 install -r requirements/dev.text
pip3 install -r requirements/test.text
```
Now, you can add a Client ID and Secret to the *data_extractor.py* file, and choose the data you want to download. 

## TODO
1. spo2 and hrv don't work yet. Need to figure these out.