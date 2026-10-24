# Ghadah Alabbadi – Portfolio

My personal portfolio website, built with Django.

- Home page: `/`
- Preview of the "page not found" design: `/404/`

## Project structure

| Path | What it holds |
|---|---|
| `pages/content.py` | All the text on the site, plus the course and certificate links |
| `templates/` | Page layout (`base.html`, `home.html`, `404.html`, and `_sky.html` for the light mode sky) |
| `static/css/site.css` | Design: colours, type, layout and animation, for dark mode and the sunny light mode |
| `static/js/site.js` | Loader, starfield, typing roles, counters, poster lightbox, tabs, copy email, contact form |
| `static/img/` | Project posters and the favicon |
| `static/files/` | Save `Ghadah_Alabbadi_CV.pdf` here to show the Download CV button |

The site has no database. To change any text, edit `pages/content.py`.

The contact form opens the visitor's email app with the message ready to send to my email address.

## Run it locally (Windows PowerShell)

```powershell
cd C:\Users\ghada\Documents\Portfolio
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py runserver
```

Then open http://127.0.0.1:8000/

If PowerShell blocks the activate script, run this once and try again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

## Deploy on Render

1. Push the project to a GitHub repository.
2. In Render, choose **New > Blueprint** and select the repository. Render reads `render.yaml`.
   Or choose **New > Web Service** and set:
   - Build command: `bash build.sh`
   - Start command: `gunicorn config.wsgi:application`
   - Environment variables: `PYTHON_VERSION` = `3.12.7`, `DEBUG` = `False`, `SECRET_KEY` = a long random value
3. Render adds its own address to the allowed hosts automatically. For a custom domain, add it to `ALLOWED_HOSTS` as a comma-separated environment variable.

## Credits

Fonts from Google Fonts: Syne, Manrope and JetBrains Mono.
