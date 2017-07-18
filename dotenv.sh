#!/bin/sh
echo "be careful, with ampersands and backslashes in your secret key this awk command wont work"
awk -i inplace '{gsub(/secret_key_goes_here/, var); print}' var=$(cat .env) ./ryan_data/settings.py

