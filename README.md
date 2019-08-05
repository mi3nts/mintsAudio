# mintsAudio
sudo apt-get update

sudo apt-get install portaudio19-dev

pip3 install PyAudio

set dev rules 
```
sudo nano 93-mymic.rules 
```
The rules should read
```
SUBSYSTEMS=="usb", ATTRS{idVendor}=="08bb", ATTRS{idProduct}=="2902", GROUP="users", MODE="0666"
SUBSYSTEMS=="usb", ATTRS{idVendor}=="0556", ATTRS{idProduct}=="0001", GROUP="users", MODE="0666"

```
