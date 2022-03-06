import Constant as c
from Colour import Colour
from Fill.FillMacros import (
    fill_colour,
    fill_fill_pattern,
    fill_decoration
)

def fill_polygon_fields(scene):
    colours = c.attribute_values(c.Colour)\
        + [i.get_id() for i in scene.project_data.items.values() if isinstance(i, Colour)]
    ids = scene.list_focus_ids
    if not ids:
        return
    if c.TYPES[scene.current_tab_idx] != 'polygon':
        return
    polygon = scene.project_data.items[ids[0]].item

    scene.ui.polygon_def_str.setText(scene.project_data.items[ids[0]].definition_string())

    scene.skip_combobox_changes = True
    scene.ui.polygon_line_stroke.setCurrentIndex(c.attribute_values(c.Line_Stroke).index(polygon["line"]["dash"]["stroke"]))
    scene.skip_combobox_changes = False

    scene.ui.polygon_line_width_slider.setValue(10.0 * polygon["line"]["line_width"])
    scene.ui.polygon_line_width_spin.setValue(polygon["line"]["line_width"])
    scene.ui.polygon_custom_dash.setText(' '.join(map(str, polygon["line"]["dash"]["custom_pattern"])))

    fill_colour(scene, polygon["fill"]["colour"], colours,
        scene.ui.polygon_marker_colour_name,
        scene.ui.polygon_marker_colour_mix_name,
        scene.ui.polygon_marker_colour_mixratio_spin,
        scene.ui.polygon_marker_colour_mixratio_slider,
        scene.ui.polygon_marker_colour_strength_spin,
        scene.ui.polygon_marker_colour_strength_slider)


    fill_fill_pattern(scene, polygon["fill"]["pattern"],
        scene.ui.polygon_pattern_type,
        scene.ui.polygon_pattern_distance_spin,
        scene.ui.polygon_pattern_distance_slider,
        scene.ui.polygon_pattern_size_spin,
        scene.ui.polygon_pattern_size_slider,
        scene.ui.polygon_pattern_rotation_spin,
        scene.ui.polygon_pattern_rotation_slider,
        scene.ui.polygon_pattern_xshift_spin,
        scene.ui.polygon_pattern_xshift_slider,
        scene.ui.polygon_pattern_yshift_spin,
        scene.ui.polygon_pattern_yshift_slider)

    fill_colour(scene, polygon["line"]["colour"], colours,
        scene.ui.polygon_border_colour_name,
        scene.ui.polygon_border_colour_mix_name,
        scene.ui.polygon_border_colour_mixratio_spin,
        scene.ui.polygon_border_colour_mixratio_slider,
        scene.ui.polygon_border_colour_strength_spin,
        scene.ui.polygon_border_colour_strength_slider)

    fill_decoration(scene, polygon["line"]["decoration"],
        scene.ui.polygon_decoration_type,
        scene.ui.polygon_amplitude_spin, scene.ui.polygon_amplitude_slider,
        scene.ui.polygon_wavelength_spin, scene.ui.polygon_wavelength_slider,
        scene.ui.polygon_decoration_text)
