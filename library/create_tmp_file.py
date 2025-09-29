#!/usr/bin/python
# -*- coding: utf-8 -*-
from ansible.module_utils.basic import AnsibleModule
import os
def run_module():
    module_args = dict(
        name=dict(type='str', required=True),
        content=dict(type='str', required=True),
        path=dict(type='str', required=False, default='/tmp')
    )
    result = dict(changed=False, message='', path='')
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)
    name = module.params['name']
    content = module.params['content']
    path = module.params['path']
    dest = os.path.join(path, name)
    result['path'] = dest
    if module.check_mode:
        if os.path.exists(dest):
            with open(dest, 'r') as f:
                existing = f.read()
            result['changed'] = (existing != content)
        else:
            result['changed'] = True
        module.exit_json(**result)
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
    if os.path.exists(dest):
        with open(dest, 'r') as f:
            existing = f.read()
        if existing == content:
            module.exit_json(changed=False, message='File already up-to-date', path=dest)
    with open(dest, 'w') as f:
        f.write(content)
    module.exit_json(changed=True, message='File written', path=dest)
def main():
    run_module()
if __name__ == '__main__':
    main()
