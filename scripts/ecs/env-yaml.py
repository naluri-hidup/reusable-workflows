from envyaml import EnvYAML
from ruamel.yaml import YAML
import os 
import argparse

arg_parser = argparse.ArgumentParser(description='EnvYaml')
arg_parser.add_argument('-t', '--template')
arg_parser.add_argument('-o', '--output')
args = arg_parser.parse_args()

dir_path = os.getcwd()

# Use the task definition template
env = EnvYAML(dir_path + '/' + args.template)

yaml = YAML(typ='safe')
yaml.preserve_quotes = True
out = StringIO()

with open(dir_path + '/' + args.output, "w", encoding = "utf-8") as yaml_file:
    dump = yaml.dump(env['task-definition'], stream=out)
    yaml_file.write(dump)

print(env['task-definition'])