# Yet Another Music Player for the Raspberry Pi

## Installation (for the RPi)

```bash
sudo apt install vlc -y # for the RPi

git clone https://github.com/bo32/yamp-pi.git
cd yamp-pi
pip3 install -r requirements --user
```

## Start the application

```bash
python manage.py runserver 0.0.0.0:8000
```

Open your browser at http://raspberrypi.local:8000/player/
or use the following REST end-points:
* GET: _address_/player/play/Your Album
* GET: _address_/player/next
* GET: _address_/player/previous
* GET: _address_/player/pause
* GET: _address_/player/sounddown
* GET: _address_/player/soundup

