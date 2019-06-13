## Django 与 Vue 的前后端分离示例

- 分离的配置: [Django 的 settings.py 文件](./myproject/api/myproject/settings.py)

  - 更改 settings 文件的 TEMPLATES 配置中 DIRS

  ```python
  TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['../appfront/dist'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
  ]
  ```

  - 配置 Django 项目中的静态资源文件路径

  ```python
  STATIC_URL = '/static/'

  # Add for vuejs

  STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "appfront/dist/static"),
  ]
  ```

- 运行须知
  - 配置 settings.py 文件中的 数据库信息
