#  Install Setup for Remote Device

ACE (Analytic Container Enviroment) being based on containers, which reduces the need for software setup on a host machine. 

This Setup includes 2 nessesary steps (JetPack + Docker), and a few additional optional steps.

ACE assumes all devices are able to see one another. This can either be achieved using a local network or an Overlay Network. The choice of specific overlay network is left to the end user

Here, we are using a method that is tested to work being most firewalls: OpenVPN, it require each hosts to connect to a central server that acts as a relay while providing a common network topology.

## Prep Jetson 
Follow the guide located at: https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit. At the time of writing, JetPack 4.6.1 was used. 

This will yeild a Jetson with the correct OS, and the nessesary JetPack version. 

JetPack installs a Ubuntu desktop version, make sure to perform software and security updates after installation.
After setup, we recommend switching the host to `runlevel 3` (ie networking without X11). Run the following commands and reboot:
```
sudo systemctl enable multi-user.target
sudo systemctl set-default multi-user.target
```

## Install ACE specific Items
Install the packages nessesary to run ACE containers. 

1. Docker: This is needed to support ACE's container setup.
2. Additional SWAP (recommended): On lower end hardware (ex a Jetson Nano), ACE can push data to the device faster than the device can process the data. This results in the freeze and ultimate crashing of the machine. Additional SWAP space can alleviate some of that pressure. 
3. OpenVPN (optional): All ACE components need to see one another, and be discoverable. The use of a VPN allows remote clients to find one another and for remote devices to publish data and run analytics.
4. SSH (optional): SSH allows for easy navigation between clients and remote access to machines.

Once this setup is done, if you want to install ACE itself, you can follow the regular setup instructions from: https://github.com/usnistgov/ACE

### Docker
Install docker package and do post install configuration to allow `docker` command to be run without sudo.
See `./docker/docker.md`

### SWAP
Create SWAP file and mount it.
See `./swap/swap.md`

### Open VPN
Install and Configure OpenVPN to connect on boot.
See `./ovpn/ovpn.md`

### SSH
Standard SSH practice
See `./ssh/ssh.md`
Setup ssh after Open VPN. So you can ssh between clients on the VPN.
