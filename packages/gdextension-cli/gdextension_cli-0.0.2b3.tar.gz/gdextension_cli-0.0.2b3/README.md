# gdextension-cli

A command line interface for Godot's GDExtension.

## Requirements

- Python >= 3.8
- Git >= 1.7.x

## Installation

`pip install gdextension-cli`

## Usage

### Create a new project

`gdextension-cli new <NAME>`

This will create a project called <NAME> in a new directory relative to your current path.

By default, https://github.com/3LK3/gdextension-template is used as the project template.

#### From a custom git repository

You can also use your own template repository to create a new project.

`gdextension-cli new <NAME> --from-git https://github.com/<you>/<your-custom-template>`

#### From a local directory

If you have a template on your local file system you can also create a project from there.

`gdextension-cli new <NAME> --from-local /home/you/your_template`