# coding=utf-8
from flask_script import Manager # class for handling a set of commands
from modules import app
import operator
# from flask import Flask
# import os
# from flask_migrate import Migrate, MigrateCommand
# from app import db, create_app
# from app import models

# app = create_app(config_name=os.getenv('APP_SETTINGS'))
# migrate = Migrate(app, db)
# manager = Manager(app)
#
# manager.add_command('db', MigrateCommand)


manager = Manager(app)

@manager.command
def routes():
    """Display registered route list"""

    print("Route list")
    headers = ('Action', 'Method', 'URI')
    dotted_lines = range(1, 111)
    blank_spaces = ''.join(' ' for _ in range(0, 37))
    print(''.join('-' for _ in dotted_lines))

    for index, header in enumerate(headers):
        if index == 0:
            print('| ' + header, end=(len(blank_spaces) - len(header)) * ' ' + '| ')
        elif index == 1:
            print(header, end=(len(blank_spaces) - len(header)) * ' ' + '| ')
        else:
            print(header, end=(len(blank_spaces) - len(header) - 7) * ' ' + '| ' + '\n')

    print(''.join('-' for _ in dotted_lines))
    rules = []
    for rule in app.url_map.iter_rules():
        methods = ', '.join(sorted(rule.methods))
        rules.append((rule.endpoint, methods, str(rule)))

    sort_by_rule = operator.itemgetter(2)
    for i, rule in enumerate(rules):
        for index, route_info in enumerate(sorted(rules, key=sort_by_rule)[i]):
            if index == 0:
                print('| ' + route_info, end=(len(blank_spaces) - len(route_info)) * ' ' + '| ')
            elif index == 1:
                print(route_info, end=(len(blank_spaces) - len(route_info)) * ' ' + '| ')
            else:
                print(route_info, end=(len(blank_spaces) - len(route_info) - 7) * ' ' + '| ' + '\n')

    print(''.join('-' for _ in dotted_lines))



if __name__ == "__main__":
    manager.run()
