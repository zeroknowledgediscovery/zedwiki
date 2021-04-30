# Pdoc

- https://pdoc.dev/
- https://pdoc3.github.io/pdoc/

# Install using PIP

```
pip3 install pdoc3
```

# Install Visual Studio Code Plugin

https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring

This plugin will automatically generate templates for documentations like this:

```
"""Parse and join the data CSV and the metadata CSV

        Args:
            fpath_data (str): file path for the data CSV
            fpath_meta (str): file path for the metadata CSV
            taxon_name (str, optional): name of the taxon column exactly as in the data CSV.
            Defaults to 'Phylum'.
            time_column_name (str, optional): name of the timestamp column exactly as in the metadata CSV. Defaults to 'Age (days)'.
            time_column_name_out (str, optional): name of the timestamp column in the return data frame. Defaults to 'day'.
            k_years (int, optional): in the return data frame, we keep timestamps up to the number of years specified. Defaults to 2.
            k_biomes (int, optional): in the return data frame, we keep the k most abundant biomes. Defaults to 15.

        Returns:
            pandas.DataFrame: parsed, cleaned data frame
        """
```

# Generate docs from the command line

Say me code lives in a directory called `qbiome`. Run the command below:

```
pdoc --html qbiome/ --output-dir docs --force
```

# Adding mathematical equations

```
pdoc --html dir/ -o docs/ -c latex_math=True -f
```

Use \$\$ \$\$ for block equations or 

> \( \)

 for inline


This creates a directory `docs/qbiome`. Host `docs/qbiome/index.html` on GitHub Pages and you have your documentation website.