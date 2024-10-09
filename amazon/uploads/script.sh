#!/bin/bash
# To connect to your EC2 instance and install the Apache web server with PHP 
yum update -y 
yum install -y httpd php8.1 
systemctl enable httpd.service 
systemctl start httpd 
cd /var/www/html 
wget https://us-west-2-tcprod.s3.amazonaws.com/courses/ILT-TF-200-ARCHIT/v7.7.1.prod-8926c8df/lab-2-VPC/scripts/instanceData.zip 
unzip instanceData.zip
