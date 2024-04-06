# Launch instance, stop instance
1. Launch an EC2 instance
aws ec2 run-instances --image-id ami-0aa7d40eeae50c9a9 --instance-type t2.micro --placement AvailabilityZone=us-east-1a
2. Stop the EC2 instance
aws ec2 stop-instances --instance-id i-XXXXXXXXXXXXXXX