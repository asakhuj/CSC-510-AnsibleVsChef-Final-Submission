#!/bin/bash

./venv-ansible-playbook 2.2.0 -i hosts prepare.yml
./prepared/test.sh
