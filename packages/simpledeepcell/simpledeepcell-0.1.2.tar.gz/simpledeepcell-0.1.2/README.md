# simpledeepcell
This is a mini-package of code directly copied from deepcell-tf (https://github.com/vanvalenlab/deepcell-tf), version 0.12.4 / deepcell-toolbox (https://github.com/vanvalenlab/deepcell-toolbox), version 0.12.0, but only retaining the portions of code needed to run Mesmer as implemented by the steinbock package (https://github.com/BodenmillerGroup/steinbock/tree/main/steinbock).

Advantages: deepcell-toolbox requires VS buildtools to be successully installed by pip, which involves extra work outside of python/conda & involves a multi-gigabyte download (VS buildtools is BIG!). Additionally, using this package should cut down on the overall download size in other ways, as this package is much smaller that the full-size deepcell packages & does not require or download as many dependencies.
So using this package may be good if you are only trying to use Mesmer, such as when using the Steinbock package or related code, however -- note that using this package with steinbock would require further editing of Steinbock to load this package instead of deepcell.

## import:

    pip install simpledeepcell

To access the Mesmer segmentation, run:

    from simpledeepcell.main import Mesmer

## License:

This package has the same license as the deepcell: a modified, non-commercial / academic-focused Apache license
