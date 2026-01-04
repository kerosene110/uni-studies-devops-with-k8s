# Log output app

## Exercise 1.7. External access with Ingress


Clean up the old cluster:

```
k3d cluster delete
k3d cluster create --port 8082:30080@agent:0 -p 8081:80@loadbalancer --agents 2
```

How to deploy:

```
docker build -t log-output:latest . # Use local image
k3d image import log-output:latest
kubectl apply -f ./manifests/deployment.yaml
kubectl apply -f ./manifests/service.yaml
kubectl apply -f ./manifests/ingress.yaml
```

## Exercise 1.7 Output

```
$ kubectl logs log-output-dep-747cbb96-w7jsm 
2026-01-04T18:59:17.898Z: xpvxy144lq
2026-01-04T18:59:22.898Z: xpvxy144lq

$ curl localhost:8081/status
"2026-01-04T20:11:59.986Z: fzzmj8ycrn"

```