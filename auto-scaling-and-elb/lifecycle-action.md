
1. Create an SNS Topic

aws sns create-topic --name my-lifecycle-topic

2. Create a lifecycle hook

aws autoscaling put-lifecycle-hook --auto-scaling-group-name ASG1 --lifecycle-hook-name my-lifecycle-hook --lifecycle-transition autoscaling:EC2_INSTANCE_TERMINATING --notification-target-arn <sns-topic-arn> --role-arn arn:aws:iam::821711655051:role/aws-service-role/autoscaling.amazonaws.com/AWSServiceRoleForAutoScaling --heartbeat-timeout 300

3. Create a role that can be assumed by Lambda with the permissions in the iam-permissions-policy-lambda.json file

4. Create a Lambda function with the code in the lambda-lifecycle-action.py file

5. Subscribe the function to the topic

aws sns subscribe --topic-arn <sns-topic-arn> --protocol lambda --notification-endpoint arn:aws:lambda:us-east-1:821711655051:function:lambda-lifecycle

6. Check that the trigger is present in Lambda, create if necessary

7. Test the lifecycle hook by terminating an EC2 instance (change the desired capacity to 0)

