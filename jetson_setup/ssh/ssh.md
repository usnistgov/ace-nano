# SSH Config
Setup SSH access. For the purposes of this document "local host" will refer to the developers computer, and "remote" will refer to the remote device that is being configured. 

This instruction set assumes the devices which require ssh access are all reachable. 

SSH should be installed by default on all the devices, check by running `ssh -V`.  If not, as root (on Ubuntu, use `sudo`) run `apt install openssh-client`. 
Check that `~/.ssh` exists. If not run `mkdir -p $HOME/.ssh`.

## SSH Key Setup
To allow the remote device to acess other remote devices, setup an ssh key.
1. Run the following command (read and follow instructions that are displayed), `ssh-keygen -t ecdsa -b 521`. 

Setup ssh keys on all remote devices. 

## Authorizing Key Access
To have seemless access (ie not password input -- also more secure than passwords), an ssh key needs to be authorized by a device before it can be used to login. 
1. On the local host. Create a `authorized_keys` file (this should be seperate from your hosts `~/.ssh/authorized_keys` file -- can append this new file later). 
2. Open the `authorized_keys` file for editing. 
3. For each remote device, copy the `~/.ssh/id_ecdsa.pub` (assuming default naming convention), file (ie, the one line that exists in the file) into the `authorized_keys` file on the local host. The `authorized_keys` file should now have every remote devices public key. Note: DO NOT COPY `~/.ssh/id_ecdsa` into the `authorized_keys` file, these are PRIVATE. 
4. Copy the `authorized_keys` file to each of the remote devices. Run the command `scp ./authorized_keys REMOTE_USER@REMOTE_IP:/home/REMOTE_USER/.ssh/`. 

See inclueded `authorized_keys` file for an example.

## SSH Config File
Having an ssh config file allows for easy movement between remote devices. 
1. Create an `ssh_config` file. Run `touch ~/.ssh/ssh_config`.
2. Open the `ssh_config` file in an editor.
3. For remote device append the following structure to the `ssh_config` file.
```
Host SHORT_NAME
  User REMOTE_USER_NAME 
  Hostname REMOTE_DEVICE_IP 
```
4. Copy the `ssh_config` file to each remote device. Run the command `scp ./authorized_keys REMOTE_USER@REMOTE_IP:/home/REMOTE_USER/.ssh/config`

For an example `config` see the included `ssh_config`.

## Recommended reading

We recommend users familiarize themselves with `ssh-agent`; the following is a good primer on ssh and its agents https://wiki.gentoo.org/wiki/SSH
