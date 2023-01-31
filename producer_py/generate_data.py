#!/usr/bin/env python

"""
Data Generator.

This program generates data which simulates AWS CLI
"""

from random import choice
import string


def generate_random(length=16):
    """Generate random alphanumerinc string."""
    characters = string.ascii_letters + string.digits
    password = "".join(choice(characters) for i in range(length))
    return password


def create_instances(num_devices=1, num_subnets=1):
    """Create AWS instances."""
    if num_devices > 254 or num_subnets > 254:
        print("Error: too many devices and/or subnets requested")

    for subnet_index in range(1, num_subnets + 1):
        for device_index in range(1, num_devices + 1):

            instances = dict()
            components = choice(['web', 'db', 'cache', 'kafka', 'cassandra'])
            instances["Name"] = f"production-{components}-{choice(string.digits)}"

            if components == "web":
                instances["ImageId"] = "ami-09246dnb00g7c4fef"
                instances["InstanceId"] = f"i-{generate_random(18)}"
                instances["Type"] = "m5.xlage"
                instances["EbsOptimized"] = choice(["true", "false"])
            elif components == "db":
                instances["ImageId"] = "ami-09267dnb00g7c4fef"
                instances["InstanceId"] = f"i-{generate_random(18)}"
                instances["Type"] = "db.r5.xlage"
                instances["EbsOptimized"] = choice(["true", "false"])
            elif components == "cache":
                instances["ImageId"] = "ami-09567dnb00g7c4fef"
                instances["InstanceId"] = f"i-{generate_random(18)}"
                instances["Type"] = "cache.r5.xlage"
                instances["EbsOptimized"] = choice(["true", "false"])
            elif components == "kafka":
                instances["ImageId"] = "ami-09767dnb00g7c4fef"
                instances["InstanceId"] = f"i-{generate_random(18)}"
                instances["Type"] = "r5.4xlage"
                instances["EbsOptimized"] = choice(["true", "false"])
            elif components == "cassandra":
                instances["ImageId"] = "ami-09667dnb00g7c4fef"
                instances["InstanceId"] = f"i-{generate_random(18)}"
                instances["Type"] = "i4.4xlage"
                instances["EbsOptimized"] = choice(["true", "false"])
            instances["PrivateDNS"] = "10.0." + str(subnet_index) + "." + str(device_index)
    return instances


if __name__ == '__main__':
    while True:
        create_instances(num_devices=20, num_subnets=4)
