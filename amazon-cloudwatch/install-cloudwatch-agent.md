# Create the IAM role for SSM/CloudWatch
1. Create an IAM role with an EC2 trust policy
2. Add the following managed policies
CloudWatchAgentServerPolicy
AmazonSSMManagedInstanceCore
3. Name the IAM role as below and create
CloudWatchAgentServerRole
4. Launch an EC2 instance and attach the role

# Install the CloudWatch agent using SSM Run Command
1. Choose AWS-ConfigureAWSPackage
2. Under name enter AmazonCloudWatchAgent
3. Install collectd
sudo amazon-linux-extras install collectd
4. Run the wizard on the EC2 instance command line
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-config-wizard
5. During the wizard specify additional log file collection
/var/log/messages
6. Run the following commmand
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c file:/opt/aws/amazon-cloudwatch-agent/bin/config.json -s
7. Then make sure the agent is started
sudo systemctl start amazon-cloudwatch-agent