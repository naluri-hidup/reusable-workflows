from envyaml import EnvYAML
import ruamel.yaml
import os 
import argparse

arg_parser = argparse.ArgumentParser(description='EnvYaml')
arg_parser.add_argument('-t', '--template')
arg_parser.add_argument('-o', '--output')
args = arg_parser.parse_args()

dir_path = os.getcwd()

# Use the task definition template
env = EnvYAML(dir_path + '/' + args.template)

with open(dir_path + '/' + args.output, "w", encoding = "utf-8") as yaml_file:
    dump = ruamel.yaml.dump(env['task-definition'], Dumper=ruamel.yaml.RoundTripDumper)
    yaml_file.write(dump)

print(env['task-definition'])