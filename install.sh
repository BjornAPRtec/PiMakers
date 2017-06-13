#!/bin/bash

function ask_yes_or_no() {
    read -p "$1 : "
    case $(echo $REPLY | tr '[A-Z]' '[a-z]') in
        y|yes) echo "yes" ;;
        *)     echo "no" ;;
    esac
}

if [ "no" == $(ask_yes_or_no "Have you ran 'sudo apt-get update' and 'sudo apt-get upgrade'? [Y/n]") ]
   
then
    echo "Do that before running the installation."
    exit 0

else
    echo "Starting installation of program and the packages needed."
    cd ~

    echo "Getting required packages."
    sudo apt-get install python3-pyqt5
    sudo pip3 install matplotlib
    sudo pip3 install pymysql
    sudo pip3 install pyserial

    echo "mysql-server will now be installed, you will be prompted to enter a password for the root user."
    sleep 5
    sudo apt-get -y install mysql-server --fix-missing

    find ~ -name PiMakers.desktop | xargs -I '{}' cp {} ~/Desktop
fi
