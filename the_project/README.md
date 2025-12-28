# 1.2. The project, step 1

> Instructions
> Let's get started!

> Create a web server that outputs "Server started in port NNNN" when it is started and deploy it into your Kubernetes cluster. Please make it so that an environment variable PORT can be used to choose the used port. You may call the server todo app since it will, amongst other things, provide the functionality of a todo application pretty soon.

> You will not have access to the port when it is running in Kubernetes yet. We will configure the access when we get to networking.

## Solution

```
docker build -t todo-app:latest . # build the app locally
k3d image import todo-app:latest   # Use the local image with k3d
kubectl create deployment todo-app-dep --image=todo-app:latest # Deploy the local image
kubectl patch deployment todo-app-dep -p '{"spec":{"template":{"spec":{"containers":[{"name":"todo-app","imagePullPolicy":"IfNotPresent"}]}}}}' # Allow local image
kubectl logs deployment/todo-app-dep
```

Output:

```
$ kubectl patch deployment todo-app-dep -p '{"spec":{"template":{"spec":{"containers":[{"name":"todo-app","imagePullPolicy":"IfNotPresent"}]}}}}' # Allow local image
deployment.apps/todo-app-dep patched

$ kubectl logs deployment/todo-app-dep
Server started in port 8000
```
