# LXD

## Instalación

```bash
snap install lxd
lxd init
```

```yaml
config:
  core.https_address: '[::]:8443'
networks:
- config:
    ipv4.address: auto
    ipv6.address: auto
  description: ""
  name: lxdbr0
  type: ""
  project: default
storage_pools:
- config:
    size: 5GiB
  description: ""
  name: default
  driver: zfs
profiles:
- config: {}
  description: ""
  devices:
    eth0:
      name: eth0
      network: lxdbr0
      type: nic
    root:
      path: /
      pool: default
      type: disk
  name: default
projects: []
cluster: null
```



## Comandos

```bash
Available Commands:
  activateifneeded   Check if LXD should be started
  cluster            Low-level cluster administration commands
  help               Help about any command
  import             Command has been replaced with "lxd recover"
  init               Configure the LXD daemon
  recover            Recover missing instances and volumes from existing and unknown storage pools
  shutdown           Tell LXD to shutdown all containers and exit
  version            Show the server version
  waitready          Wait for LXD to be ready to process requests

Flags:
  -d, --debug     Show all debug messages
      --group     The group of users that will be allowed to talk to LXD
  -h, --help      Print help
      --logfile   Path to the log file
      --syslog    Log to syslog
      --trace     Log tracing targets
  -v, --verbose   Show all information messages
      --version   Print version number
```