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

data['task-definition']['containerDefinitions'][0]['environment'] = data2['prod']['environment']
data['task-definition']['containerDefinitions'][0]['secrets'] = data2['prod']['secrets']

with open(dir_path + "/" + args.output, "w", encoding = "utf-8") as yaml_file:
    dump = ruamel.yaml.dump(data, Dumper=ruamel.yaml.RoundTripDumper)
    yaml_file.write(dump)
