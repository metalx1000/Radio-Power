# Radio-Power
Code for recording RTL Radio power with GPS

# Install
sudo apt install vim rtl-sdr nmap busybox git
#UnPlug sdr device in and kill kernel module
sudo rmmod dvb_usb_rtl28xxu rtl2832

#test sdr device and get some info
sudo rtl_test -t

