import os
import pandas as pd
import biom
import tempfile
import q2templates
from shutil import which     

def plot(
        output_dir: str,
        collapsed_table: biom.Table,
        delimiter: str = ";") -> None:

    all_dict = {}
    taxa = []
    for values, id, metadata in collapsed_table.transpose().iter():
        taxa.append(id)
    for values, id, metadata in collapsed_table.iter():
        sample_dict = {}
        for i, v in enumerate(values):
            sample_dict[taxa[i]] = v
        all_dict[id] = sample_dict

    tempdir = tempfile.mkdtemp()
    sample_filepaths = []
    for sample in all_dict.keys():
        sample_filepath = os.path.join(tempdir, sample + ".txt")
        sample_filepaths.append(sample_filepath)
        sample_file = open(sample_filepath, "w")
        for taxa in all_dict[sample].keys():
            val = all_dict[sample][taxa]
            taxa = taxa.replace(delimiter, "\t")
            sample_file.write(str(val) + "\t" + taxa + "\n")
        sample_file.close()
    
    if which("ktImportText") is None:
        raise FileNotFoundError("'ktImportText' is not found, but can be installed with:\n\nconda install -c bioconda krona")      

    krona_filepath = os.path.join(tempdir, "index.html")
    krona_command = " ".join(["ktImportText", " ".join(sample_filepaths), "-o", krona_filepath])
    os.system(krona_command)

    q2templates.render(sample_filepaths+[krona_filepath], output_dir)

def collapse_and_plot(ctx, table, taxonomy, level=7, delimiter=";"):
    collapse = ctx.get_action('taxa', 'collapse')
    collapsed_table, = collapse(table=table, taxonomy=taxonomy, level=level)

    plot = ctx.get_action('krona', 'plot')
    krona_plot, = plot(collapsed_table = collapsed_table, delimiter = delimiter)

    return krona_plot
