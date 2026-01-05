# The project

## 1.8. The project, step 5

How to deploy with the local image:

```bash
k3d cluster delete # Clean up the clusters before
k3d cluster create --port 8082:30080@agent:0 -p 8081:80@loadbalancer --agents 2 # Create a new cluster

docker build -t todo-app:latest . # Update the image
k3d image import todo-app:latest # Update the container
kubectl apply -f manifests/deployment.yaml # Deploy the update
kubectl apply -f manifests/ingress.yaml 
kubectl apply -f manifests/service.yaml 
```

Optionally, restart the deployment:

```bash
kubectl rollout restart deployment/todo-app-dep
```

Output:

```
$ kubectl logs deployments/todo-app-dep 
Server started in port 8000

$ curl localhost:8081
"Todo app is running with Ingress"
```
