# Ansible Role: {{cookiecutter.role_name}}

* Development branch: [![Build Status](https://travis-ci.org/{{cookiecutter.github_user}}/{{cookiecutter.repo_name}}.svg?branch=development)](https://travis-ci.org/{{cookiecutter.github_user}}/{{cookiecutter.repo_name}})
* Master branch: [![Build Status](https://travis-ci.org/{{cookiecutter.github_user}}/{{cookiecutter.repo_name}}.svg?branch=master)](https://travis-ci.org/{{cookiecutter.github_user}}/{{cookiecutter.repo_name}})

{{cookiecutter.short_description}}

## Using the role
### Installation
```
ansible-galaxy install {{ cookiecutter.role_name }}
```

### Example Playbook
```
  - hosts: all
    roles:
      - {{ cookiecutter.role_name }}
```

## Testing the role

### Dependencies
- Bundler 1.13.0+
- Ruby 2.3.0+
- Docker 1.12.0+

(may work with older versions)

### Setup
1. Install the necessary tools: [test/scripts/test-role.sh](test/scripts/before-install.sh)
1. Install required gems from inside the root of the project: [test/scripts/test-role.sh](test/scripts/install.sh)
1. Run lint checks and tests: [test/scripts/test-role.sh](test/scripts/test-role.sh)

Note that after installing the required gems you can run other Test-kitchen commands besides the ones listed in [test/scripts/test-role.sh](test/scripts/test-role.sh).

### Parallel test execution

See [test/scripts/test-role.sh](test/scripts/test-role.sh).
