#!/usr/bin/python3

import os
import json
import math
from string import Template
from typing import Mapping, Sequence, Union, Any
from PySide6.QtCore import QFile, QPoint, QPointF
from PySide6.QtGui import QColor, QRadialGradient, QLinearGradient


class _QssTemplate(Template):
    delimiter = "--"


class QStyleSheet:
    '''
    :param: qss: 
        - dict: {"background-color": "white"}
        - str : "QWidget { background-color: white; }"
        - str : ":/path/to/resoucre/file.qss",
        - str : "/path/to/local/file.qss"
        - str : "/path/to/local/file.json"

    ## e.g
    Label(
        qss=QStyleSheet(
            qss={
                "background-color": "--themeColor",
                "color": "white",
                "font-size": "24px"
            },
            vars={
                "themeColor": "blue"
            }
        )
    )
    :result:
        QLabel {
            background-color: blue;
            color: white;
            font-size: 24px;
        }

    '''

    class Element:
        def __new__(cls, *args, **kwargs) -> Any:
            instance = super().__new__(cls)
            return instance.__init__(*args, **kwargs)

    class BorderRadius(Element):
        def __init__(self, 
                     top_left: int = 0,
                     top_right: int = 0,
                     bottom_left: int = 0,
                     bottom_right: int = 0) -> str:

            return " ".join(map(lambda x: f"{x}px",
                                (top_left, top_right, bottom_right, bottom_left)))

    class RadialGradient(Element):
        def __init__(self, 
                     stops: Union[Sequence[tuple[float, Union[QColor, str]]], 
                                  dict[float, Union[QColor, str]]],
                     cx: float = None, 
                     cy: float = None,
                     fx: float = None,
                     fy: float = None,
                     radius: float = None,
                     spread: Union[str, QRadialGradient.Spread] = None,
                     coordinate: Union[str, QRadialGradient.CoordinateMode] = None
                     ) -> str:

            if isinstance(spread, QRadialGradient.Spread):
                spread = spread.name.removesuffix("Spread").lower()

            if isinstance(coordinate, QRadialGradient.CoordinateMode):
                coordinate = coordinate.name.removesuffix("Mode")
                coordinate[0] = coordinate[0].lower()

            args = {"cx": cx, "cy": cy, "radius": radius, "fx": fx, "fy": fy, "spread": spread, "coordinateMode": coordinate}
            data = [f"{k}: {v}" for k, v in args.items() if v is not None]
            for value, color in (stops.items() if isinstance(stops, dict) else stops):
                if isinstance(color, QColor):
                    color = f"rgba({','.join(map(str, color.toTuple()))})"
                if value > 1:
                    value = value / 100
                data.append(f"stop: {value} {color}")
            return f"qradialgradient({', '.join(data)})"
    
    class LinearGradient(Element):
        def __init__(self, 
                     stops: Union[Sequence[tuple[float, Union[QColor, str]]], 
                                  dict[float, Union[QColor, str]]],
                     start: Union[QPoint, QPointF] = None, 
                     end: Union[QPoint, QPointF] = None,
                     degree: int = None) -> str:

            data = []
            for value, color in (stops.items() if isinstance(stops, dict) else stops):
                if isinstance(color, QColor):
                    color = f"rgba({','.join(map(str, color.toTuple()))})"
                if value > 1:
                    value = value / 100
                data.append(f"stop: {value} {color}")

            if degree is not None:
                degree = f"x1: {math.cos(degree)}, y1: {math.sin(degree)}, x2: 1, y2: 1"
            else:
                x1, y1, x2, y2 = start.toTuple(), end.toTuple()
                degree = f"x1: {x1}, y1: {y1}, x2: {x2}, y2: {y2}"

            return f"qlineargradient({degree}, {', '.join(data)})"

    class BoxShadow(Element):
        def __init__(self, 
                     x: float,
                     y: float,
                     blur_radius: float,
                     color: Union[QColor, str]):

            if isinstance(color, QColor):
                color = f"rgba({','.join(map(str, color.toTuple()))})"

            return f"{x}px {y}px {blur_radius}px 0px {color}"

    def __init__(self,
                 qss: Union[dict, str],
                 vars: dict = None):

        self._qss = qss
        self._vars = vars
        self._temp = _QssTemplate("")
        self._parent = None

    def _set_parent(self, parent: object):
        self._parent = parent

    def _get_qss_from_str(self, qss: str) -> str:
        if qss.startswith(":") or os.path.exists(qss):
            file = QFile(qss)
            file.open(QFile.OpenModeFlag.ReadOnly)
            data = str(file.readAll(), "utf-8")

            # add .json support
            if qss.lower().endswith(".json"):
                data = self._get_qss_from_dict(json.loads(data))

            file.close()
            return data
        return qss

    def _get_qss_parent(self) -> str:
        _parent = self._parent.objectName().strip()
        if not _parent:
            _parent = self._parent.__class__.__base__.__name__
            return _parent
        return "#" + _parent

    def _get_qss_from_dict(self, qss: dict) -> str:
        style_sheet = ""
        _obj_style = ""

        for k, v in qss.items():
            if isinstance(v, dict) and not k.startswith(":"):
                raise ValueError("Invalid Qss parent!")

            if k.startswith(("#", ".", "*")):
                raise ValueError("Invalid Qss key value!")

            if isinstance(v, dict):
                style_sheet += "%s%s {\n" % (self._get_qss_parent(), k)
                for sk, sv in v.items():
                    style_sheet += f"\t{sk}: {sv};\n"
                style_sheet += "}\n"
            else:
                _obj_style += f"\t{k}: {v};\n"

        style_sheet += "%s {\n" % self._get_qss_parent()
        style_sheet += _obj_style
        style_sheet += "}\n"

        return style_sheet

    def _set_qss(self, qss: Union[dict, str]) -> None:
        if qss:
            _style = (self._get_qss_from_str(qss)
                    if isinstance(qss, str) 
                    else self._get_qss_from_dict(qss))

            if self._vars:
                self._temp.template = _style
                _style = self._temp.safe_substitute(self._vars)

            self._parent.setStyleSheet(_style)

    def update_vars(self, vars: dict) -> None:
        self._vars = vars
        self._set_qss(self._qss)

    def update_qss(self,
                   qss: Union[dict, str],
                   *,
                   save: bool = False) -> None:

        if self._qss is not None:
            if (isinstance(qss, dict) 
                and isinstance(self._qss, dict)):
                _qss = self._qss.copy()
                _qss.update(qss)
                self._qss = qss if save else self._qss
                _style = self._get_qss_from_dict(_qss)
            else:
                self._qss = qss if save else self._qss
                _style = self._get_qss_from_str(qss)
        else:
            _style = (
                self._get_qss_from_dict(qss)
                if isinstance(qss, dict)
                else
                self._get_qss_from_str(qss)
            )

            if save:
                self._qss = qss

        if self._vars:
            self._temp.template = _style
            self._temp.safe_substitute(_style)
            _style = self._temp.safe_substitute(self._vars)

        self._parent.setStyleSheet(_style)

    def restore_qss(self) -> None:
        if self._qss is not None:
            if isinstance(self._qss, dict):
                _style = self._get_qss_from_dict(self._qss)
            else:
                _style = self._get_qss_from_str(self._qss)

            if self._vars:
                self._temp.template = _style
                self._temp.safe_substitute(_style)
                _style = self._temp.safe_substitute(self._vars)

            self._parent.setStyleSheet(_style)
        else:
            self._parent.setStyleSheet("")

    def update(self, 
               qss: Union[dict, str], 
               vars: dict = None, 
               *,
               save: bool = False) -> None:

        if vars is not None:
            self.update_vars(vars)

        self.update_qss(qss, save=save)

    def restore(self) -> None:
        self.restore_qss()

    def style(cls,
              qss: Union[dict, str],
              vars: Mapping[str, object] = None) -> str:
        '''
        :param: qss: 
            - dict: {"background-color": "white"}
            - str : "QWidget { background-color: white; }"
            - str : ":/path/to/resoucre/file.qss",
            - str : "/path/to/local/file.qss"
            - str : "/path/to/local/file.json"
        '''
        if qss:
            _style = (cls._get_qss_from_str(qss)
                      if isinstance(qss, str) 
                      else cls._get_qss_from_dict(qss))
            if vars:
                _temp = _QssTemplate(_style)
                return _temp.safe_substitute(vars)
            return _style