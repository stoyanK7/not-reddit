# Development

The purpose of this folder is to contain scripts and other references that are used to build and
maintain the project.

---

## Prerequisites

Add this to your `~/.bashrc` or `~/.zshrc`:

```bash
export PATH="<...>/not-reddit/.dev:$PATH"
```

---

## Useful scripts

### Encode in base64

```bash
echo -n "blabla" | base64
```

### Create virtual environment

```bash
python3 -m venv .venv
```

### Activate virtual environment

Make sure you are in the `api` directory.

```bash
. activate-venv.sh
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Export dependencies

Make sure you are in the `api` directory.

```bash
export-deps.sh
```

### Run all services

Make sure you are in the `api` directory and virtual environment is activated.

```bash
services.sh
```

---

## Kubernetes

### Use with local images

```bash
eval $(minikube docker-env)
```

Then use `imagePullPolicy: Never`.

### Get contexts

```bash
kubectl config get-contexts

```

### Use context

```bash
kubectl config use-context <context>
```

---

## Docker

### Build images

From `api` directory:

```bash
docker build -t user -f src/main/user/Dockerfile .
```

### Clean dangling images

```bash
docker image prune -f
```

### Remove not-reddit images

```bash
docker rmi $(docker images | grep not-reddit | tr -s ' ' | cut -d ' ' -f 3)
```

---

## PyCharm

### Custom scope that hides unnecessary files

```bash
!file:*/__init__.py&&!file:.idea//*&&!file:*/.pytest_cache//*&&!file:*/.coverage&&!file:*/htmlcov//&&!file:*/.venv//
```
