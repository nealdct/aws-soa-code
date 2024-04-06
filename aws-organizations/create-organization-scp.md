# Create SCP for Restricting EC2 Instance Types

1. In AWS Organizations, enable Service Control Policies (SCPs)
2. Create a policy called "RequireT2Micro"
3. Enter the following JSON code:

***Code for the SCP***

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "RequireMicroInstanceType",
      "Effect": "Deny",
      "Action": "ec2:RunInstances",
      "Resource": "arn:aws:ec2:*:*:instance/*",
      "Condition": {
        "StringNotEquals":{               	
          "ec2:InstanceType":"t2.micro"
        }
      }
    }
  ]
}

4. Attach the SCP to the OU that contains the dev account (OU1)
5. Switch roles to administer the dev account

## Switch role using:
Account number of the dev account
Role: OrganizationAccountAccess

6. In Amazon EC2 attempt to launch a t2.micro instance. It should work
7. Next, attempt to launch any other EC2 instance type. It should fail
8. Switch back to the management account, and attach the SCP to the Root OU
9. Attempt to launch a t2.medium instance. What happens?
