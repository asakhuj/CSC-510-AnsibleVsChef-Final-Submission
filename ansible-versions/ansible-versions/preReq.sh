echo "**********Downloading preReq***********************"
sudo apt-get install python-pip python-dev build-essential
sudo pip install --upgrade pip
sudo pip install --upgrade virtualenv
echo "**********Downloaded all preReq******************"
chmod +x start.sh
echo "**********Running the tests*************"
./start.sh
