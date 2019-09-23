Role Name: {{cookiecutter.role_name}}
=========

[![Build Status](https://travis-ci.org/{{cookiecutter.github_user}}/{{cookiecutter.repo_name}}.svg?branch=master)](https://travis-ci.org/{{cookiecutter.github_user}}/{{cookiecutter.repo_name}}) [![Buy me a coffee](https://img.shields.io/badge/$-BuyMeACoffee-blue.svg)](https://www.buymeacoffee.com/jobcespedes)

{{cookiecutter.short_description}}

Requirements
------------

- See [`requirements.txt`](requirements.txt)

Role Variables
--------------

- See [`defaults/main.yml`](defaults/main.yml).

Dependencies
------------

- Depends on other Ansible roles: no

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - {{github_user}}.{{ cookiecutter.role_name }}
```

License
-------

Apache 2.0

Author Information
------------------

{{cookiecutter.full_name}}: {{cookiecutter.email}}
