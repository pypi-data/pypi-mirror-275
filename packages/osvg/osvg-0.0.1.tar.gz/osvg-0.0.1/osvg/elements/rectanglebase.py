"""
Module to define shared methods for rectangle-like classes.
"""

from typing_extensions import Unpack
import osvg.elements.elementbase
import osvg.positions
import osvg.float
import osvg.float_math


class RectangleBaseParams(osvg.elements.elementbase.SVGElementParams):
    """
    Keyword argument definition for RectangleBase class.
    """

    width: float | int | osvg.float.Const = 0
    height: float | int | osvg.float.Const = 0


class RectangleBase(osvg.elements.elementbase.SVGElement):
    # pylint: disable=no-member
    """
    Base class for rectangle-like Elements.
    """
    width = osvg.float.FloatProperty()
    height = osvg.float.FloatProperty()

    def __init__(self, **kwargs: Unpack[RectangleBaseParams]) -> None:
        super().__init__(**kwargs)
        self.width = kwargs.get("width", 0)
        self.height = kwargs.get("height", 0)
        self.create_default_connectors()

    def _connector_top_left(self):
        return osvg.positions.ShiftedPosition(
            origin=self.position,
            x_shift=osvg.float_math.Prod(self.width, -0.5),
            y_shift=osvg.float_math.Prod(self.height, -0.5),
        )

    def _connector_top_center(self):
        return osvg.positions.ShiftedPosition(
            origin=self.position,
            y_shift=osvg.float_math.Prod(self.height, -0.5),
        )

    def _connector_top_right(self):
        return osvg.positions.ShiftedPosition(
            origin=self.position,
            x_shift=osvg.float_math.Prod(self.width, 0.5),
            y_shift=osvg.float_math.Prod(self.height, -0.5),
        )

    def _connector_center_left(self):
        return osvg.positions.ShiftedPosition(
            origin=self.position,
            x_shift=osvg.float_math.Prod(self.width, -0.5),
        )

    def _connector_center(self):
        return osvg.positions.ShiftedPosition(origin=self.position)

    def _connector_center_right(self):
        return osvg.positions.ShiftedPosition(
            origin=self.position,
            x_shift=osvg.float_math.Prod(self.width, 0.5),
        )

    def _connector_bottom_left(self):
        return osvg.positions.ShiftedPosition(
            origin=self.position,
            x_shift=osvg.float_math.Prod(self.width, -0.5),
            y_shift=osvg.float_math.Prod(self.height, 0.5),
        )

    def _connector_bottom_center(self):
        return osvg.positions.ShiftedPosition(
            origin=self.position,
            y_shift=osvg.float_math.Prod(self.height, 0.5),
        )

    def _connector_bottom_right(self):
        return osvg.positions.ShiftedPosition(
            origin=self.position,
            x_shift=osvg.float_math.Prod(self.width, 0.5),
            y_shift=osvg.float_math.Prod(self.height, 0.5),
        )

    def create_default_connectors(self) -> None:
        """
        Create Positions as connectors and add them.
        """
        self.add_connector(
            self._connector_top_left(), name="top-left", respect_rotation=True
        )
        self.add_connector(
            self._connector_top_center(), name="top-center", respect_rotation=True
        )
        self.add_connector(
            self._connector_top_right(), name="top-right", respect_rotation=True
        )
        self.add_connector(
            self._connector_center_left(), name="center-left", respect_rotation=True
        )
        self.add_connector(self._connector_center(), "center")
        self.add_connector(
            self._connector_center_right(), name="center-right", respect_rotation=True
        )
        self.add_connector(
            self._connector_bottom_left(), name="bottom-left", respect_rotation=True
        )
        self.add_connector(
            self._connector_bottom_center(), name="bottom-center", respect_rotation=True
        )
        self.add_connector(
            self._connector_bottom_right(), name="bottom-right", respect_rotation=True
        )

    def add_connector_at_angle(self, angle: float | int | osvg.float.Float, name: str):
        """
        Add a connector at element's border at the angle
        in relation to the center.
        """
        # pylint: disable=too-many-return-statements,too-many-branches
        if not issubclass(type(angle), osvg.float.Float):
            angle = osvg.float.Const(angle)
        n_angle = angle.value % 360
        if name in self.connectors:
            raise ValueError(f"Connector with name {name} already exists")
        if n_angle == 0:
            self.connectors[name] = self.connectors["center-right"]
        else:
            if n_angle > 180:
                half_height = osvg.float_math.Prod(self.height, -0.5)
            else:
                half_height = osvg.float_math.Prod(self.height, 0.5)
            if 90 < n_angle < 270:
                half_width = osvg.float_math.Prod(self.width, -0.5)
            else:
                half_width = osvg.float_math.Prod(self.width, 0.5)
            cot_angle = osvg.float_math.InvertedSign(osvg.float_math.Cot(angle))
            x_shift = osvg.float_math.LowestAbs(
                half_width,
                osvg.float_math.Prod(cot_angle, half_height),
            )
            tan_angle = osvg.float_math.InvertedSign(osvg.float_math.Tan(angle))
            y_shift = osvg.float_math.LowestAbs(
                half_height,
                osvg.float_math.Prod(tan_angle, half_width),
            )
            self.add_connector(
                position=osvg.positions.ShiftedPosition(
                    origin=self.position,
                    x_shift=x_shift,
                    y_shift=y_shift,
                ),
                name=name,
                respect_rotation=True,
            )
        return self.connectors[name]
