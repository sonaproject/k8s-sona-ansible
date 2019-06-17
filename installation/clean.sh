kubectl delete statefulset atomix -n kube-system
kubectl delete statefulset onos -n kube-system
rm -rf /tmp/atomix-config
rm -rf /tmp/onos-config
