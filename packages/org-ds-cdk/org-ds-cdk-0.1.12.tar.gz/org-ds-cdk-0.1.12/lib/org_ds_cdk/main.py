# main_stack.py
from constructs import Construct
from aws_cdk import (
    Stack,
    CfnOutput,
    Environment,
)
from .vpc import VpcConstruct
from .apigateway import ApiGatewayConstruct
from .multilambda import MultiLambdaConstruct
#from org_ds_cdk import (ApiGatewayStack, 
#                        MultiLambdaStack)

class MainStack(Stack):
    def __init__(self, scope: Construct, id: str, config: dict, **kwargs):
        super().__init__(scope, id, **kwargs)
        """
        Initializes a new instance of the MainStack class.

        Args:
            scope (Construct): The parent construct.
            id (str): The construct ID.
            config_path (str): The path to the configuration file.
            **kwargs: Additional keyword arguments.

        Returns:
            None
        """
        # Create an instance of VpcConstruct
        vpc_construct = VpcConstruct(self, "VpcConstruct", config=config)

        # Create an instance of LambdaStack
        #multi_lambda_stack = MultiLambdaStack(self, "MultiLambdaStack", config=config)

        
        # # Add Lambda function names and ARNs as CloudFormation outputs
        # for function_name, function in multi_lambda_stack.lambda_functions.items():
        #     CfnOutput(self, f"{function_name}Name", value=function_name)
        #     CfnOutput(self, f"{function_name}Arn", value=function.function_arn)

        # # Create an instance of ApiGatewayStack with LambdaStack as a parameter
    
        # ApiGatewayStack(self, "ApiGateway", lambda_stack=multi_lambda_stack, config=config)