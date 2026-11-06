# Hello Studio

## Deliberate startup-failure deployment test

This branch intentionally raises `RuntimeError` when `app.py` is imported.
The app cannot start or pass its `/` deployment health check. This tests
Builder's unhealthy-version handling; it is not a functional app release.
The normal route tests below are expected to fail during import on this branch.
Do not merge this change into the connected `python` branch.

The version active immediately before this test was
`ver_20261106_8023625683d8`; the redesigned working version is
`ver_20261106_be5e95adced6`. Inspect current app state before any recovery.

A responsive Flask greeting app with an ivory-and-forest design, a live name
preview, and personalized greeting cards. The interface uses local CSS and
JavaScript with system fonts; no frontend build or third-party assets are needed.
The greeting form works without JavaScript.

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python app.py
```

Open `http://localhost:8080`. Submit a name to create a greeting; use **Make
another hello** to return to the form. Empty submissions redirect home.

## Check behavior

```powershell
.\.venv\Scripts\python -m unittest -v
```

The app preserves the original `GET /`, `POST /hello`, and favicon routes.
Names are escaped by Jinja on the greeting page. The preview uses `textContent`,
not HTML, and remains decorative for screen readers. Responsive layouts, visible
keyboard focus, a skip link, and reduced-motion preferences are supported.

## Deployment

The existing App Service Builder app uses this repository's `python` branch.
UI changes on another branch do not change that source connection. Publishing
a branch and deploying it are separate operations; confirm the target and
deployment policy before changing the connected source.