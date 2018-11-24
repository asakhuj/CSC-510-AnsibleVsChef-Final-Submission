#!/bin/bash

vmm1=$(sudo virsh domifaddr VMM1 | grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}')         
vmm2=$(sudo virsh domifaddr VMM2 | grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}')   

vmm3="$vmm1 ansible_connection=ssh ansible_ssh_user=root ansible_ssh_pass=root ansible_ssh_common_args='-o StrictHostKeyChecking=no'"
vmm4="$vmm2 ansible_connection=ssh ansible_ssh_user=root ansible_ssh_pass=root ansible_ssh_common_args='-o StrictHostKeyChecking=no'"         
echo "[VM_IPs]" >> /etc/ansible/hosts
echo $vmm3 >> /etc/ansible/hosts
echo $vmm4 >> /etc/ansible/hosts

