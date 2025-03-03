#!/bin/bash

# Before executing this file, check and modify its permissions if needed.
# Run the following command to list the file details:
# ls -l
# If the execute (x) permission is missing, the output will look like this:
# -rw-rw-r-- 1 sherry sherry 1221 Feb 20 09:50 download.sh

# To add execute permissions, run:
# chmod +x download.sh
# After this, the output should look like:
# -rwxrwxr-x 1 sherry sherry 1221 Feb 20 09:50 download.sh

# Finally, to execute the script in bash, run:
# ./download.sh

# Update the system
echo "Updating packages..."
sudo apt-get update 

# Install GParted
echo "Installing GParted..."
sudo apt-get install gparted -y

# Install Visual Studio Code
echo "Installing Visual Studio Code..."
sudo snap install --classic code

# Install Google Chrome
echo "Installing Google Chrome..."
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt -f install
rm google-chrome-stable_current_amd64.deb
# NOTICE: if you change host name then open gg chrome, it is not working
# try: rm -rf ~/.config/google-chrome/Singleton*

# Remove Firefox
sudo snap remove firefox

# Install Git
echo "Installing Git..."
sudo apt-get install -y git
git --version

# Install Java
echo "Installing Java..."
sudo apt install openjdk-21-jdk-headless -y
javac --version

# Install Unikey
echo "Installing Unikey..."
echo | sudo add-apt-repository -y ppa:ubuntu-vn/ppa
sudo apt-get update
sudo apt-get install ibus-unikey
ibus restart

# Install Anaconda 
echo "Downloading Anaconda Installer..."
wget https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Linux-x86_64.sh
bash ~/Anaconda3-2024.10-1-Linux-x86_64.sh
source ~/.bashrc
conda --version
# NOTICE: The version may change daily. If an error occurs, you can find the latest version to install.

# Finalize
echo "All applications have been installed successfully!"
