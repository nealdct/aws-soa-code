# Install Apache and Configure Logging
1. If not already installed, install the CloudWatch agent
sudo yum install amazon-cloudwatch-agent
2. Also, install collectd
sudo amazon-linux-extras install collectd
3. Install and enable Apache
sudo yum install -y httpd
sudo systemctl start httpd
sudo systemctl enable httpd
4. If the config file exists, delete it
sudo rm -rf /opt/aws/amazon-cloudwatch-agent/bin/config.json
5. Create the config.json
sudo nano /opt/aws/amazon-cloudwatch-agent/bin/config.json
6. Add the contents from the cw-config.json file provided
7. Run the following commmand
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c file:/opt/aws/amazon-cloudwatch-agent/bin/config.json -s
8. Then make sure the agent is started
sudo systemctl start amazon-cloudwatch-agent
9. Generate some traffic to Apache including some 404s

# Create a metric filter and alarm
1. Create a metric filter and use the following pattern
[host, logName, user, timestamp, request, statusCode=404, size]
2. Define the filter and create
Name = 404
Metric namespace = HTTPStatusCode
Metric name = 404Error
Metric value = 1
Unit = Count
3. Create an alarm for the filter with count greater than 2 in 5 minutes
4. Create a new SNS Topic or use an existing one
5. Generate more 404 errors