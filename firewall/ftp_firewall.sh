#!/bin/sh
# adding firewall entry for port 2121 nix
sudo iptables -A INPUT -s 192.168.1.0/24 -p tcp --dport 2121 -j ACCEPT
sudo iptables -A OUTPUT -d 192.168.1.0/24 -p tcp --sport 2121 -j ACCEPT
# for passive ports
sudo iptables -A INPUT -s 192.168.1.0/24 -p tcp --dport 60000:65534 -j ACCEPT
sudo iptables -A OUTPUT -d 192.168.1.0/24 -p tcp --sport 60000:65534 -j ACCEPT


# requires service wrapper
sudo service firewall restart

# may require 
# modprobe ip_conntrack_ftp
