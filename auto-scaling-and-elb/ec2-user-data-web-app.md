# CODE UPDATED SO IT WORKS WITH AMAZON LINUX 2 AMI AND AMAZON LINUX 2023
*** COPY CODE FROM LINES 4-11 ***

#!/bin/bash
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
EC2AZ=$(TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` && curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/meta-data/placement/availability-zone)
echo '<center><h1>This Amazon EC2 instance is located in Availability Zone: AZID </h1></center>' > /var/www/html/index.txt
sed "s/AZID/$EC2AZ/" /var/www/html/index.txt > /var/www/html/index.html