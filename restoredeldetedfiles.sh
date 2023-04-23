sed -n '/^Remove/ s/([^ ]*//g;s/Remove: //p' < /var/log/apt/history.log | tee uninstalled
sudo apt update
sudo apt install
