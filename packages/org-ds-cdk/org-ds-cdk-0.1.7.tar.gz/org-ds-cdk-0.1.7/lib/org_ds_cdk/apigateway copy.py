from constructs import Construct
from .utils import load_config

from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
    CfnOutput
)


class ApiGatewayConstruct(Construct):
    def __init__(self, scope: Construct, id: str, lambda_stack, config: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        apiName = config["ApiGateway"]["apiName"]
        description = config["ApiGateway"]["description"]
        stageName = config["ApiGateway"]["stageName"]
        routes = config['ApiGateway']['routes']

        # Create an API Gateway
        api = apigateway.RestApi(self, "api",
            rest_api_name=apiName,
            description=description,
        )

        if routes is None:
            # Add a method to the root resource
            api.root.add_method('GET')  # GET is just an example, use the appropriate method

        else:
            # Create a dictionary to hold the resources for different paths
            resources = {}

            # Iterate over routes in the configuration
            for route in routes:
                # Split the path into individual parts
                path_parts = route['path'].strip('/').split('/')

                resource = api.root  # Start with the root resource

                # Create nested resources if needed
                for part in path_parts:
                    if part.startswith('{') and part.endswith('}'):
                        # If the part is a dynamic parameter, add it as a path parameter
                        resource = resource.add_resource(f"{{{part[1:-1]}}}")
                    else:
                        # If the part is a static path, add it as a resource
                        if part not in resources:
                            resources[part] = resource.add_resource(part)
                        resource = resources[part]

                # Iterate over the HTTP methods for the route
                for method in route['methods']:
                    if route['integration'] == 'lambda':
                        # If the integration type is Lambda, create a Lambda integration
                        integration = apigateway.LambdaIntegration(lambda_stack.lambda_functions[route['lambdaFunctionName']], proxy=True)
                    
                    # Add the method to the resource
                    resource.add_method(method, integration)

        CfnOutput(self, "ApiGatewayId",
            value=api.rest_api_id,
            description="API Gateway ID"
        )