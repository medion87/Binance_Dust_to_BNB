# Binance Dust to BNB bot
This is a very simple python script that converts your dust to BNB on Binance Exchange.
You can just use this script in your terminal or you can use it in Docker.

## Installation
**Clone the repository**
```
git clone https://github.com/medion87/Binance_Dust_to_BNB.git
```

**Download zip file**
Or you can download this script as a zip file.
<a title='Binance_Dust_to_BNB' href='https://github.com/medion87/Binance_Dust_to_BNB/archive/refs/heads/main.zip'>https://github.com/medion87/Binance_Dust_to_BNB/archive/refs/heads/main.zip</a>

**Install required libraries**
```
pip install -r requirements.txt
```

## Configure
**settings.cfg**
There is a file called settings_example.cfg.
Rename this file to settings.cfg and change the settings.

```
[default]
## Place your Binance api key and api secret here.
## How you can create a Binance api key? -> https://www.binance.com/en/support/faq/360002502072
## IMPORTANT: Save your api key and api secret in a document, you can no longer obtain your api secret via Binance afterwards.
## Enable Spot & Margin Trading and Permits Universal Transfer
## We can NOT send any money out of your account!
## Universal Transfer is for transfer from your spot wallet to another wallet in your account.
api_key = YOUR_API_KEY
api_secret = YOUR_API_SCRET

## Which currency do you want to use?
## For example USDT. This must be in capital letters.
currency = USDT

## What is the maximum amount that the script may convert to BNB?
## As an example, the price of ADA USDT is 0.763 we still have 5 ADA which is worth 3.81 USDT. 
## But the script should not convert anything worth more than 9.99 USDT.
## This completely depends on which currency you want to use.
max = 9.99

## NOTE: Rename this file to settings.cfg
```

**Dockerfile**
There is a file called Dockerfile_example
Rename this file to Dockerfile

On line 4 in this file it says WORKDIR this must be the path to where the folder is located. 
Change this to your own path.

```
# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

WORKDIR /YOUR ROUTE TO MAP/Binance_Dust_To_BNB

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "main"]
```

**Creating Docker image**
Open your terminal and enter:
```
docker build --tag binance_dust Your_Path_To_Map/Binance_Dust_to_BNB
```

**Creating Docker container**
We just made an image. Now we are going to use this to build a container. First need image id. Here for type you:
```
docker images
```

copy the image id from binance dust and paste it after -d
```
docker run -d YOUR ID
```

Ok now we're going to make this container always reboot if it crashed or you just because the computer was off.
Eerst moeten we weten wat is de container ID is
```
docker ps
```

And finally, we're going to update the container with the command to always reboot.
```
docker update --restart always YOUR ID
```

## License
<a href='https://github.com/medion87/Binance_Dust_to_BNB/blob/main/LICENSE.md'>Open Software License ("OSL") v 3.0</a>