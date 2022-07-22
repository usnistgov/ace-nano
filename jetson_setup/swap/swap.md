# Swap
Add extra swap space to the nano.

## Add Swap
Create and then mount a swap file.
Run the following as root (on Ubuntu, use `sudo`):
1. Create empty 6 GB file for swap. Run `fallocate -l 6G /swapfile`
2. Change permissions so only root can read and write to swap. Run `chmod 600 /swapfile`
3. Tell linux to use swap file. Run `mkswap /swapfile && swapon /swapfile`.
4. Make changes persistant across reboots. Edit `/etc/fstab`, and append the following line `/swapfile swap swap defaults 0 0`.
5. Check swap is recognized. Run `free -h`. Swap should appear with 6GB of total space.

## Attribution
See the following two articals for more info:
https://linuxize.com/post/create-a-linux-swap-file/
https://itsfoss.com/create-swap-file-linux/
