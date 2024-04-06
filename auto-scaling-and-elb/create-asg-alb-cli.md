
## Create a security group

aws ec2 create-security-group --group-name ALB-EC2-Access --description "Route 53 Policy Test" --region us-east-1

aws ec2 authorize-security-group-ingress --group-name ALB-EC2-Access --protocol tcp --port 22 --cidr 0.0.0.0/0 --region us-east-1

aws ec2 authorize-security-group-ingress --group-name ALB-EC2-Access --protocol tcp --port 80 --cidr 0.0.0.0/0 --region us-east-1

## create auto scaling group

aws autoscaling create-auto-scaling-group --auto-scaling-group-name ASG1 --launch-template "LaunchTemplateName=LT1" --min-size 1 --max-size 3 --desired-capacity 2 --availability-zones "us-east-1a" "us-east-1b" --vpc-zone-identifier "<subnet-id>, <subnet-id>"

## create target group, load balancer, listener, and then link it all up

aws elbv2 create-target-group --name TG1 --protocol HTTP --port 80 --vpc-id <vpc-id>

aws elbv2 create-load-balancer --name ALB1 --subnets <subnet-id> <subnet-id> --security-groups <security-group-id>

aws elbv2 create-listener --load-balancer-arn <alb-arn> --protocol HTTP --port 80 --default-actions Type=forward,TargetGroupArn=<target-group-arn>

aws autoscaling attach-load-balancer-target-groups --auto-scaling-group-name ASG1 --target-group-arns <target-group-arn>

## delete ASG and ALB

aws elbv2 delete-load-balancer --load-balancer-arn <alb-arn>

aws autoscaling delete-auto-scaling-group --auto-scaling-group-name ASG1 --force-delete