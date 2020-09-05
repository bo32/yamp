# Yet Another Music Player for the Raspberry Pi 

[![Build Status](https://travis-ci.org/bo32/yamp-pi.svg?branch=master)](https://travis-ci.org/bo32/yamp-pi)

## Installation (for the RPi)

```bash
sudo apt install vlc -y # if not already installed
git clone https://github.com/bo32/yamp-pi.git
cd yamp-pi
pip3 install -r requirements --user
```

## Start the application

```bash
python manage.py runserver 0.0.0.0:8000
```

Open your browser at `http://raspberrypi.local:8000/player/`
or use the following REST end-points:
* GET: _address_/player/play/Your Album
* GET: _address_/player/next
* GET: _address_/player/previous
* GET: _address_/player/pause
* GET: _address_/player/sounddown
* GET: _address_/player/soundup

## Extras features

### Start the application as a service 

Follow instructions [here](https://www.wikihow.com/Execute-a-Script-at-Startup-on-the-Raspberry-Pi). 

## Troubleshooting

### USB audio device on the RPi

When starting this project I started using a USB speaker (a B&O one and since Bluetooth fro, the RPi could not connect to it, I decided to use it via USB).  
Some configuration was then required on the Pi to play music via USB audio device. Edit file `/usr/share/alsa/alsa.conf` and change `defaults.ctl.card` and `defaults.pcm.card` properties from value `0` to `1`.  
Source: https://learn.adafruit.com/usb-audio-cards-with-a-raspberry-pi/updating-alsa-config

## About this project

This project is strongly inspired by (this other one)[https://www.hackster.io/mark-hank/sonos-spotify-vinyl-emulator-3be63d].  
The NFC reader used is the (PN532_NFC_HAT)[https://www.waveshare.com/wiki/PN532_NFC_HAT].  

![Waveshare - PN532 NFC HAT](https://www.waveshare.com/media/catalog/product/cache/1/image/800x800/9df78eab33525d08d6e5fb8d27136e95/p/n/pn532-nfc-hat-1.jpg?size=300)
