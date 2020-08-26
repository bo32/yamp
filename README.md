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

## Troubleshooting

### USB audio device on the RPi

When starting this project I started using a USB speaker (a B&O one and since Bluetooth fro, the RPi could not connect to it, I decided to use it via USB).  
Some configuration was then required on the Pi to play music via USB audio device. Edit file `/usr/share/alsa/alsa.conf` and change `defaults.ctl.card` and `defaults.pcm.card` properties from value `0` to `1`.  
Source: https://learn.adafruit.com/usb-audio-cards-with-a-raspberry-pi/updating-alsa-config