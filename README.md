# Cookiecutter Ansible Role

[![Build Status](https://travis-ci.org/jobcespedes/cookiecutter-ansible-role.svg?branch=master)](https://travis-ci.org/jobcespedes/cookiecutter-ansible-role)

[Cookiecutter](https://github.com/audreyr/cookiecutter) recipe to easily create [ansible roles](http://docs.ansible.com/playbooks_roles.html#roles).
This is a fork from [ferrarimarco/cookiecutter-ansible-role](https://github.com/ferrarimarco/cookiecutter-ansible-role)

## Features

1. Follows Ansible [best practices](http://docs.ansible.com/playbooks_best_practices.html)
1. Follows Ansible Galaxy [best practices](https://galaxy.ansible.com/intro#good)
1. Only Creates the necessary files and folders
1. Blazing fast creation, forget about file creation and focus in actions
1. Lint checks ([Ansible-lint](https://github.com/willthames/ansible-lint), [yamllint](https://github.com/adrienverge/yamllint))
1. Travis-CI integration ready, with support for parallel builds: ([.travis.yml]({{cookiecutter.role_name}}/.travis.yml), [badges in README.md for development and master branches]({{cookiecutter.role_name}}/README.md))

## Usage

1. Install [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html#install-cookiecutter): `pip install cookiecutter`
1. `cookiecutter https://github.com/jobcespedes/cookiecutter-ansible-role`

It will ask you questions about the structure of your role like tasks names, handlers names, and default variables. You can jump to the next question by entering an empty string.

## Test the generated role

See [README.md of the generated role]({{cookiecutter.role_name}}/README.md).

## Example
```
    ROLE CONFIGURATION:
    ===================

    Should it have tasks?  [Y/n]
      Add task name i.e (Install packages) Add some task
      Add task name i.e (Install packages) another task
      Add task name i.e (Install packages)

    Should it have handlers? [Y/n]
      Add handler name i.e (Restart uwsgi) restart something
      Add handler name i.e (Restart uwsgi) alert someone
      Add handler name i.e (Restart uwsgi)

    It should contain default variables?:  [Y/n]
      Add variable i.e (operator: : drunken_master) var: name
      Add variable i.e (operator: : drunken_master)

    Should it have meta info?  [Y/n]
     - Should it have dependencies?  [Y/n]
        Add dependency i.e ({role: aptsupercow, var: 'value'}) {role: cool, version: latest}
        Add dependency i.e ({role: aptsupercow, var: 'value'})

    Should it have templates?  [Y/n] n

    Should it have files?  [Y/n] y

```
