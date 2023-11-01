from aws_cdk.core import Stack, Construct
from aws_cdk.aws_lambda import Function, Runtime, Code, LayerVersion
from aws_cdk.aws_lambda_python import PythonFunction

class CdkBrowserLambdaStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Define the Lambda function
        browser_function = PythonFunction(self, "BrowserFunction",
            entry=".deploy/",
            index="browser_handler.py",
            handler="lambda_handler",
            runtime=Runtime.PYTHON_3_9,
            memory_size=1024,
            timeout=core.Duration.seconds(30)
        )

        # Add the Chrome layer to the Lambda function
        chrome_layer = LayerVersion(self, "ChromeLayer",
            layer_version_name="chrome_aws_lambda_python39",
            compatible_runtimes=[Runtime.PYTHON_3_9],
            description="Layer containing headless Chrome binary for Python 3.9",
            license="Apache-2.0",
            # Replace with the ARN of the public layer for your region
            layer_version_arn="arn:aws:lambda:us-east-1:764866452798:layer:chrome-aws-lambda:22"
        )

        browser_function.add_layers(chrome_layer)
