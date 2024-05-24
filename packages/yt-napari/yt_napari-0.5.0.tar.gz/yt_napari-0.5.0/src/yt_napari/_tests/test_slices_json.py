import pytest

from yt_napari._data_model import InputModel
from yt_napari._model_ingestor import _choose_ref_layer, _process_validated_model
from yt_napari._schema_version import schema_name

jdicts = []
jdicts.append(
    {
        "$schema": schema_name,
        "datasets": [
            {
                "filename": "_ytnapari_load_grid",
                "selections": {
                    "slices": [
                        {
                            "fields": [{"field_name": "density", "field_type": "gas"}],
                            "resolution": [400, 400],
                            "normal": "x",
                            "slice_width": {"value": 0.25, "unit": "code_length"},
                            "slice_height": {"value": 0.25, "unit": "code_length"},
                            "center": {"value": [0.5, 0.5, 0.5], "unit": "code_length"},
                        }
                    ]
                },
            }
        ],
    }
)
jdicts.append(
    {
        "$schema": schema_name,
        "datasets": [
            {
                "filename": "_ytnapari_load_grid",
                "selections": {
                    "slices": [
                        {
                            "fields": [{"field_name": "density", "field_type": "gas"}],
                            "normal": "x",
                        }
                    ]
                },
            }
        ],
    }
)


@pytest.mark.parametrize("jdict", jdicts)
def test_basic_slice_validation(jdict):
    _ = InputModel.model_validate(jdict)


@pytest.mark.parametrize("jdict", jdicts)
def test_slice_load(yt_ugrid_ds_fn, jdict):
    im = InputModel.model_validate(jdict)
    layer_lists, _ = _process_validated_model(im)
    ref_layer = _choose_ref_layer(layer_lists)
    _ = ref_layer.align_sanitize_layers(layer_lists)

    jdict["datasets"][0]["selections"]["slices"][0]["rescale"] = True
    im = InputModel.model_validate(jdict)
    layer_lists, _ = _process_validated_model(im)
    im_data = layer_lists[0][0]
    assert im_data.min() == 0
    assert im_data.max() == 1
