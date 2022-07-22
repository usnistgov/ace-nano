# OpenVPN Install
Install OpenVPN and have it start automatically on boot.

## Install OpenVPN
First Open VPN needs to be installed: 
1. Run `./ovpn_install.sh` as root. This will install the apt repository for openvpn3, install openvpn3, and install openvpn.
2. Check openvpn is installed by running `openvpn --version`

## Configure to run on Boot
Second configure Open VPN to start on boot.
1. Ask network admin for an `.ovpn` file. This is what allows open vpn to find and connect to the network. 
As root (aka sudo) do the following:
2. Edit `/etc/default/openvpn` and uncomment `AUTOSTART="all"`. 
3. Copy the `.ovpn` file to `/etc/openvpn/client.conf`. 
4. Run `touch /etc/openvpn/pass` to create the file, then change the permissions by running `chmod 400 /etc/openvpn/pass`.
5. Enable the Openvpn service to run at boot. Run the command `systemctl enable openvpn@client.service`

At this point, the device will automatically connect when the device reboots. DO NOT REBOOT YET.

### Check OVPN connection
Check VPN is properly configured before rebooting. 
As Root (`sudo` on Ubuntu) run the following:
1. Reload the openvpn daemon. Run the command `systemctl daemon-reload`.
2. Start the VPN service. Run the command `service openvpn@client start`.
3. Run `ifconfig` and look for a `tun0` (it could be another tunnel if multiple vpn connections are configured) and check the ip address is correctly assigned. 

## Attribution

For further information on the process see:

To install openvpn3 on linux see: https://community.openvpn.net/openvpn/wiki/OpenVPN3Linux

To setup openvpn service on reeboot: https://www.ivpn.net/knowledgebase/linux/linux-autostart-openvpn-in-systemd-ubuntu/
