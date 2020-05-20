#!/usr/bin/env python
import io
import cfnlint
import pypandoc
import datetime
from pytablewriter import MarkdownTableWriter
from pathlib import Path


def get_cfn(file_name):
    print(file_name)
    with open(file_name, encoding="utf8", errors='ignore') as _f:
        _decoded = cfnlint.decode.cfn_yaml.loads(_f.read())
        return _decoded


for yaml_cfn_file in Path('./templates').glob('*.yaml'):
    print(f"Working on {yaml_cfn_file}")
    template = get_cfn(Path(yaml_cfn_file))
    print(template)
    _pf = Path(yaml_cfn_file).stem + ".adoc"
    p_file = f"docs/generated/{_pf}"

    label_mappings = {}
    reverse_label_mappings = {}
    parameter_mappings = {}
    parameter_labels = {}
    no_groups = {}

    def determine_optional_value(param):
        optional = template['Metadata'].get('OptionalParams')
        if optional and (param in optional):
            return '__Optional__'
        return '**__Requires Input__**'

    for label in template['Metadata']['AWS::CloudFormation::Interface']['ParameterGroups']:
        label_name = label['Label']['default']
        label_params = label['Parameters']
        label_mappings[label_name] = label_params
        for ln in label_params:
            reverse_label_mappings[ln] = label_name

    for label_name, label_data in template['Metadata']['AWS::CloudFormation::Interface']['ParameterLabels'].items():
        parameter_labels[label_name] = label_data.get('default')

    for label_name, label_data in template['Parameters'].items():
        parameter_mappings[label_name] = label_data
        if not reverse_label_mappings.get(label_name):
            no_groups[label_name] = label_data

    with open(p_file, 'w') as new_params_file :
        _nl = '\n'
        _now = datetime.datetime.now()
        _ts_now=_now.strftime("%Y-%m-%d %H:%M:%S")
        new_params_file.write(f'IMPORTANT: Last Change to input parameters on: {_ts_now}{_nl}{_nl}')


    for label_name, label_params in label_mappings.items():
        writer = MarkdownTableWriter()
        writer.table_name = label_name
        writer.headers = ["Parameter label (name)", "Default", "Description"]
        writer.value_matrix = []
        writer.stream = io.StringIO()
        for lparam in label_params:
            writer.set_indent_level(4)
            writer.value_matrix.append([
            f"**{str(parameter_labels.get(lparam, 'NO_LABEL'))}**<br>(`{lparam}`)",
            str(parameter_mappings[lparam].get('Default', determine_optional_value(lparam))),
            str(parameter_mappings[lparam].get('Description', 'NO_DESCRIPTION'))
            ])
        writer.write_table()

        with open (p_file, 'a') as p:
            print(f"Generating {p_file}")
            p.write(pypandoc.convert_text(writer.stream.getvalue(), 'asciidoc', format='markdown'))
