# Create private subnets and NAT gateway

## Create a private subnet in us-east-1a
aws ec2 create-subnet --vpc-id <default-vpc-id> --cidr-block 172.31.96.0/20 --availability-zone us-east-1a --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=private-1a}]'
## Create a private subnet in us-east-1b
aws ec2 create-subnet --vpc-id <default-vpc-id> --cidr-block 172.31.112.0/20 --availability-zone us-east-1b --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=private-1b}]'
## Create a route table in the default VPC
aws ec2 create-route-table --vpc-id <default-vpc-id> --tag-specifications 'ResourceType=route-table,Tags=[{Key=Name,Value=PrivateRT}]'
## Associate private subnets to the route table
aws ec2 associate-route-table --route-table-id <route-table-id> --subnet-id <private-subnet-id-1a>
aws ec2 associate-route-table --route-table-id <route-table-id> --subnet-id <private-subnet-id-1b>
## Create an Elastic IP
aws ec2 allocate-address
## Create a NAT gateway
aws ec2 create-nat-gateway --subnet-id <public-subnet-id> --allocation-id <eip-allocation-id>
## Update the private route table to point to the NAT gateway
aws ec2 create-route --route-table-id <route-table-id> --destination-cidr-block 0.0.0.0/0 --nat-gateway-id <nat-gateway-id>

# Launch EC2 instance

1. Create a security group
aws ec2 create-security-group --group-name NAT-GW-LAB --description "Temporary SG for the NAT gateway Lab"
2. Launch instance in US-EAST-1A
aws ec2 run-instances --image-id ami-005f9685cb30f234b --instance-type t2.micro --subnet-id <private-subnet-id> --security-group-ids <security-group-id> --iam-instance-profile Name=SSMInstanceProfile