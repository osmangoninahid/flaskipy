# coding=utf-8
from os.path import exists, realpath, dirname
from os import makedirs, chdir
from shutil import copy
import click
import inquirer
import inflect
from pprint import pprint

root_dir = dirname(realpath(__file__))
templates_dir = root_dir+'/flaskipy_templates'
p = inflect.engine()

@click.group()
def cli():
    pass


@cli.command()
def init():
    """Project structure initializer

    :return: None
    """
    try:
        answers = inquirer.prompt([inquirer.Text('name', message="What's your project name ? ")])
        __directory_creator(answers.get('name'))
        chdir(answers.get('name'))
        click.echo('Project structure initializing...')
        __directory_creator('utils')  # utilities package create
        __file_copier(templates_dir + '/__init__.txt', 'utils/__init__.py')
        __directory_creator('modules')  # models package create
        __file_copier(templates_dir + '/modules_init.txt', 'modules/__init__.py')
        __directory_creator('tests')  # tests package create
        __file_copier(templates_dir + '/__init__.txt', 'tests/__init__.py')
        __file_copier(templates_dir + '/config_ini.txt', 'config.ini')
        __file_copier(templates_dir + '/config.txt', 'config.py')
        __file_copier(templates_dir + '/main.txt', 'main.py')
        __file_copier(templates_dir + '/requirements.txt', 'requirements.txt')
        __file_copier(templates_dir + '/README.txt', 'README.md')

    except FileNotFoundError as fnf:
        print(str(fnf))
        exit(0)

    except Exception as ex:
        pprint(ex)
        exit(0)


def __directory_creator(dir_name):
    """Directory creator

    :param dir_name: str
        Name of the directory

    :return: Bool
    """
    if not exists(dir_name):
        # create directory
        makedirs(dir_name)

        return True

    else:
        return False


def __file_copier(source, destination):
    """File copier

    :param source: str
        Copy from

    :param destination: str
        Copy to

    :return: Bool
    """
    if not exists(destination):
        copy(source, destination)

        return True

    else:
        return False


@cli.command()
@click.option('--name', prompt='Enter module name ',  help='Pass your module name here. For example : posts')
def module(name):
    """Automatically create module

    :param name: str
        module name

    :return: None
    """
    try:
        singular_name = p.plural_verb(name)
        plural_name =  p.plural(singular_name)

        module_dir = 'modules/'+ plural_name
        controller_dir = module_dir+'/controllers'
        model_dir = module_dir+'/models'
        route_dir = module_dir + '/routes'

        if not exists(module_dir):
            __directory_creator(module_dir)
            # create __init__.py
            with open(module_dir + '/__init__.py', 'a+') as file:
                file.write('# coding=utf-8\n')
                file.write('from .routes import {0}_route\n'.format(name))

            __create_controller(plural_name, controller_dir)
            __create_model(singular_name, model_dir)
            __create_route(plural_name, route_dir)

            # update __init__.py
            with open('modules/__init__.py', 'a+') as file:
                file.write('\n# register post routers\n')
                file.write('from .{0} import {0}_route\n'.format(plural_name))
                file.write('app.register_blueprint({0}_route)\n'.format(plural_name))

            click.echo('{0} module created'.format(plural_name))

        else:
            click.echo('{0} module already exist'.format(plural_name))

    except Exception as ex:
        pprint(ex)
        exit(0)


def __create_controller(module_name, controller_dir):
    """Creating controllers

    :param module_name: str
        module directory name

    :param controller_dir: str
        controller directory name

    :return: None
    """
    __directory_creator(controller_dir)
    __file_copier(templates_dir + '/controller.txt', controller_dir +'/'+module_name+'.py')

    with open(templates_dir + '/controller_init.txt') as file:
        file_contents = file.readlines()

    init_content = []
    for content in file_contents:
        init_content.append(content.replace('controller_name', module_name))

    with open(controller_dir + '/__init__.py', 'w') as file:
        file.writelines(init_content)


def __create_model(module_name, model_dir):
    """Create models

    :param module_name: str
        module dir name

    :param model_dir: str
        model dir name

    :return: None
    """
    __directory_creator(model_dir)
    __file_copier(templates_dir + '/__init__.txt', model_dir + '/__init__.py')
    # __file_copier(templates_dir + '/model.txt', model_dir +'/'+ module_name+'.py')
    with open(templates_dir + '/model.txt') as file:
        file_contents = file.readlines()

    model_file_content = []
    for content in file_contents:
        content = content.replace('model_name', module_name.capitalize())
        model_file_content.append(content.replace('table_name', module_name))

    with open(model_dir +'/'+ module_name+'.py', 'w') as file:
        file.writelines(model_file_content)


    with open(templates_dir + '/model_init.txt') as file:
        model_contents = file.readlines()

    model_init_content = []
    for content in model_contents:
        content = content.replace('model_name', module_name)
        model_init_content.append(content.replace('model_class', module_name.capitalize()))

    with open(model_dir + '/__init__.py', 'w') as init_file:
        init_file.writelines(model_init_content)


def __create_route(module_name, route_dir):
    """Create routes

    :param module_name: str
        module dir name

    :param route_dir: str
        route dir name

    :return: None
    """
    __directory_creator(route_dir)
    # __file_copier(templates_dir + '/route.txt', route_dir + '/__init__.py')
    with open(templates_dir + '/route.txt') as file:
        file_contents = file.readlines()

    init_content = []
    for content in file_contents:
        content = content.replace('router_endpoint', module_name)
        init_content.append(content.replace('router_name', module_name+'_route'))

    with open(route_dir + '/__init__.py', 'w') as file:
        file.writelines(init_content)
