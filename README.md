Ansible Web Service Deployment

This repository contains an Ansible setup to deploy:

Nginx on Linux (with custom index page from Jinja2 template)

IIS on Windows (with custom web.config template)

A custom Ansible module (create_tmp_file)

Vault

Secrets are stored in group_vars/*/vault.yml.
Encrypt secrets using ansible-vault encrypt_string, e.g.:

ansible-vault encrypt_string 'myapikey' --name 'api_key'
ansible-vault encrypt_string 'MyP@ssw0rd!' --name 'iis_pool_password'


Deploy both Linux + Windows (from site.yml)
ansible-playbook -i inventory.ini site.yml -e env=dev --ask-vault-pass

Run Linux deployment (dev env):
ansible-playbook -i inventory.ini site.yml -e env=dev --tags linux --ask-vault-pass

Run Windows deployment (prod env):
ansible-playbook -i inventory.ini site.yml -e env=prod --tags windows --ask-vault-pass

Dry-run with diff:	
ansible-playbook -i inventory.ini site.yml -e env=dev --check --diff

Custom Module

Example usage of create_tmp_file:

- name: Create a test file
  create_tmp_file:
    name: test.json
    content: "this is a file"


inventory.ini

[linux_web]
linux1 ansible_host=192.168.56.101 ansible_user=ubuntu ansible_become=yes

[windows_web]
win1 ansible_host=192.168.56.102 ansible_user=Administrator ansible_password=YourPassword ansible_connection=winrm ansible_winrm_transport=basic ansible_winrm_server_cert_validation=ignore

Workflow

Clone repo and update inventory.ini with your host details.

Update group_vars/*/vars.yml with environment-specific variables.

Encrypt secrets with ansible-vault encrypt_string and update vault.yml.

Run site.yml for full deployment or individual playbooks for OS-specific deployment.
