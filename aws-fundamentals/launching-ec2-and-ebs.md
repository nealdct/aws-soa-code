## Launch EC2 instance
1. Create a security group
aws ec2 create-security-group --group-name EC2-EBS-Lab --description "Temporary SG for the EC2 and EBS Lab"
2. Add a rule for SSH inbound to the security group
aws ec2 authorize-security-group-ingress --group-name EC2-EBS-Lab --protocol tcp --port 22 --cidr 0.0.0.0/0
3. Launch instance in US-EAST-1A
aws ec2 run-instances --image-id ami-0dfcb1ef8550277af --instance-type t2.micro --placement AvailabilityZone=us-east-1a --security-group-ids sg-xxxxxxxxxxxxxx

## Create and Attach an EBS Volume
1. Create a 10GB gp2 volume in us-east-1a with a name tag of 'test-volume-1'
2. List non-loopback block devices on instance
sudo lsblk -e7
3. Attach the volume to the instance in us-east-1a
4. Rerun the command to view block devices

## Create a filesystem and mount the volume
1. Create a filesystem on the EBS volume
sudo mkfs -t ext4 /dev/xvdf
2. Create a mount point for the EBS volume
sudo mkdir /data
3. Mount the EBS volume to the mount point
sudo mount /dev/xvdf /data
4. Make the volume mount persistent
Run: 'sudo nano /etc/fstab' then add '/dev/xvdf /data ext4 defaults,nofail 0 2' and save the file