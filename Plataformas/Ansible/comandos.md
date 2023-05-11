```bash
ansible <target> [-i <invent-file>] -m <modulo>
    modulo:
        ping
        setup
```

ansible-inventory

ansible-playbook

ansible-doc

```bash
ansible-vault encrypt_string 'foobar' --name 'the_secret' --ask-vault-pass


export EDITOR=nano
ansible-vault create vault.yaml
ansible-vault view vault.yaml
ansible-vault edit vault.yaml

ansible-vault encrypt tasks.txt --output tasks.txt.enc
ansible-vault rekey tasks.txt.enc
ansible-vault decrypt tasks.enc.txt --output tasks2.txt

```