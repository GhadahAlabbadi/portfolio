"""All text on the site.

To change any wording, edit it here.
"""

PROFILE = {
    "email": "ghadah.au4@gmail.com",
    "github": "https://github.com/GhadahAlabbadi",
    "linkedin": "https://www.linkedin.com/in/ghadah-alabbadi",
    "linkedin_handle": "ghadah-alabbadi",
    "emaa_demo": "https://emaa-expo.onrender.com",
    # Web3Forms access key: messages from the contact form go straight to the email above.
    # Leave it empty to fall back to opening the visitor's email app.
    "web3forms_key": "",
}

CERT_LINKS = {
    "ccna": "https://www.netacad.com/courses/ccna-introduction-networks?courseLang=en-US",
    "oracle_exam": "https://education.oracle.com/product/pexam_1Z0-006",
    "languagecert": "https://selt.languagecert.org/",
    "blockchain": "https://updraft.cyfrin.io/courses/blockchain-basics",
    "python_mega": "https://www.udemy.com/course/the-python-mega-course/",
    "fullstack": "https://www.coursera.org/learn/fullstack-web-development",
    "oracle_db": "https://academy.oracle.com/en/solutions-curriculum-database.html",
}

TECH = [
    {"short": "Py", "color": "#3776ab", "name": "Python", "kind": "Language"},
    {"short": "Dj", "color": "#0c4b33", "name": "Django", "kind": "Web framework"},
    {"short": "DRF", "color": "#a30000", "name": "Django REST", "kind": "APIs"},
    {"short": "Fl", "color": "#02569b", "name": "Flutter", "kind": "Mobile"},
    {"short": "Da", "color": "#0175c2", "name": "Dart", "kind": "Language"},
    {"short": "Jv", "color": "#e76f00", "name": "Java", "kind": "Language"},
    {"short": "JS", "color": "#b58900", "name": "JavaScript", "kind": "Language"},
    {"short": "Fb", "color": "#f57c00", "name": "Firebase", "kind": "Backend"},
    {"short": "My", "color": "#00758f", "name": "MySQL", "kind": "Database"},
    {"short": "Or", "color": "#c74634", "name": "Oracle", "kind": "Database"},
    {"short": "BI", "color": "#c9a000", "name": "Power BI", "kind": "Data"},
    {"short": "Git", "color": "#f05032", "name": "Git and GitHub", "kind": "Tools"},
]


CONTENT = {
    "meta_title": "Ghadah Alabbadi | Software Developer",
    "meta_description": (
        "Portfolio of Ghadah Alabbadi, a Computer Science graduate in Riyadh building "
        "bilingual web and mobile products with Python, Django and Flutter."
    ),
    "skip": "Skip to content",
    "nav": [
        ("about", "About"),
        ("projects", "Projects"),
        ("journey", "Journey"),
        ("certificates", "Certificates"),
        ("contact", "Contact"),
    ],
    "status": "Open to work",
    "menu_open": "Open menu",
    "menu_close": "Close menu",
    "theme_light": "Switch to light mode",
    "theme_dark": "Switch to dark mode",
    "hero": {
        "eyebrow": "Software developer, Riyadh",
        "first": "Ghadah",
        "last": "Alabbadi",
        "roles": ["Python and Django developer", "Java developer", "Flutter developer"],
        "intro": (
            "Computer Science graduate (First Class Honours) building bilingual web and "
            "mobile products with Django and Flutter, with a strong interest in FinTech."
        ),
        "projects_btn": "View projects",
        "cv_btn": "Download CV",
        "badge_icon": "1st",
        "badge_title": "Best project",
        "badge_sub": "Expo Hackathon 2026",
        "scroll": "Scroll",
    },
    "marquee": ["Software Developer", "Django", "Flutter", "Accessibility", "FinTech", "Bilingual UX"],
    "about": {
        "eyebrow": "About me",
        "before": (
            "I am a Computer Science graduate from Princess Nourah University who builds "
            "with Python, Django and Flutter. I turn real needs into "
        ),
        "highlight": "products people can use on day one",
        "after": ", from an award-winning accessibility app to a full service-management platform.",
        "orbit_caption": "My everyday stack, always in orbit",
    },
    "projects": {
        "title_before": "Selected ",
        "title_em": "projects",
        "title_after": " /",
        "enlarge": "Enlarge the {name} poster",
        "items": [
            {
                "tag": "Expo Hackathon winner",
                "name": "EMAA Expo",
                "text": (
                    "An accessibility companion for Deaf and non-speaking visitors of Expo 2030 "
                    "Riyadh, with a Saudi Sign Language avatar, visit planning and communication "
                    "tools. Ranked in the Top 12 out of 80+ projects, and best project in the Smart "
                    "Visitor Experience track."
                ),
                "chips": ["Django REST", "Flutter", "Figma"],
                "link": PROFILE["emaa_demo"],
                "link_label": "Open live demo",
                "poster": "img/poster-emaa-expo.webp",
                "alt": "EMAA Expo poster: the exhibition in your language, beyond spoken words, with app screens",
            },
            {
                "tag": "Capstone, Tuwaiq Academy",
                "name": "EnterpriseFlow",
                "text": (
                    "A bilingual platform for service cases, SLA deadlines and vendor contracts, "
                    "with four roles, dashboards, CSV reports and 108 automated tests."
                ),
                "chips": ["Python", "Django", "SQLite", "JavaScript"],
                "link": None,
                "link_label": "",
                "poster": "img/poster-enterpriseflow.webp",
                "alt": "EnterpriseFlow poster: every case, on time, with the manager dashboard",
            },
            {
                "tag": "Front-end, Tuwaiq Academy",
                "name": "SkyRoute Travel",
                "text": (
                    "A responsive travel website with booking and contact forms, built with "
                    "Flexbox, CSS Grid, media queries and animations."
                ),
                "chips": ["HTML5", "CSS3"],
                "link": None,
                "link_label": "",
                "poster": "img/poster-skyroute.webp",
                "alt": "SkyRoute Travel poster: plan the trip, book the flight, with the home page and booking form",
            },
        ],
    },
    "journey": {
        "title_before": "My ",
        "title_em": "journey",
        "tabs": ["Experience", "Education", "Tech stack"],
        "experience": [
            {
                "date": "08/2026 – 01/2027",
                "title": "Lab Instructor",
                "place": "Princess Nourah bint Abdulrahman University",
                "text": "Teach the lab sections of Java Programming 1, Advanced Programming (Java) and Software Engineering.",
            },
            {
                "date": "01/2026 – 04/2026",
                "title": "Co-op Trainee",
                "place": "Saudi Data and AI Authority (SDAIA)",
                "text": "Project management and documentation, UI design for the Digital Twin project, and Power BI dashboards.",
            },
        ],
        "education": [
            {
                "date": "07/2026 – 10/2026",
                "title": "Web Application Development Using Python",
                "place": "Tuwaiq Academy bootcamp",
                "text": "Python, OOP, HTML and CSS, Django and relational database design. Finished with the EnterpriseFlow capstone.",
            },
            {
                "date": "08/2022 – 05/2026",
                "title": "BSc in Computer Science",
                "place": "Princess Nourah bint Abdulrahman University",
                "text": "First Class Honours, GPA 4.95 out of 5.",
            },
        ],
    },
    "certs": {
        "title_before": "Certificates ",
        "title_em": "&",
        "title_after": " courses",
        "certs_label": "Certificates",
        "courses_label": "Courses",
        "certs": [
            {"name": "CCNAv7: Introduction to Networks", "by": "Cisco Networking Academy", "date": "", "url": CERT_LINKS["ccna"]},
            {"name": "Oracle 1Z0-006 Exam", "by": "Oracle", "date": "", "url": CERT_LINKS["oracle_exam"]},
            {"name": "LanguageCert International ESOL", "by": "LanguageCert", "date": "", "url": CERT_LINKS["languagecert"]},
        ],
        "courses": [
            {"name": "Blockchain Basics", "by": "Cyfrin Updraft", "date": "06/2026", "url": CERT_LINKS["blockchain"]},
            {"name": "Python Mega Course: Build 20 Real-World Apps and AI Agents", "by": "Udemy", "date": "10/2025", "url": CERT_LINKS["python_mega"]},
            {"name": "Full Stack Web Development", "by": "Amazon, on Coursera", "date": "10/2025", "url": CERT_LINKS["fullstack"]},
            {"name": "Database Foundations", "by": "Oracle Academy", "date": "10/2023", "url": CERT_LINKS["oracle_db"]},
        ],
    },
    "contact": {
        "eyebrow": "Get in touch",
        "title_before": "Let's build ",
        "title_em": "something",
        "title_after": " together.",
        "email": "Email",
        "linkedin": "LinkedIn",
        "location": "Location",
        "location_value": "Riyadh, Saudi Arabia",
        "copy": "Copy",
        "copied": "Copied",
        "selected": "Selected",
        "name_label": "Your name",
        "name_ph": "Sara",
        "email_label": "Email address",
        "email_ph": "sara@company.com",
        "msg_label": "Message",
        "msg_ph": "Hi Ghadah, we have a role that fits you...",
        "send": "Send message",
        "note": "Your email app will open with the message ready to send.",
        "sending": "Sending...",
        "sent": "Thanks, your message was sent. I'll get back to you soon.",
        "error": "Your message couldn't be sent. Please try again, or email me directly.",
        "subject": "Message from your portfolio",
    },
    "footer": {
        "before": "Let's build ",
        "em": "the future.",
        "rights": "Ghadah Alabbadi",
        "built": "Built with Django",
    },
    "lightbox_label": "Project poster",
    "close": "Close",
    "not_found": {
        "meta": "Page not found",
        "eyebrow": "Error 404",
        "title_before": "Lost in ",
        "title_em": "orbit",
        "text": "This page drifted out of orbit, or it never existed. Let's get you back on course.",
        "home": "Back home",
        "projects": "View projects",
    },
    "tech": TECH,
}
