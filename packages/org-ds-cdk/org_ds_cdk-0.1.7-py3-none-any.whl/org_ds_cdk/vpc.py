from constructs import Construct
from aws_cdk import (
    aws_ec2 as ec2,
)
from .utils import generate_cidrs

class VpcConstruct(Construct):
    @property
    def vpc(self):
        """Return the VPC object."""
        return self._vpc
    @vpc.setter
    def vpc(self, vpc):
        self._vpc = vpc        
    @property
    def public_cidrs(self):
        """Return the list of public CIDR blocks."""
        return self._public_cidrs
    @property
    def private_cidrs(self):
        """Return the list of private CIDR blocks."""
        return self._private_cidrs

    def __init__(self, scope: Construct, id: str, config: dict, **kwargs):
        super().__init__(scope, id, **kwargs)

        project_name = config["global"]["projectName"]

        # Get the VPC configuration
        az_count = config.get("vpcConfig", {}).get("azCount", 1)
        addPrivSubnets = config.get("vpcConfig", {}).get("addPrivSubnets", False)
        cidr_block = config.get("vpcConfig", {}).get("cidrBlock", "10.0.0.0/16")

        # Generate the CIDR blocks for the subnets
        self._public_cidrs, self._private_cidrs = generate_cidrs(cidr_block, az_count)
    
        # Define subnet configuration
        subnet_config = []

        # Create public subnets
        subnet_config.append(ec2.SubnetConfiguration(
            name=f"Public",
            subnet_type=ec2.SubnetType.PUBLIC,
            cidr_mask=24
        ))

        # Create private subnets if private access is enabled
        if addPrivSubnets:
            subnet_config.append(ec2.SubnetConfiguration(
                name=f"Private",
                subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                cidr_mask=24
            ))

        # Create the VPC
        vpc = ec2.Vpc(self, f"{project_name}-VPC",
                      max_azs=az_count,
                      ip_addresses=ec2.IpAddresses.cidr(cidr_block),
                      subnet_configuration=subnet_config,
                      nat_gateways=az_count if addPrivSubnets else 0,
                      enable_dns_hostnames=True,
                      enable_dns_support=True
                      )

        self.vpc = vpc

        for i in range(az_count):
            self.assignSubnetCidr(f'PrivateSubnet{i+1}', self.private_cidrs[i])

        # Output the VPC ID
        self.vpc_id = vpc.vpc_id

    def assignSubnetCidr(self, subnet_name: str, cidr: str):
        cfn_subnet = self.vpc.node.try_find_child(subnet_name)
        if cfn_subnet is not None:
            cfn_subnet = cfn_subnet.node.try_find_child('Subnet')
            if cfn_subnet is not None:
                cfn_subnet.add_property_override('CidrBlock', cidr)

