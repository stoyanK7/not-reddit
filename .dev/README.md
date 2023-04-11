# Development

The purpose of this folder is to contain scripts and other references that are used to build and
maintain the project.

## Prerequisites

Add this to your `~/.bashrc` or `~/.zshrc`:

```bash
export PATH="<...>/not-reddit/.dev:$PATH"
```

## Useful scripts

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

## Docker

### Clean dangling images

```bash
docker image prune -f
```

## PyCharm

### Custom scope that hides unnecessary files

```bash
!file:*/__init__.py&&!file:.idea//*&&!file:*/.pytest_cache//*&&!file:*/.coverage&&!file:*/htmlcov//&&!file:*/.venv//
```