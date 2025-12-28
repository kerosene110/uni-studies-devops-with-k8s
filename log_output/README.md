# Log output app

## Exercise 1.3

How to deploy

```
docker build -t log-output:latest . # Use local image
kubectl apply -f ./manifests/deployment.yaml
```

## Exercise 1.3 Output

```
$ kubectl logs log-output-dep-747cbb96-f8wfv --follow
2025-12-28T17:32:50.812Z: 0.u4xalzffoc
2025-12-28T17:32:55.936Z: 0.u4xalzffoc
```