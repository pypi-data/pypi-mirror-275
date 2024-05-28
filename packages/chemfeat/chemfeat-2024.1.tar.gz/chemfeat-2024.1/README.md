---
title: README
author: Jan-Michael Rye
---

![ChemFeat logo](https://gitlab.inria.fr/jrye/chemfeat/-/raw/main/img/chemfeat_logo.svg)

# Synopsis

Generate molecular feature vectors for machine- and deep-learning models using cheminformatics software packages.

The package uses an extensible system of subclasses to calculate feature sets. Currently [80 different feature sets](https://jrye.gitlabpages.inria.fr/chemfeat/gen_features.html) are provided using the following software packages:

* [RDKit](https://pypi.org/project/rdkit/)
* [PaDEL-pywrapper](https://pypi.org/project/PaDEL-pywrapper/)

New feature sets can be added by simply subclassing [the FeatureCalculator class](https://gitlab.inria.fr/jrye/chemfeat/-/blob/main/src/chemfeat/features/calculator.py) and registering the new subclass. The [QED calculator](https://gitlab.inria.fr/jrye/chemfeat/-/blob/main/src/chemfeat/features/calculators/qed.py) illustrates how simple this can be.

Features sets can be selected and configured via a [simple list in a YAML configuration file](https://jrye.gitlabpages.inria.fr/chemfeat/gen_feature_set_configuration.html), with several feature sets supporting custom parameters. The list format allows the same feature set to be included multiple times using different parameters, with each parameterized feature set receiving a distinct name in the resulting feature vector.

Features sets are calculated in parallel and cached in an [SQLite](https://www.sqlite.org/index.html) database to avoid the overhead of redundant calculations when feature sets are re-used.



## Links

[insert: links]: #

## GitLab

* [Homepage](https://gitlab.inria.fr/jrye/chemfeat)
* [Source](https://gitlab.inria.fr/jrye/chemfeat.git)
* [Documentation](https://jrye.gitlabpages.inria.fr/chemfeat)
* [Issues](https://gitlab.inria.fr/jrye/chemfeat/-/issues)
* [GitLab package registry](https://gitlab.inria.fr/jrye/chemfeat/-/packages)

## Other Repositories

* [Python Package Index](https://pypi.org/project/chemfeat/)
* [Software Heritage](https://archive.softwareheritage.org/browse/origin/?origin_url=https%3A//gitlab.inria.fr/jrye/chemfeat.git)
* [HAL open science](https://hal.science/hal-04248197)

[/insert: links]: #

### Projects Using ChemFeat

* [MolPred](https://gitlab.inria.fr/jrye/molpred) - A [Hydronaut](https://gitlab.inria.fr/jrye/hydronaut)-based framework for building machine- and deep-learning models to predict properties of molecules.



# Installation

The package can be installed from the [Python Package Index](https://pypi.org/project/chemfeat/) with any compatible Python package manager, e.g.

~~~
pip install chemfeat
~~~

To install from source, clone the Git repository and install the package directly:

~~~
git clone https://gitlab.inria.fr/jrye/chemfeat.git
pip install ./chemfeat
~~~


# Usage

## Command-Line

The package provides the `chemfeat` command-line tool to generated CSV files of feature vectors from lists of InChI strings. It can also be used to generate a template feature-set configuration file and a markdown document describing all of the feature sets. The command's various help messages can be found [here](https://jrye.gitlabpages.inria.fr/chemfeat/gen_command_help.html).

### Usage Example

Given a feature set configuration file ("feature_sets.yaml") and a CSV file with a column of InChI strings ("inchis.csv"), a CSV file out features ("features.csv") can be generated with the following command:

~~~sh
chemfeat calc feature_sets.yaml inchis.csv features.csv
~~~

The following sections contain example contents for the input files and the output file that they produce.

#### feature_sets.yaml

Example feature set configuration file. Note that the feature sets are specified as a list, which allows the same feature set to be use multiple times with different parameters. For the full list of features, see the [feature descriptions](https://jrye.gitlabpages.inria.fr/chemfeat/gen_features.html) and the [configuration file template](https://jrye.gitlabpages.inria.fr/chemfeat/gen_feature_set_configuration.html).

~~~yaml
# QED feature calculator.
- name: qed

# RDK descriptor feature calculator.
- name: rdkdesc
~~~

#### inchis.csv

Example CSV input file with a column containing InChI values. The name of the InChI column is configurable and defaults to "InChI".

~~~
InChI,name
"InChI=1S/C8H9NO2/c1-6(10)9-7-2-4-8(11)5-3-7/h2-5,11H,1H3,(H,9,10)","paracetamol"
"InChI=1S/C13H18O2/c1-9(2)8-11-4-6-12(7-5-11)10(3)13(14)15/h4-7,9-10H,8H2,1-3H3,(H,14,15)","ibuprofen"
~~~

#### featurs.csv

The CSV feature file that results from the example input files above.

~~~
InChI,qed__ALERTS,qed__ALOGP,qed__AROM,qed__HBA,qed__HBD,qed__MW,qed__PSA,qed__ROTB,rdkdesc__FpDensityMorgan1,rdkdesc__FpDensityMorgan2,rdkdesc__FpDensityMorgan3,rdkdesc__MaxAbsPartialCharge,rdkdesc__MaxPartialCharge,rdkdesc__MinAbsPartialCharge,rdkdesc__MinPartialCharge,rdkdesc__NumRadicalElectrons,rdkdesc__NumValenceElectrons
"InChI=1S/C8H9NO2/c1-6(10)9-7-2-4-8(11)5-3-7/h2-5,11H,1H3,(H,9,10)",2,2.0000999999999998,1,2,2,151.16500000000002,52.82000000000001,1,1.2727272727272727,1.8181818181818181,2.272727272727273,0.5079642937129114,0.18214293782620056,0.18214293782620056,-0.5079642937129114,0,58
"InChI=1S/C13H18O2/c1-9(2)8-11-4-6-12(7-5-11)10(3)13(14)15/h4-7,9-10H,8H2,1-3H3,(H,14,15)",0,3.073200000000001,1,2,1,206.28499999999997,37.3,4,1.2,1.7333333333333334,2.1333333333333333,0.4807885019257389,0.3101853515323108,0.3101853515323108,-0.4807885019257389,0,82
~~~


## Python API

~~~python
from chemfeat.database import FeatureDatabase
from chemfeat.features.manager import FeatureManager

# Here we assume that the following variables have already been defined:
# 
# feat_specs:
#   A list of feature specifications as returned by loading a YAML feature-set
#   configuration file.
#
# inchis:
#   An iterable of InChI strings representing the molecules for which the
#   features should be calculated.


# Create the database object.
feat_db = FeatureDatabase('features.sqlite')

# Create the feature manager object.
feat_man = FeatureManager(feat_db, feat_specs)

# Calculate the features and retrieve them as a Pandas dataframe.
feat_dataframe = feat_man.calculate_features(inchis, return_dataframe=True)
~~~

## Adding Feature Sets

The [QED calculator](https://gitlab.inria.fr/jrye/chemfeat/-/blob/main/src/chemfeat/features/calculators/qed.py) provides a minimal example of how to add a custom feature set. The following are required:

* A class docstring in [Markdown format](https://en.wikipedia.org/wiki/Markdown) that provides a brief description of the feature set, links to more information about the feature, a reference article or other scientific citation if available, and a list of the features calculated. The docstring will be used to automatically generated the documentation of available feature sets.
* A `FEATURE_SET_NAME` class attribute. This is the name that will be used to select the feature set in the configuration file and also the basis of the prefix that will be appended to the features that the feature set calculates.
* A method named `is_numeric` that accepts the name of a feature belonging to the feature set and returns `True` if the feature is numeric else `False` if it is categoric.
* A method named `add_features` that accepts a features `dict` and an RDKit molecule object. The method must update the `dict` with the calculated features. The names of the features should be prefixed with the configured feature set's identifier. This can be done using the `add_prefix` method.

Once the subclass has been defined, it must be registered using the base class's `register` method, which should normally be invoked just after the class definition to ensure that it is registered when the containing module is imported.

### Importing Feature Calculators

In the simplest case, the modules containing feature calculators can be explicitly imported in the user's code. `chemfeat.features.manager` also provides the [import_calculators](https://jrye.gitlabpages.inria.fr/chemfeat/chemfeat.features.html#chemfeat.features.manager.import_calculators) function to facilitate imports. It can be used to glob imports from a dedicated feature calculator subclass directory or dynamically configure imports based on custom criteria such as the availability of dependencies.
