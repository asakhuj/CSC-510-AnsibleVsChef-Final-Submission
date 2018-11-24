
Requirements:

OS:  Ubuntu 16.04
Download  CentOS-7-x86_64-Minimal-1708.iso




1. Add following files into a folder.

anaconda-ks.cfg 
App_install.yml     
Enable_if.sh 
SW2.xml  
SW4.xml
Ansible.yml      
create_invetory.sh   
SW1.xml  
SW3.xml
VMM3.xml


2. Run Ansible.yml as a sudo user. 

   sudo ansible-playbook Ansible.yml

3. Enter the path of Centos 7 image file.

4. Wait for the VM1 to install

5. Once the installation completes, click on reboot and close the console. 

6. Once the Ansible.yml playbook completes execution, execute App_install.yml 
  
    sudo ansible-playbook App_install.yml

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++Completed++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
