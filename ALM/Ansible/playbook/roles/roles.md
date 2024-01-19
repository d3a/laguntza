[https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_reuse_roles.html#using-roles]

* Storing and finding roles

By default, Ansible looks for roles in the following locations:
- in collections, if you are using them
- in a directory called roles/, relative to the playbook file
- in the configured roles_path. The default search path is ~/.ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles.
- in the directory where the playbook file is located

If you store your roles in a different location, set the roles_path configuration option so Ansible can find your roles. Checking shared roles into a single location makes them easier to use in multiple playbooks. See Configuring Ansible for details about managing settings in ansible.cfg.

Alternatively, you can call a role with a fully qualified path:
```ansible
---
- hosts: webservers
  roles:
    - role: '/path/to/my/roles/common'
```


* Using roles


By default Ansible will look in each directory within a role for a main.yml file for relevant content (also main.yaml and main):
- tasks/main.yml - the main list of tasks that the role executes.
- handlers/main.yml - handlers, which may be used within or outside this role.
- library/my_module.py - modules, which may be used within this role (see Embedding modules and plugins in roles for more information).
- defaults/main.yml - default variables for the role (see Using Variables for more information). These variables have the lowest priority of any variables available, and can be easily overridden by any other variable, including inventory variables.
- vars/main.yml - other variables for the role (see Using Variables for more information).
- files/main.yml - files that the role deploys.
- templates/main.yml - templates that the role deploys.
- meta/main.yml - metadata for the role, including role dependencies and optional Galaxy metadata such as platforms supported.


You can use roles in three ways:
- at the play level with the roles option: This is the classic way of using roles in a play.
- at the tasks level with include_role: You can reuse roles dynamically anywhere in the tasks section of a play using include_role.
- at the tasks level with import_role: You can reuse roles statically anywhere in the tasks section of a play using import_role