from envyaml import EnvYAML
import ruamel.yaml
import os 

dir_path = os.getcwd()
# read file env.yaml and parse config
env = EnvYAML(dir_path + '/template/ecs-td-template/template.yml')


with open(dir_path + '/after.yml', "w", encoding = "utf-8") as yaml_file:
    dump = ruamel.yaml.dump(env['task-definition'], Dumper=ruamel.yaml.RoundTripDumper)
    yaml_file.write(dump)

print(env['task-definition'])