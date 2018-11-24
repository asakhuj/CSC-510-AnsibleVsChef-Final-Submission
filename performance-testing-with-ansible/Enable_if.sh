#!/bin/bash

sudo ip link set SW1-bridge up
sudo ip addr add 192.168.205.1/24 dev SW1-bridge
sudo ip link set SW2-bridge up
sudo ip link set SW3-bridge up
sudo ip link set SW4-bridge up
