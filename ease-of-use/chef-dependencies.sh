sudo apt update
sudo apt install -y ruby-full
echo "-----------------Ruby installed -----------------"
ruby --version
echo "*********Downloading ChefDK********"
wget https://packages.chef.io/files/stable/chefdk/3.2.30/ubuntu/18.04/chefdk_3.2.30-1_amd64.deb
sudo dpkg -i chefdk_3.2.30-1_amd64.deb
echo "*********Chef installed*****"
chef --version
sudo apt-get install -y virtualbox
VBoxManage --version
sudo apt-get install -y vagrant
sudo gem install kitchen-vagrant -v '0.16.0'
vagrant --version
echo "***********Downloaded all preReq*******"