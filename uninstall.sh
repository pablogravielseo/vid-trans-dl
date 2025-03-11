#!/bin/bash
# Uninstallation script for vid-trans-dl

echo "Uninstalling vid-trans-dl..."
pip3 uninstall -y vid-trans-dl

if [ $? -eq 0 ]; then
    echo "Uninstallation successful!"
else
    echo "Uninstallation failed. Please check the error messages above."
    exit 1
fi 