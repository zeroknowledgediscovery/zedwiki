# Issues encountered

Using pip versions of `qbiome`/`quasinet`, 

- `example1.ipynb`
    * `label_matrix` populates with `nan` strings
    * training sometimes fails with `ValueError: zero-size array to reduction operation maximum which has no identity`

- `example2.ipynb`
    * same issue with `label_matrix` and `nan` strings
    * frequently getting 622 features instead of 621 (cf. the [known bug](https://github.com/zeroknowledgediscovery/qbiome/tree/main/examples#bugs))
        - `sns.lineplot` fails for `'Actinobacteriota', 'Bacteroidota'` biomes