# Radio-Power
Code for recording RTL Radio power with GPS

# Install
sudo apt install vim rtl-sdr nmap busybox git rfkill zd1211-firmware hostapd hostap-utils iw dnsmasq
#UnPlug sdr device in and kill kernel module
sudo rmmod dvb_usb_rtl28xxu rtl2832

#test sdr device and get some info
sudo rtl_test -t

#setup hotspot
git clone https://github.com/unixabg/RPI-Wireless-Hotspot.git
cd RPI-Wireless-Hotspot
sudo ./install

#gps setup
sudo apt install gpsd gpsd-clients python-gps
#follow these instructions
https://learn.adafruit.com/adafruit-ultimate-gps-on-the-raspberry-pi?view=all

#test with 
cat /dev/ttyS0
