chmod +x Enable_if.sh
echo "Downloading preReq*****************"
wget http://yum.tamu.edu/centos/7.5.1804/isos/x86_64/CentOS-7-x86_64-Minimal-1804.iso
echo "*************Downloading ansible**************"
sudo apt-get update
sudo apt-get install -y software-properties-common
sudo apt-add-repository ppa:ansible/ansible
sudo apt-get update
sudo apt-get install -y ansible
echo "Checking the version of ansible"
ansible --version
echo "****Checked the version*****"
echo "Follow the readMe now"

