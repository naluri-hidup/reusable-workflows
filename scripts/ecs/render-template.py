import os
import argparse
from pathlib import Path

from ruamel.yaml import YAML
from jinja2 import Environment, FileSystemLoader


def parse_template(template_file: str, variables):
  local_env = Environment(loader=FileSystemLoader(searchpath=Path(__file__).parent.parent.parent.as_posix()))
  template = local_env.get_template(template_file)

  build_version = os.environ.get('build_version', '')
  env = os.environ.get('env', '')

  return template.render(
    build_version=build_version,
    env=env,
    **variables
  )


def set_github_env(name, value):
  with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
    f.write(f'{name}={value}\n')


def main():
  parser = argparse.ArgumentParser(description='Render YAML task definition template')
  parser.add_argument('-v', '--variables', help='Path to the definition.yml variables file', required=True)
  parser.add_argument('-o', '--output', help='Path to the output file', required=True)
  args = parser.parse_args()

  yaml = YAML(typ='safe')
  yaml.preserve_quotes = True
  yaml.default_style = '='

  # Add 2 extra spaces when indenting lists
  # https://stackoverflow.com/q/25108581/10612
  yaml.indent(sequence=4, offset=2)

  with open(args.variables) as definition:
    definitions = yaml.load(definition)

  # possible values: dev, stag, prod
  env = os.environ.get('env', 'stag')
  variables = definitions[env]
  if not variables:
    raise KeyError('No definition found for env: ' + env)

  template_file = Path("ecs-td-template") / f"{variables['ecs']['task_definition_template']}.yml.j2"

  with open(os.path.join(os.getcwd(), args.output), "w", encoding = "utf-8") as final:
    parsed_template = parse_template(template_file.as_posix(), variables)
    yaml.dump(yaml.load(parsed_template)['task-definition'], final)

  ecs_variables = variables['ecs']
  set_github_env('task_definition_name', ecs_variables.get('task_definition_name', ''))
  set_github_env('cluster_name', ecs_variables.get('cluster_name', ''))
  set_github_env('service_name', ecs_variables.get('service_name', ''))


if __name__ == '__main__':
  main()