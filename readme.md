# Python Project Setup Guide

## Setup Virtual Environment


## Clone The project files
```sh
git clone https://github.com/Mohammed22668/whatsapp_msg
```


### Move into project dir
```sh
cd whatsapp_msg
```



## Install Google Chrome
```sh
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
```
```sh
sudo dpkg -i google-chrome-stable_current_amd64.deb
```


## Install ChromeDriver
```sh
wget https://storage.googleapis.com/chrome-for-testing-public/135.0.6999.2/linux64/chromedriver-linux64.zip
```
```sh
cd /chromedriver-linux64
```
```sh
sudo cp chromedriver /usr/local/bin/
```
```sh
sudo chmod +x /usr/local/bin/chromedriver
```


### Windows:

```sh
python -m venv env
```

### Linux:

```sh
python3 -m venv env
```

## Activate Virtual Environment

### Windows:

```sh
env\Scripts\activate
```

### Linux:

```sh
source env/bin/activate
```

## Install Requirements

```sh
pip install -r requierment.txt
```

## Run Python File

```sh
python main.py
```

### Steps

    - Choose the xlsx file and Click Send Messages
    - The code will open the Browser (Chrome Driver)
    - Please scan the QR code to log in to WhatsApp Web.
    - After login into WhatsApp Click OK when you are logged in.

### xlsx File example

![Example xlsx](image.png)
