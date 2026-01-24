# Log output app

## Exercise 1.10 Even more services 

### Instructions

```
Split the "Log output" application into two different containers within a single pod:

One generates a random string on startup and writes a line with the random string and timestamp every 5 seconds into a file.
The other reads that file and provides the content in the HTTP GET endpoint for the user to see
```

### Solution

Clean up the old cluster:

```
k3d cluster delete
k3d cluster create --port 8082:30080@agent:0 -p 8081:80@loadbalancer --agents 2
```

How to deploy:

```
# Build images locally
docker build -f log-generator/Dockerfile -t log-generator log-generator 
docker build -f log-reader/Dockerfile -t log-reader log-reader
k3d image import log-generator:latest
k3d image import log-reader:latest

kubectl apply -f ./manifests/deployment.yaml
kubectl apply -f ./manifests/service.yaml
kubectl apply -f ./manifests/ingress.yaml
```

## Exercise 1.10 Output

```
$ kubectl logs log-output-dep-79bd7b86f7-5rcj8 
Defaulted container "log-generator" out of: log-generator, log-reader
2026-01-24T14:49:41.927Z: 1s7td4q0x0

$ curl localhost:8081/status
"OK"

$ curl localhost:8081/
2026-01-24T14:49:41.927Z: 1s7td4q0x0
2026-01-24T14:49:46.928Z: 1s7td4q0x0
2026-01-24T14:49:51.931Z: 1s7td4q0x0
2026-01-24T14:49:56.932Z: 1s7td4q0x0
2026-01-24T14:50:01.932Z: 1s7td4q0x0
2026-01-24T14:50:06.933Z: 1s7td4q0x0
```