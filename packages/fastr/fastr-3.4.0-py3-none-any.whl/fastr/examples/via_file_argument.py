#!/usr/bin/env python

# Copyright 2011-2014 Biomedical Imaging Group Rotterdam, Departments of
# Medical Informatics and Radiology, Erasmus MC, Rotterdam, The Netherlands
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import fastr

IS_TEST = True


def create_network():
    network = fastr.create_network(id="via_file_argument")

    source1 = network.create_source('Int', id='numbers')

    sum_node = network.create_node('fastr/math/SumViaFile:1.0', tool_version='1.0', id='sum')
    link = source1.output >> sum_node.inputs['values']
    link.collapse = 'numbers'

    sink = network.create_sink('Int', id='sink')
    sink.input = sum_node.outputs['result']

    return network


def source_data(network):
    return {'numbers': list(range(10))}


def sink_data(network):
    return {'sink': 'vfs://tmp/results/{}/result_{{sample_id}}_{{cardinality}}{{ext}}'.format(network.id)}


def main():
    print(""" WARNING: experimental feature ;) """)
    print(""" Please run "pip install sklearn" to make use of the experimental cross validation flow. """)
    network = create_network()

    network.draw(draw_dimensions=True)

    network.execute(source_data(network), sink_data(network))


if __name__ == '__main__':
    main()
