# Ansible_assignment
# DEPLOY of EC2_INSTANCE:
- in the deploy_server.yml i had created two ec2 instances using ansible to deploy a web application on to these two servers
- we need to encrypt the vars.yml file as we are sharing sensitive information like access key and seceret key
- command to encyrpt the vars.yml 
- ansible-vault encrypt vars.yml
- during execution
- ansible-playbook ---ask-vault-password deploy_server.yml
- if we want to modify the information in vars.yml we can edit the vars.yml file using the below command
- ansible-vault edit vars.yml
# Install dependencies
- we have installed necessary dependencies on target severs using Ansible playbooks
  # ROLES
  - created roles for flask_web and mysql_db
  # configure application'
  - configured application using the roles flask_web and mysql_db 




