# django-static-dm-file-uploader

Django application contains jquery dm-file-uploader plugin.

## Install

```shell
pip install django-static-dm-file-uploader
```

## Usage

*pro/settings.py*

```python
INSTALLED_APPS = [
    ...
    "django_static_dm_file_uploader",
    ...
]

```

*app/templates/view.html*

```django
{% load static %}

{% block header %}

<link rel="stylesheet" type="text/css" href="{% static "dm_file_uploader/css/jquery.dm-uploader.min.css" %}">
<script src="{% static "admin/js/vendor/jquery/jquery.js" %}"></script>
<script src="{% static "dm_file_uploader/js/jquery.dm-uploader.min.js" %}"></script>
<script src="{% static "admin/js/jquery.init.js" %}"></script>

{% endblock %}

```

## 开源协议

所有静态文件下载自：`https://github.com/danielm/uploader`。开源协议详见：`https://github.com/danielm/uploader/blob/master/LICENSE.txt`。

## Releases

### 1.0.2.2

- First release.

### 1.0.2.3

- Fix app name problem.
