kitchen init
kitchen list
echo"*****************"
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
chef generate cookbook git_cookbook
#cd git_cookbook
kitchen create default-ubuntu-1604
kitchen converge
