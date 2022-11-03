#!bin/bash

echo ${task_definition_template}
if [[ -z ${task_definition_template} ]]; then
    echo "no"
else
    echo "yes"
if