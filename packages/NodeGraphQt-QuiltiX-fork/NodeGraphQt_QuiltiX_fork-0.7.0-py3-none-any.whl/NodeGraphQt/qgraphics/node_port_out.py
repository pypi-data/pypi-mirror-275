#!/usr/bin/python
from qtpy import QtCore, QtGui, QtWidgets

from NodeGraphQt.constants import NodeEnum
from NodeGraphQt.qgraphics.node_base import NodeItem


class PortOutputNodeItem(NodeItem):
    """
    Output Port Node item.

    Args:
        name (str): name displayed on the node.
        parent (QtWidgets.QGraphicsItem): parent item.
    """

    def __init__(self, name='group port', parent=None):
        super(PortOutputNodeItem, self).__init__(name, parent)
        self._text_item.set_locked(True)
        self._icon_item.setVisible(False)

    def _paint_horizontal(self, painter, option, widget):
        painter.save()
        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(QtCore.Qt.NoBrush)

        # base background.
        margin = 0
        rect = self.boundingRect()
        rect = QtCore.QRectF(rect.left() + margin,
                             rect.top() + margin,
                             rect.width() - (margin * 2),
                             rect.height() - (margin * 2))

        radius = 4.0
        painter.setBrush(QtGui.QColor(self.backgroundColor))
        painter.drawRoundedRect(rect, radius, radius)

        # light overlay on background when selected.
        if self.selected:
            painter.setBrush(QtGui.QColor(*NodeEnum.SELECTED_COLOR.value))
            painter.drawRoundedRect(rect, radius, radius)

        # node name background.
        padding = 0, 0
        text_rect = self._text_item.boundingRect()
        text_rect = QtCore.QRectF(text_rect.x() + padding[0],
                                  rect.y() + padding[1],
                                  rect.width() - padding[0] - margin,
                                  text_rect.height() - (padding[1] * 2))

        text_rect2 = QtCore.QRectF(text_rect.x() + padding[0],
                                  rect.y() + 3 + padding[1],
                                  rect.width() - padding[0] - margin,
                                  text_rect.height() - (padding[1] * 2))
        # if self.selected:
        #     painter.setBrush(QtGui.QColor(*NodeEnum.SELECTED_COLOR.value))
        # else:
        #     painter.setBrush(QtGui.QColor(0, 0, 0, 80))
        # painter.setBrush(QtGui.QColor(self.titleBackground))
        # painter.drawRoundedRect(text_rect, 3.0, 3.0)
        # painter.drawRect(text_rect2)

        # node border
        if self.selected:
            border_width = 1.2
            border_color = QtGui.QColor(
                *NodeEnum.SELECTED_BORDER_COLOR.value
            )
        else:
            border_width = 0.8
            border_color = QtGui.QColor(*self.border_color)

        border_rect = QtCore.QRectF(rect.left(), rect.top(),
                                    rect.width(), rect.height())

        pen = QtGui.QPen(border_color, border_width)
        pen.setCosmetic(self.viewer().get_zoom() < 0.0)
        path = QtGui.QPainterPath()
        path.addRoundedRect(border_rect, radius, radius)
        painter.setBrush(QtCore.Qt.NoBrush)
        painter.setPen(pen)
        painter.drawPath(path)

        painter.restore()

    def set_proxy_mode(self, mode):
        super(PortOutputNodeItem, self).set_proxy_mode(mode)
        self._icon_item.setVisible(False)
