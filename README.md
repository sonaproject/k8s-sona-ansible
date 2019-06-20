# k8s-sona-ansible
An automated installation script used for installing Kubernetes, Docker, OVS, ONOS, SONA-CNI and Helm.

## Requirements
- OS: CentOS 7.6
- Kernel: 3.10.0-957
- Network:
  - Primary: management, tunneling
  - Secondary: NodeIP, routing
- Nodes: 
  - 1 master node
  - 1 worker node (multi-worker nodes case will be supported later)

## Components to be installed
- Mandatory
  - Kubernetes
  - ONOS with SONA-CNI
  - OpenvSwitch
  - Docker
- Optional
  - Helm

## Installation
1. Install ansible at all nodes.
```
# yum install ansible git -y
```

2. Generate RSA key at master node. Make sure do not create any passphrase.
```
# ssh-keygen -t rsa
```

3. Configure the hostname of each node. Run following command at each node to configure the hostname.
```
# hostnamectl set-hostname $node-name
```
Add configured hostname and IP address pair to /etc/hosts at master node.
Followings are the example configuration.
```
master  192.168.56.101
worker  192.168.56.201
```

3. Copy distribute RSA public key to all nodes (master + worker).
```
# ssh-copy-id root@$node-name
```

4. Clone k8s-sona-ansible script at master node.
```
# git clone https://github.com/sonaproject/k8s-sona-ansible.git
```

5. Configure the hosts.ini located under ```inventory/default/```.
```
[master]
192.168.56.101

[worker]
192.168.56.201

[cluster:children]
master
worker
```

6. Configure network related parameters via all.yml which is located under ```inventory/default/group_vars/```.
Make sure you have configured the correct ```external_interface```, and ```external_gateway_ip``` name.

7. Run ansible script at master node.
```
# ansible-playbook inventory/default/site.yml
```

8. Enjoy!
