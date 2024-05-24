# Django Env Robots (.txt)

Serve different robots.txt from your production | stage | etc servers by setting environment variables. Rules are managed via templates.


## Installation

Install from [PyPI](https://pypi.org/project/django-env-robots/):

```
pip install django-env-robots
```

Then add the following to your project's `INSTALLED_APPS`.

```
'django_env_robots',
```

## Usage

### settings.py
```
# robots
SERVER_ENV = Env.get('SERVER_ENV', 'production')
ROBOTS_ROOT = os.path.join(BASE_DIR, 'robots')
ROBOTS_SITEMAP_URLS = Env.list('ROBOTS_SITEMAP_URLS', '/sitemap.xml')
```

### urls.py
```
from django_env_robots import urls as robots_urls
...
urlpatterns = [
    path("robots.txt", include(robots_urls)),
]
```
### Other considertions

A robots.txt being served from a Whitenose public directory will win over this app. That is because of whitenoise's middleware behaviour - quite correct but watch out for that.
