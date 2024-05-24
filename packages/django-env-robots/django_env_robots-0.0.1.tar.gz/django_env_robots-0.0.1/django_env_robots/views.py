import os
from django.http import HttpResponse
from django.conf import settings
from django.template import Context, Template

DEFAULT_TEMPLATE = """
# Robots template: "{{ template }}" could not be found. Using default
User-agent: *
Disallow: /

{% for sitemap_url in sitemap_urls %}Sitemap: {{ sitemap_url }}
{% endfor %}
"""

def robots(request):

    sitemap_urls = []
    try:
        for sitemap_url in settings.ROBOTS_SITEMAP_URLS:
            sitemap_urls.append(f"{request.scheme}://{request.get_host()}{sitemap_url}")
    except AttributeError:
        pass

    context = Context({
        'scheme': request.scheme,
        'host': request.get_host(),
        'sitemap_urls': sitemap_urls,
    })

    robots_txt = os.path.join(settings.ROBOTS_ROOT, f"{settings.SERVER_ENV}.txt")
    try:
        with open(robots_txt, 'r') as rfile:
            content = rfile.read()
    except FileNotFoundError:
        content = DEFAULT_TEMPLATE
        context['template'] = robots_txt

    template = Template(content)
    response = template.render(context)
    return HttpResponse(response, content_type="text/plain")
