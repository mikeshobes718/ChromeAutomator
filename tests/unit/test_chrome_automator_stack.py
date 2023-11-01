import aws_cdk as core
import aws_cdk.assertions as assertions

from chrome_automator.chrome_automator_stack import ChromeAutomatorStack

# example tests. To run these tests, uncomment this file along with the example
# resource in chrome_automator/chrome_automator_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ChromeAutomatorStack(app, "chrome-automator")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
