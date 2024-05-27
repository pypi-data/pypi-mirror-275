import yaml
import ipaddress

def load_config(file_path: str):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)
    


def generate_cidrs(cidr_block: str, az_count: int):
    network = ipaddress.ip_network(cidr_block)

    # Split the network into /24 subnets
    subnets = list(network.subnets(new_prefix=24))

    # Take the first az_count subnets for the public CIDRs
    public_cidrs = [str(subnet) for subnet in subnets[:az_count]]

    # Take the second half of the /16 network for the private CIDRs
    private_start = len(subnets) // 2
    private_cidrs = [str(subnet) for subnet in subnets[private_start:private_start+az_count]]

    return public_cidrs, private_cidrs    

