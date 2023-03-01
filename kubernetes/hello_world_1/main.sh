kubectl run --restart=Never --image=hello-world my-hello-world
sleep 3
kubectl logs my-hello-world
