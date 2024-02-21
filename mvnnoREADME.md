#! /bin/bash
sudo apt update -y && sudo apt install unzip
wget https://dlcdn.apache.org/maven/maven-3/3.9.6/binaries/apache-maven-3.9.6-bin.zip
unzip apache-maven-3.9.6-bin.zip
echo "make it as command"
sudo ln -s /home/ubuntu/apache-maven-3.9.6/bin/mvn  /usr/local/sbin/
chmod 777 /usr/local/sbin/mvn
