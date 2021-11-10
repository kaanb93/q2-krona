# ----------------------------------------------------------------------------
# Copyright (c) 2016-2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import qiime2.plugin
from qiime2.plugin import Visualization

import q2_krona
from q2_krona._functions import plot
from q2_krona._functions import collapse_and_plot

from q2_types.feature_data import FeatureData, Taxonomy
from q2_types.feature_table import FeatureTable, Frequency


plugin = qiime2.plugin.Plugin(
    name='krona',
    description='This is a simple tool to generate Krona charts '
                'from feature tables.',
    version='1.0.0',
    website='https://github.com/kaanb93/q2-krona',
    package='q2_krona',
    user_support_text=None,
    citation_text='',
    short_description='Plugin for creating Krona charts.',
)

plugin.visualizers.register_function(
    function=plot,
    inputs={'collapsed_table': FeatureTable[Frequency]},
    parameters={'delimiter': qiime2.plugin.Str},
    input_descriptions={
        'collapsed_table': 'Frequencies collapsed to taxonomy.'
    },
    parameter_descriptions={
        'delimiter': 'Delimiter character used in taxonomy file.'
    },
    name='Generate Krona chart visualizer',
    description="Generate Krona chart visualizer",
    citations=None
)

plugin.pipelines.register_function(
    function=collapse_and_plot,
    inputs={
        'table': FeatureTable[Frequency],
        'taxonomy': FeatureData[Taxonomy]
    },
    parameters={
        'level': qiime2.plugin.Int,
        'delimiter': qiime2.plugin.Str
    },
    outputs=[('krona_plot', Visualization)],
    input_descriptions={
        'table': 'Feature table containing the frequencies.',
    },
    parameter_descriptions={
        'level': ('The taxonomic level at which the features should be '
                  'collapsed.'),
        'delimiter': 'Delimiter character used in taxonomy file.'
    },
    output_descriptions={
        'krona_plot': 'Visualizer of Krona plots.'
    },
    name='Collapse features and generate Krona plot',
    description="Generate Krona plot from feature table by collapsing "
                "to specified level."
)
