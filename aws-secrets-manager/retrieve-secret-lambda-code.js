const AWS = require('aws-sdk');
const client = new AWS.SecretsManager();

exports.handler = async (event, context) => {
  try {
    const secretName = 'prod/sample-db'; // replace with your secret name
    const data = await client.getSecretValue({ SecretId: secretName }).promise();
    const secret = data.SecretString;

    console.log(secret); // Output the secret value to CloudWatch logs

    return {
      statusCode: 200,
      body: 'Successfully retrieved secret',
    };
  } catch (err) {
    console.error(err);
    return {
      statusCode: 500,
      body: 'Error retrieving secret',
    };
  }
};
