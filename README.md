# Ledge

## Overview

This is a simple web app for my personal finance needs.

**Frontend**: NuxtJS with Tailwind CSS

**Backend**: FastAPI

This project is currently WIP in early stages.

## Set-up instructions

### Dependencies

Python
- Python 3.10
- fastapi 0.71.0

JS
- Node v16.13.0
- Nuxt 2.15.7

### FastAPI

`config.toml` - create a configuration file using `config.toml.txt` as a template.

To start the FastAPI server, perform the following:

```bash
>>> cd backend
>>> ./Scripts/activate
>>> uvicorn main:app
```

### Nuxt

Note: dev only at the moment

```bash
>>> cd ledge-front
>>> npm run dev
```


