[![travis_build](https://travis-ci.org/sonaproject/k8s-sona-ansible.svg?branch=master)](https://travis-ci.org/sonaproject/k8s-sona-ansible)

# k8s-sona-ansible
An automated installation script used for installing Kubernetes, Docker, OpenvSwitch, ONOS, SONA-CNI and Helm.

## Requirements
- Operating System
  - CentOS 7.6 (kernel: 3.10.0-957)
  - Ubuntu 16.04, 18.04 (LTS)
- Network:
  - Primary (internal): management, tunneling
  - Secondary (external): NodeIP, routing
- Nodes: 
  - 1 master node
  - 0 ~ n worker nodes
  
## Components to be installed
- Mandatory
  - Kubernetes with Dashboard
  - ONOS with SONA-CNI
  - OpenvSwitch
  - Docker
- Optional
  - Helm
  - Healthcheck

## Installation
1. Install ansible and git at master node.

CentOS:
```
# yum install ansible git -y
```
Ubuntu:

16.04:

If you are running Ubuntu 16.04, the pre-installed ansible does not support multi-tasks, and this in turn causes runtime failure. To resolve this issue, the users need to following [this guide](https://github.com/sonaproject/k8s-sona-ansible/wiki/Guides-of-upgrading-ansible-package-on-Ubuntu-16.04) to upgrade ansible to higher version.

18.04 or higher:

If you are running Ubuntu 18.04 or higher version, no need to manually upgrade ansible.
```
# apt-get install ansible git -y
```

2. Generate RSA key at master node. Make sure do not create any passphrase.
```
# ssh-keygen -t rsa
```

3. Configure the hostname of each node. Run following command at each node to configure the hostname.
```
# hostnamectl set-hostname $node-name
```
(Optional) Add configured hostname and IP address pair to /etc/hosts at master node.
Followings are the example configuration.
```
master  192.168.56.101
worker  192.168.56.201
```

3. Copy RSA public key from master node and distribute to all nodes (master + worker).
```
# ssh-copy-id root@$node-name
```

4. Clone ```k8s-sona-ansible``` script at master node.
```
# git clone https://github.com/sonaproject/k8s-sona-ansible.git
```

5. Add ```hosts.ini``` by referring to the example config from ```inventory/default/hosts.ini.example```.
```
[master]
192.168.56.101

[worker]
192.168.56.201

[cluster:children]
master
worker
```

6. Add ```all.yml``` by referring to the example config from ```inventory/default/group_vars/all.yml.example```.
Make sure you have configured the correct ```external_interface```, and ```external_gateway_ip```. Typically we use secondary network as the external network. It is also possible to install optional packages (e.g., helm, healthcheck) by toggling the flag to ```true``` at ```all.yml```.

7. Run ansible script at master node.
```
# ansible-playbook inventory/default/site.yml
```

8. Enjoy!

## Site Reset
In case you would like to reset the entire environments, run following ansible script at master node.
Note that site reset does not uninstall Kubernetes, OpenvSwitch and Docker.
```
# ansible-playbook inventory/default/reset-site.yml
```

## Important Pointers
* For latest updates, visit [project page](https://github.com/sonaproject/sona-cni).
* For manually installation, visit [installation page](https://wiki.onosproject.org/display/ONOS/SONA-CNI+Installation)
* Report bugs or new requirement(s) on the [bug page](https://github.com/sonaproject/k8s-sona-ansible/issues).
* Any contribution is appreciated.
* Start contributing and enjoy ;)

## License
[Apache 2.0](https://github.com/sonaproject/k8s-sona-ansible/blob/master/LICENSE)
