import json
import os

from django.contrib.staticfiles import finders
from django.shortcuts import render

from .content import CONTENT, PROFILE

CV_PATH = "files/Ghadah_Alabbadi_CV.pdf"


def _asset_version():
    """Changes whenever the CSS or JS changes, so browsers never use an old copy."""
    stamps = [os.path.getmtime(finders.find(f)) for f in ("css/site.css", "js/site.js")]
    return str(int(max(stamps)))


def _base_context():
    c = CONTENT
    return {
        "v": _asset_version(),
        "c": c,
        "p": PROFILE,
        "site_data": {
            "roles": c["hero"]["roles"],
            "email": PROFILE["email"],
            "subject": c["contact"]["subject"],
            "copy": c["contact"]["copy"],
            "copied": c["contact"]["copied"],
            "selected": c["contact"]["selected"],
        },
    }


def home(request):
    context = _base_context()
    c = context["c"]
    context["projects"] = [
        dict(item, enlarge=c["projects"]["enlarge"].format(name=item["name"]))
        for item in c["projects"]["items"]
    ]
    context["orbit_outer"] = ["Python", "Django", "JavaScript", "Flutter", "Figma", "Git", "Power BI"]
    context["orbit_inner"] = ["HTML", "Dart", "CSS", "REST", "SQL", "Java"]
    # The Download CV button appears once the PDF is saved in static/files/.
    context["cv_path"] = CV_PATH if finders.find(CV_PATH) else None
    return render(request, "home.html", context)


def emaa_expo(request):
    """Share link for EMAA Expo: shows a proper preview card on LinkedIn, then opens the live demo."""
    demo = PROFILE["emaa_demo"]
    return render(request, "emaa_expo.html", {
        "demo_url": demo,
        "demo_url_json": json.dumps(demo),
        "description": (
            "Accessibility companion app for Deaf and non-speaking visitors of Expo 2030 Riyadh. "
            "Top 12 out of 80+ projects and best project in the Smart Visitor Experience track."
        ),
    })


def not_found(request, exception=None):
    return render(request, "404.html", _base_context(), status=404)
