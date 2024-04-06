import boto3
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info('Received event: %s', event)

    # Parse the SNS message payload
    message = event['Records'][0]['Sns']['Message']
    logger.info('Received message: %s', message)

    try:
        message_data = json.loads(message)
    except json.JSONDecodeError:
        logger.error('Unable to decode message payload')
        return

    instance_id = message_data['EC2InstanceId']
    logger.info('Instance ID: %s', instance_id)

    # Create an EC2 resource and get the instance object
    ec2 = boto3.resource('ec2')
    instance = ec2.Instance(instance_id)

    # Get the instance's root EBS volume ID
    root_device = instance.block_device_mappings[0]
    volume_id = root_device['Ebs']['VolumeId']
    logger.info('Volume ID: %s', volume_id)

    # Create a snapshot of the root EBS volume
    snapshot = ec2.create_snapshot(VolumeId=volume_id, Description='Auto Scaling Group snapshot')

    logger.info('Snapshot created: %s', snapshot.id)
