import Constant as c
from ConnectSignal.Lambda import (
    # connect_plain_text_edit_abstract,
    # connect_text_edit_pushbutton_apply_abstract,
    connect_combobox_abstract,
    # connect_checkbox_abstract,
    connect_slider_moved_abstract,
    connect_slider_released_abstract,
    connect_dash_lineedit_abstract,
    # connect_lineedit_abstract
)

from ConnectSignal.ConnectMacros import (
    connect_o_arrow,
    connect_d_arrow,
    connect_colour)

def connect_segment(scene):
    scene.ui.segment_line_width_slider.sliderMoved.connect(
        lambda x: connect_slider_moved_abstract(x, scene, ['line'], 'line_width', lambda x: x/10.0, scene.ui.segment_line_width_spin))
    scene.ui.segment_line_width_slider.sliderReleased.connect(
        lambda : connect_slider_released_abstract(scene))

    scene.ui.segment_custom_dash.editingFinished.connect(
        lambda : connect_dash_lineedit_abstract(scene, ['line', 'dash'], 'custom_pattern', scene.ui.segment_custom_dash))

    scene.ui.segment_line_stroke.currentIndexChanged.connect(
        lambda x: connect_combobox_abstract(x, scene, ['line', 'dash'], 'stroke', c.attribute_values(c.Line_Stroke)))

    scene.ui.segment_double_distance_slider.sliderMoved.connect(
        lambda x: connect_slider_moved_abstract(x, scene, ['line', 'double'], 'distance', lambda x: x/10.0, scene.ui.segment_double_distance_spin))
    scene.ui.segment_double_distance_slider.sliderReleased.connect(
        lambda : connect_slider_released_abstract(scene))

    connect_o_arrow(scene,
        scene.ui.segment_o_tip,
        scene.ui.segment_o_side,
        scene.ui.segment_o_reversed,
        scene.ui.segment_o_length_spin,
        scene.ui.segment_o_length_slider,
        scene.ui.segment_o_width_spin,
        scene.ui.segment_o_width_slider)

    connect_d_arrow(scene,
        scene.ui.segment_d_tip,
        scene.ui.segment_d_side,
        scene.ui.segment_d_reversed,
        scene.ui.segment_d_length_spin,
        scene.ui.segment_d_length_slider,
        scene.ui.segment_d_width_spin,
        scene.ui.segment_d_width_slider)

    connect_colour(scene, ['line', 'colour'],
        scene.ui.segment_colour_name,
        scene.ui.segment_colour_mix_name,
        scene.ui.segment_colour_mixratio_spin,
        scene.ui.segment_colour_mixratio_slider,
        scene.ui.segment_colour_strength_spin,
        scene.ui.segment_colour_strength_slider)