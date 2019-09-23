#!/usr/bin/env python
from __future__ import unicode_literals, absolute_import, print_function

import os
import shutil
from collections import OrderedDict
from cookiecutter.prompt import read_user_yes_no

try:
    input = raw_input
except NameError:
    pass


folders = OrderedDict()

defaults_folder_name = 'defaults'
main_file_name = 'main.yml'

folders['tasks']= {
    'question': '\nShould it have tasks? ',
    'hint': '  Add task name i.e (Install packages) ',
    'action': '- name: {}\n  # TODO\n\n',
    'file_name': main_file_name
}

folders['handlers'] = {
    'question': '\nShould it have handlers?',
    'hint': '  Add handler name i.e (Restart uwsgi) ',
    'action': '- name: {}\n  # TODO\n\n',
    'file_name': main_file_name
}

folders[defaults_folder_name] = {
    'question': '\nShould it contain default variables?: ',
    'hint': '  Add variable i.e (operator: drunken_master) ',
    'action': '{}\n\n',
    'file_name': main_file_name
}

folders['meta']= {
    'question': '\nShould it have meta info? ',
    'pre_hint': ' - Should it have dependencies? ',
    'pre_action': '\ndependencies:\n',
    'hint': '    Add dependency i.e ({role: aptsupercow, var: \'value\'}) ',
    'action': '  - {}\n',
    'file_name': main_file_name
}

folders['templates'] = {
    'question': '\nShould it have templates? ',
}

folders['files'] = {
    'question': '\nShould it have files? ',
}

ansible_role_name = '{{ cookiecutter.role_name }}'

def configure_role():
    print('\n\nROLE CONFIGURATION:\n===================')
    for folder_name, folder in folders.items():
        if read_user_yes_no(folder['question'], default_value=u'yes'):

            # try:
            #     # this file has to be there, git doesn't store empty folders.
            #     os.remove(os.path.join(folder_name, '.empty'))
            # except OSError:
            #     pass

            if 'hint' in folder:
                file_name = folder['file_name']
                with open('{}/{}'.format(folder_name, file_name), 'a') as fp:

                    if 'pre_hint' in folder:
                        if read_user_yes_no(folder['pre_hint'], default_value=u'yes'):
                            fp.write(folder['pre_action'])
                        else:
                            continue

                    action_name = input(folder['hint'])
                    while action_name:
                        if folder_name == defaults_folder_name:
                            fp.write(ansible_role_name.replace('.', '_') + '_' + folder['action'].format(action_name))
                        else:
                            fp.write(folder['action'].format(action_name))
                        action_name = input(folder['hint'])

        else:
           shutil.rmtree(folder_name)


if __name__ == '__main__':
    configure_role()
