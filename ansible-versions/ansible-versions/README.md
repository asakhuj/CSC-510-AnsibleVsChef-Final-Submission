It feels like Ansible becomes slower with each release? Is it true?

This is an answer. We are using Ansible to measure Ansible's performance. Kindly run the scripts with sudo privelege : 


Steps :

1) chmod +x start.sh
2) chmod +x venv-ansible-playbook
3) sudo apt-get install python-pip python-dev build-essential
4) pip install --upgrade pip
5) pip install --upgrade virtualenv
6) ./start.sh



I performed the following tests on NCSU VCL machine, creating virtual environments and testing the templates on all stable ansible versions.


Result on my machine : 

Test 1
Subject: Testing template performance
------------------------------------------------------
v1.9.6 1:56.08
v2.0.2 2:12.62
v2.1.3 2:19.40
v2.2.0 1:02.48

Test 2
Subject: Testing big stack of variables
------------------------------------------------------
v1.9.6 1:57.17
v2.0.2 2:14.20
v2.1.3 2:22.90
v2.2.0 1:03.15

Test 3
Subject: Testing shell execution with register
------------------------------------------------------
v1.9.6 1:55.44
v2.0.2 2:00.34
v2.1.3 2:05.97
v2.2.0 0:45.97


