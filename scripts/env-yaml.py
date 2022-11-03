from envyaml import EnvYAML
import ruamel.yaml
import os 
import argparse

arg_parser = argparse.ArgumentParser(description='EnvYaml')
arg_parser.add_argument('-t', '--template')

args = arg_parser.parse_args()

dir_path = os.getcwd()
# Use the task definition template
env = EnvYAML(dir_path + '/template/ecs-td-template/' + args.template + '.yml')


with open(dir_path + '/task-definition.yml', "w", encoding = "utf-8") as yaml_file:
    dump = ruamel.yaml.dump(env['task-definition'], Dumper=ruamel.yaml.RoundTripDumper)
    yaml_file.write(dump)

print(env['task-definition'])