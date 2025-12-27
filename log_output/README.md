# Log output app: 1.1. Getting started

Run the app with k8s deployment:

```
docker build -t log-output:latest . # build the app locally
k3d image import log-output:latest   # Use the local image with k3d
kubectl create deployment log-output-dep --image=log-output:latest # Deploy the local image
kubectl patch deployment log-output-dep -p '{"spec":{"template":{"spec":{"containers":[{"name":"log-output","imagePullPolicy":"IfNotPresent"}]}}}}' # Allow local image
kubectl logs deployment/log-output-dep --follow
```

## Optional: Cleanup

```
kubectl delete deployment log-output-dep
```

## Exercise 1.1 Output

```
$ kubectl logs deployment/log-output-dep --follow
2025-12-27T17:38:18.856Z: 0.53398fzusfr
2025-12-27T17:38:23.896Z: 0.53398fzusfr
2025-12-27T17:38:28.901Z: 0.53398fzusfr
2025-12-27T17:38:33.906Z: 0.53398fzusfr
2025-12-27T17:38:38.912Z: 0.53398fzusfr
2025-12-27T17:38:43.917Z: 0.53398fzusfr
2025-12-27T17:38:48.935Z: 0.53398fzusfr
2025-12-27T17:38:53.940Z: 0.53398fzusfr
2025-12-27T17:38:58.945Z: 0.53398fzusfr
2025-12-27T17:39:03.950Z: 0.53398fzusfr
```