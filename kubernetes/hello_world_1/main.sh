kubectl run --restart=Never --image=hello-world my-hello-world
while ! kubectl get pods my-hello-world 2>/dev/null | grep -q Completed; do sleep 1; done
kubectl logs my-hello-world
