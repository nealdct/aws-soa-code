# Perform the following actions per Region

aws ec2 create-security-group --group-name R53PolicyTest --description "Route 53 Policy Test" --region us-east-1

aws ec2 authorize-security-group-ingress --group-name R53PolicyTest --protocol tcp --port 22 --cidr 0.0.0.0/0 --region us-east-1

aws ec2 authorize-security-group-ingress --group-name R53PolicyTest --protocol tcp --port 80 --cidr 0.0.0.0/0 --region us-east-1

aws ec2 run-instances --image-id <ami-id> --count 1 --instance-type t2.micro --security-group-ids <security-group-id> --subnet-id <subnet-id> --user-data file://ec2-user-data-web-app.txt --region us-east-1

aws elbv2 create-load-balancer --name ALB1 --subnets <subnet-ids> --security-groups <security-group-ids> --type application

aws elbv2 create-target-group --name TG1 --protocol HTTP --port 80 --vpc-id <vpc-id>

aws elbv2 register-targets --target-group-arn <target-group-arn> --targets Id=<instance-id>

aws elbv2 create-listener --load-balancer-arn <load-balancer-arn> --protocol HTTP --port 80 --default-actions Type=forward,TargetGroupArn=<target-group-arn>