# k8s-sona-ansible
An automated installation script used for installing Kubernetes, Docker, OVS, ONOS, SONA-CNI and Helm.

## Installation
Requirements
- OS: CentOS 7.6
- Network: Two network interfaces
- Nodes: 1 master node, n worker nodes

1. Install ansible at all nodes.
```
# yum install ansible git -y
```

2. Generate RSA key at master node. Make sure do not create any passphrase.
```
# ssh-keygen -t rsa
```

3. Copy distribute RSA public key to all worker nodes.
```
# ssh-copy-id root@worker1~n
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
192.168.56.102

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
