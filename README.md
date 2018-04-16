# Flaskipy

Flaskipy CLI will help you to create a RESTFul backend.

> It's Under Development

## Table of Contents

* [Background](#background)
* [Install](#install)
* [Usage](#usage)
* [Project Run](#how-to-run-this-project)
* [Command Help](#display-the-command-options-with-the-h-option)
* [Project Structure](#project-structure)
* [Endpoints](#endpoints)
* [Features Released](#features-released)
* [Upcoming Features](#upcoming-features)
* [Maintainers](#maintainers)
* [Contributes](#contributes)
* [How to become a contributor](#how-to-become-a-contributor)
* [License](#license)

## Background

## Install

```shell
$[sudo] pip install flaskipy
```

OR, git clone

```shell
$ git clone https://github.com/osmangoninahid/flaskipy

$ cd flaskipy
$ python setup.py install
```

## Before running this project (after cloned from _github_)

* change the name of `config.ini.example` to `config.in`
* inside `config.in` replace the value of the variables with your values
* run `pip install -r requirements.txt` to make sure dependencies are installed

## Usage

```shell
// Initialize project
$ cd [project_name]

// Project structue initialize
$ flaskipy init

// Add new module
$ flaskipy module --name YourModuleName
```

## How to Run this project

```shell
// Development
$ cd [project_name]
$ python main.py
```

It should make a question, like

* Name of the project (It will create a folder in your current working directory and the folder name will be your project name)

### Display the command options with the -h option:

```ssh
$ flaskipy -help

Usage: flaskipy [OPTIONS] COMMAND [ARGS]...

Options:
--help  Show this message and exit.

Commands:
init    Project structure initializer :return: None
module  Automatically create module :param name: str...
```

## Project Structure

```bash
├── config.ini
├── config.ini.example
├── config.py
├── example
│   ├── config.ini
│   ├── config.py
│   ├── main.py
│   ├── modules
│   │   ├── blogs
│   │   │   ├── controllers
│   │   │   │   ├── blogs.py
│   │   │   │   ├── __init__.py
│   │   │   ├── __init__.py
│   │   │   ├── models
│   │   │   │   └── __init__.py
│   │   │   └── routes
│   │   │       ├── __init__.py
│   │   ├── __init__.py
│   ├── README.md
│   ├── tests
│   │   └── __init__.py
│   └── utils
│       └── __init__.py
├── flaskipy
│   ├── commands.py
│   ├── flaskipy_templates
│   │   ├── config_ini.txt
│   │   ├── config.txt
│   │   ├── controller_init.txt
│   │   ├── controller.txt
│   │   ├── __init__.txt
│   │   ├── main.txt
│   │   ├── modules_init.txt
│   │   ├── README.txt
│   │   └── route.txt
│   ├── __init__.py
├── main.py
├── README.md
├── requirements.txt
├── setup.cfg
├── setup.py
└── tests
```

## Endpoints

| Request                   | Response                                             |
| ------------------------- | ---------------------------------------------------- |
| GET base-url/examples     | This will return all example with pagination support |
| POST base-url/examples    | This will create a new example                       |
| GET base-url/example/{id} | This will return a example                           |
| PUT base-url/example/{id} | This is for updating a example                       |
| DELETE base-url/example   | This will delete the example with identification     |

### Features Released

* [x] RestAPI Boilerplate
* [x] Flaskipy CLI

### Upcoming Features

* [ ] JWT integration for authentication and authorization
* [ ] DeployNow integration
* [ ] ApiDoc generation
* [ ] Automated deploy with guinicorn and Python-Fabric
* [ ] Dockerize
* [ ] and Based on feedback

## Maintainers

* **[Osman Goni Nahid](https://github.com/osmangoninahid)**
* **[Porimol Chandro](https://github.com/porimol)**

## Contributes

See the list of [contributors](https://github.com/osmangoninahid/flaskipy/contributors) who participated in this project.

### How to become a contributor

If you want to contribute to `Flaskipy` and make it better, your help is very welcome.
You can make constructive, helpful bug reports, feature requests and the noblest of all contributions.
If like to contribute in a good way, then follow the following guidelines.

#### How to make a clean pull request

* Create a personal fork on Github.
* Clone the fork on your local machine.(Your remote repo on Github is called `origin`.)
* Add the original repository as a remote called `upstream`.
* If you created your fork a while ago be sure to pull upstream changes into your local repository.
* Create a new branch to work on! Branch from `dev`.
* Implement/fix your feature, comment your code.
* Follow `Flaskipy`'s code style, including indentation(4 spaces).
* Write or adapt tests as needed.
* Add or change the documentation as needed.
* Push your branch to your fork on Github, the remote `origin`.
* From your fork open a pull request to the `dev` branch.
* Once the pull request is approved and merged, please pull the changes from `upstream` to your local repo and delete your extra branch(es).

## License

### The MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
