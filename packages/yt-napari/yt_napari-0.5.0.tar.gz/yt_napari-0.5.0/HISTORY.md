## v0.5.0

### New Features
* covering grid support ([#120](https://github.com/data-exp-lab/yt-napari/pull/120))

### Maintenance
* replace np.random.random with new Generator api ([#130](https://github.com/data-exp-lab/yt-napari/pull/130))


## v0.4.0
This release upgrades required dependencies:
* napari >= 0.4.19
* pydantic>2.0

## v0.3.0

This release introduces an initial metadata explorer widget and improvements to the
Reader widgets.

### New Features
* Saving Reader widget selections to yt-napari JSON ([#108](https://github.com/data-exp-lab/yt-napari/pull/108), @TomasPetro)
* Metadata explorer widget: check fields available in a dataset

## v0.2.1

Bugfix release.

### Fixes
* fix slice scaling for width!=height

## v0.2.0

This release includes some non-backwards compatible changes to the schema. Old
json files will need to be updated to use with yt-napari >= v0.2.0

### New Features
* timeseries loading: a new widget, yt-napari timeseries slicer, is available from the napari gui and json files can also specify timeseries selections. Additionally, there is a new `yt_napari.timeseries` module for jupyter notebook interaction.

### Breaking changes

Breaking schema updates:
* the top level `data` attribute has been renamed `datasets` to distinguish between loading selections from a single timestep and the new `timeseries` selection

## v0.1.0

This release includes some non-backwards compatible changes to the schema. Old
json files will need to be updated. The main change is that with the addition of
adding 2D slices, the region selection from v0.0.1 has been nested within a
`SelectionObject` level.

### New Features

* can now load 2D slices
* widget reader redesign: add multiple selections!
* yt dataset cacheing to speed up subsequent loads
* improved logging
* test infrastructure updates
* improved development maintenance scripts
