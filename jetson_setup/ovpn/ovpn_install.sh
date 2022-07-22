#!/bin/bash
# run the following as root (these commands are for Ubuntu 20.04)
apt install curl apt-transport-https
curl -fsSL https://swupdate.openvpn.net/repos/openvpn-repo-pkg-key.pub | gpg --dearmor > /etc/apt/trusted.gpg.d/openvpn-repo-pkg-keyring.gpg
# for the following, replace "bionic" with whatever release name is appropriate
curl -fsSL https://swupdate.openvpn.net/community/openvpn3/repos/openvpn3-bionic.list >/etc/apt/sources.list.d/openvpn3.list
apt update
apt install openvpn3

apt-get install openvpn
