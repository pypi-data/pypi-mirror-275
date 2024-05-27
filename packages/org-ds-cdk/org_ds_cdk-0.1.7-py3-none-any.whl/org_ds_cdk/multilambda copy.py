from constructs import Construct
from aws_cdk import (
    Duration,
    Tags,
    aws_lambda as _lambda,
    aws_ec2 as ec2,
    aws_iam as iam
)
from .utils import load_config

class MultiLambdaConstruct(Construct):
    @property
    def lambda_functions(self):
        """Return the dictionary of Lambda functions."""
        return self._lambda_functions
    
    def __init__(self, scope: Construct, id: str, config: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        lambda_functions = config["LambdaFunctions"]

        # Create a dictionary to hold the Lambda functions
        self._lambda_functions = {}

        for function in lambda_functions:

            function_props = {}

            # Create an execution role for the Lambda function
            execution_role = iam.Role(self, f"Lambda_{function['name']}_ExecutionRole", 
                                      assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"))

            # Add required policies to the role
            execution_role.add_to_policy(iam.PolicyStatement(
                actions=["lambda:GetLayerVersion"],
                resources=['*']
            ))
            execution_role.add_to_policy(iam.PolicyStatement(
                actions=[
                    "logs:CreateLogGroup",
                    "logs:CreateLogStream",
                    "logs:PutLogEvents"
                ],
                resources=["arn:aws:logs:*:*:*"]
            ))            

            # Add dynamic properties if they exist
            if 'memorySize' in function:
                function_props['memory_size'] = function['memorySize']

            if 'timeout' in function:
                function_props['timeout'] = Duration.seconds(function['timeout'])

            if 'environment' in function:
                function_props['environment'] = function['environment']

            if 'securityGroup' in function:
                function_props['security_groups'] = function['securityGroup']

            if 'vpcId' in function and 'vpcSubnetIds' in function:
                # Perform VPC lookup using intrinsic functions for account ID and region
                vpc = ec2.Vpc.from_lookup(self, "VPC", vpc_id=function['vpcId'])
                function_props['vpc'] = vpc
                function_props['vpc_subnets'] = ec2.SubnetSelection(
                    subnets=[ec2.Subnet.from_subnet_id(self, f"Subnet{i}", subnet_id) 
                             for i, subnet_id in enumerate(function['vpcSubnetIds'])])
                    
            function_props.update({
                "function_name": function['name'],
                "runtime": getattr(_lambda.Runtime, function['runtime']),
                "handler": function['handler'],
                "code": _lambda.Code.from_asset(function['path']),
                "role": execution_role,
            })

            lambda_function = _lambda.Function(self, function['name'], **function_props)

            if 'layers' in function:
                for i, layer_arn in enumerate(function['layers']):
                    layer_version = _lambda.LayerVersion.from_layer_version_arn(self, f"Layer{i}_{function['name']}", layer_arn)
                    lambda_function.add_layers(layer_version)

            # Add tags to the Lambda functions  
            if 'tags' in function:
                for key, value in function['tags'].items():
                    Tags.of(lambda_function).add(key, value)       

            self._lambda_functions[function['name']] = lambda_function
