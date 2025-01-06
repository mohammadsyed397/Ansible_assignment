#!/usr/bin/env python3

import json

def main():
    inventory = {
        "_meta": {
            "hostvars": {
                "target-1": {
                    "ansible_host": "ip address of instance",
                    "ansible_connection": "ssh",
                    "ansible_user": "ubuntu",
                    "ansible_ssh_private_key_file": "./munna.pem"
                },
                "target-2": {
                    "ansible_host": "ip address of instance",
                    "ansible_connection": "ssh",
                    "ansible_user": "ubuntu",
                    "ansible_ssh_private_key_file": "./munna.pem"
                },
                "target-4": {
                    "ansible_host": "ip address of instance",
                    "ansible_connection": "ssh",
                    "ansible_user": "ubuntu",
                    "ansible_ssh_private_key_file": "./munna.pem"
                },
                "target-5": {
                    "ansible_host": "ip address of instance",
                    "ansible_connection": "ssh",
                    "ansible_user": "ubuntu",
                    "ansible_ssh_private_key_file": "./munna.pem"
                }
            }
        },
        "web_servers": {
            "hosts": ["target-1", "target-2"]
        },
        "db_servers": {
            "hosts": ["target-4", "target-5"]
        }
    }

    print(json.dumps(inventory, indent=2))

if __name__ == '__main__':
    main()

