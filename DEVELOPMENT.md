# Development

This document describes the process for running this application on your local computer.

## Getting started

It is assumed you have these installed locally - `Docker`, `node`, `npm`, `Python`, `pip`.

[Make sure to add scripts to your `PATH` if you haven't already](.dev/README.md#prerequisites)
### API

```bash
postgres.sh
rabbitmq.sh
cd api
pip install -r src/test/requirements.txt # only the first time
. activate-venv.sh
. source-env.sh
services.sh

```

### Frontend

```bash
cd ui/src/main
npm install # only the first time
npm run dev
```