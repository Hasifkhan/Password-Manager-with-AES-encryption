#!/bin/bash

# Check if Python3 and pip3 are installed
if ! command -v python3 &> /dev/null; then
    echo "Python3 is not installed. Installing Python3..."
    sudo apt-get install python3
fi

if ! command -v pip3 &> /dev/null; then
    echo "pip3 is not installed. Installing pip3..."
    sudo apt-get install python3-pip
fi

# Install the required Python libraries
echo "Installing required Python libraries..."
pip3 install cryptography

# Make the main Python script executable
echo "Making password_manager.py executable..."
chmod +x password_manager.py

echo "Installation complete. You can now run ./password_manager.py"
