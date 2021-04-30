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

Use \$\$ \$\$ for block equations or backslash bracket  for inline

# Dark mode

```
pdoc --html hypothesis/ -o docs/ -c latex_math=True -f --template-dir custom_templates/
```

where we first copy the contents of the dfault pdoc/templates to custim_templates, and then use this as the css.mako [css.mako](http://34.66.189.202:4567/uploads/css.mako/3e814aa20e8b7ce8d029eeb632da5f1d549df3a9)


This creates a directory `docs/qbiome`. Host `docs/qbiome/index.html` on GitHub Pages and you have your documentation website.