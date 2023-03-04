# .dev

The purpose of this folder is to contain scripts and other references that are used to build and
maintain the project.

## Prerequisites

Add this to your `~/.bashrc` or `~/.zshrc`:

```bash
export PATH="<...>/not-reddit/.dev:$PATH"
```

### Create virtual environment

```bash
python3 -m venv .venv
```

### Activate virtual environment

```bash
. activate-venv.sh
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Docker

### Clean dangling images

```bash
docker image prune -f
```
