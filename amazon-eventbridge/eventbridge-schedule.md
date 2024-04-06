# Create a Lambda function with Nodejs 16 and the below code

exports.handler = async (event, context) => {
  const message = event['message'];
  console.log(message);
};


# Create an Eventbridge schedule with the following payload

{
  "message": "Hello from EventBridge!"
}
