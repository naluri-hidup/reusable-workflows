import os
import argparse
import ruamel.yaml

arg_parser = argparse.ArgumentParser(description='Insert env and secrets into yaml')
arg_parser.add_argument('-e', '--environment')
arg_parser.add_argument('-s', '--source')
arg_parser.add_argument('-d', '--destination')
arg_parser.add_argument('-o', '--output')

args = arg_parser.parse_args()
yaml = ruamel.yaml.YAML()
dir_path = os.getcwd()

with open(dir_path + "/" + args.destination) as ad:
    data = yaml.load(ad)

with open(dir_path + "/" + args.source) as ad:
    data2 = yaml.load(ad)

if 'environment' in data2[args.environment]:
    data['containerDefinitions'][0]['environment'] = data2[args.environment]['environment']

if 'secrets' in data2[args.environment]:
    data['containerDefinitions'][0]['secrets'] = data2[args.environment]['secrets']

if 'portMappings' in data2[args.environment]:
    data['containerDefinitions'][0]['portMappings'] = data2[args.environment]['portMappings']

if 'linuxParameters' in data2[args.environment]:
    data['containerDefinitions'][0]['linuxParameters'] = data2[args.environment]['linuxParameters']

if 'command' in data2[args.environment]:
    data['containerDefinitions'][0]['command'] = data2[args.environment]['command']

if 'volumes' in data2[args.environment]:
    data['volumes'] = data2[args.environment]['volumes']

if 'mountPoints' in data2[args.environment]:
    data['containerDefinitions'][0]['mountPoints'] = data2[args.environment]['mountPoints']

with open(dir_path + "/" + args.output, "w", encoding = "utf-8") as yaml_file:
    dump = ruamel.yaml.dump(data, Dumper=ruamel.yaml.RoundTripDumper)
    yaml_file.write(dump)
