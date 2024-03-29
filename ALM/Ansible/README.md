# LXD/LXC

## [Instalación](lxd-setup.md)

# Ansible

### Ubuntu
```bash
apt install ansible
```

## Comandos

### ansible-inventory
```bash
ansible-inventory [--inventory <invent-file>] [--output <output-file>] [--yaml | --toml] --list
ansible-inventory [--inventory <invent-file>] [--vars] --graph
ansible-inventory [--inventory <invent-file>] --host <host>
```


### ansible-playbook
```bash
ansible-playbook [--inventory <inventory-file>] [--limmit <alias-en-inventario>] [--extra-vars '{"var":"val",...}'] [--step] [--check] [--syntax-check] <playbook.yaml> [-v]
```



### ansible
```bash
ansible <target> [-i <invent-file>] [-m <modulo>] [-a <argumentos>]
    algunos modulos:
        command # default
        shell
        script
        ping
        setup   # facts
    ejemplos:
        -a "/sbin/reboot"
        -m ansible.builtin.copy -a "src=/etc/hosts dest=/tmp/hosts"
        -m ansible.builtin.apt -a "name=acme state=present"
        -m ansible.builtin.user -a "name=nombre_usuario password=mipass"
        -m ansible.builtin.service -a "name=httpd state=started"
```

Leer facts con filtro:
```bash
ansible <target> [-i <invent-file>] -m setup -a "filter=patron_filtro"
```

Usar facts:
```bash
{{ ansible_facts.nombre_propiedad }}
```

### ansible-doc
```bash
ansible-vault --list | <modulo>
```

[ansible-vault](playbook/vault.md)
