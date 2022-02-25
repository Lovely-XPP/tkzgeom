from PyQt5 import QtCore, QtWidgets, QtGui

from Item import Item
from Point import Point
from Tikzifyables.Arrowable import Arrowable
from Tikzifyables.DashPatternable import DashPatternable
from Tikzifyables.Colourable.LineColourable import LineColourable
import Constant as c

class Segment(Item, Arrowable, DashPatternable, LineColourable):
    def __init__(self, item):
        Item.__init__(self, item)
        if item is None:
            self.dictionary_builder(None, "")
        Arrowable.__init__(self, self.item)
        DashPatternable.__init__(self, self.item)
        LineColourable.__init__(self, self.item)

    def tikzify(self):
        options = [
            self.tikzify_arrows(),
            self.tikzify_dash(),
            'draw=' + self.tikzify_line_colour()
        ]
        options = filter(bool, options)
        return "\\draw[%s](%s) -- (%s);" % ( ', '.join(options) , self.item["definition"]["A"], self.item["definition"]["B"])

    def __str__(self):
        return "Segment from (%s) to (%s)" % (self.item["definition"]["A"], self.item["definition"]["B"])

    def draw_on_canvas(self, items, scene, colour=QtCore.Qt.darkMagenta):
        thickness = 4
        graphics_line = QtWidgets.QGraphicsLineItem(
            *items[self.item["definition"]["A"]].get_canvas_coordinates(),
            *items[self.item["definition"]["B"]].get_canvas_coordinates()
        )
        graphics_line.setPen(QtGui.QPen(QtGui.QBrush(colour), thickness))
        scene.addItem(graphics_line)

    @staticmethod
    def draw_on_canvas_static(x1, y1, x2, y2, scene, colour=QtCore.Qt.darkMagenta):
        thickness = 4
        graphics_line = QtWidgets.QGraphicsLineItem(x1, y1, x2, y2)
        graphics_line.setPen(QtGui.QPen(QtGui.QBrush(colour), thickness))
        scene.addItem(graphics_line)

    def distance_sqr(self, x, y, items):
        x1, y1 = items[self.item["definition"]["A"]].get_canvas_coordinates()
        x2, y2 = items[self.item["definition"]["B"]].get_canvas_coordinates()
        x3, y3 = x, y
        px = x2-x1
        py = y2-y1
        norm = px*px + py*py
        if norm == 0.0:
            return 0.0
        u =  ((x3 - x1) * px + (y3 - y1) * py) / float(norm)

        if u > 1:
            u = 1
        elif u < 0:
            u = 0

        x = x1 + u * px
        y = y1 + u * py
        dx = x - x3
        dy = y - y3

        dist = dx*dx + dy*dy
        return dist

    def definition_builder(self, data):
        return { "A": data[0], "B": data[1]}


    @staticmethod
    def static_patterns():
        return ["pp"]

    def patterns(self):
        return ["pp"]

    def next_id_func(self, definition, iter_counter):
        current = definition["A"] + '_' + definition["B"]
        if iter_counter != 0:
            current += '_' + iter_counter * '\''
        return current

    def definition_builder(self, data, items):
        return dict(zip(["A", "B"], data))

    def dictionary_builder(self, definition, id):
        dictionary = {}
        dictionary["id"] = id
        dictionary["type"] = 'segment'
        dictionary["show"] = True
        dictionary["definition"] = definition
        dictionary["label"] = {}
        dictionary["label"]["show"] = c.Segment.Default.Label.SHOW
        dictionary["label"]["text"] = c.Segment.Default.Label.TEXT
        dictionary["label"]["anchor"] = c.Segment.Default.Label.ANCHOR
        dictionary["label"]["offset"] = c.Segment.Default.Label.OFFSET
        dictionary["line"] = {}
        dictionary["line"]["line_width"] = c.Segment.Default.LINE_WIDTH
        dictionary["line"]["colour"] = {}
        dictionary["line"]["colour"]["name"] = c.Segment.Default.Line_Colour.NAME
        dictionary["line"]["colour"]["mix_with"] = c.Segment.Default.Line_Colour.MIX_WITH
        dictionary["line"]["colour"]["mix_percent"] = c.Segment.Default.Line_Colour.MIX_RATIO
        dictionary["line"]["colour"]["strength"] = c.Segment.Default.Line_Colour.STRENGTH
        dictionary["line"]["dash"] = {}
        dictionary["line"]["dash"]["stroke"] = c.Segment.Default.LINE_DASH_STROKE
        dictionary["line"]["dash"]["custom_pattern"] = c.Segment.Default.LINE_DASH_CUSTOM
        dictionary["o_arrow"] = {}
        dictionary["o_arrow"]["width"] = c.Segment.Default.O_Arrow.WIDTH
        dictionary["o_arrow"]["length"] = c.Segment.Default.O_Arrow.LENGTH
        dictionary["o_arrow"]["tip"] = c.Segment.Default.O_Arrow.TIP
        dictionary["d_arrow"] = {}
        dictionary["d_arrow"]["width"] = c.Segment.Default.D_Arrow.WIDTH
        dictionary["d_arrow"]["length"] = c.Segment.Default.D_Arrow.LENGTH
        dictionary["d_arrow"]["tip"] = c.Segment.Default.D_Arrow.TIP
        dictionary["fill"] = {}
        dictionary["fill"]["colour"] = {}
        dictionary["fill"]["colour"]["name"] = c.Point.Default.Fill_Colour.NAME
        dictionary["fill"]["colour"]["mix_with"] = c.Point.Default.Fill_Colour.MIX_WITH
        dictionary["fill"]["colour"]["mix_percent"] = c.Point.Default.Fill_Colour.MIX_RATIO
        dictionary["fill"]["colour"]["strength"] = c.Point.Default.Fill_Colour.STRENGTH

        self.item = dictionary