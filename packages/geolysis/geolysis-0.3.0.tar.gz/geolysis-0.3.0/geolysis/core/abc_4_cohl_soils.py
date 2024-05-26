from abc import ABC, abstractmethod

from geolysis.core.constants import UNIT
from geolysis.core.foundation import FoundationSize
from geolysis.core.utils import round_

__all__ = [
    "BowlesABC4PadFoundation",
    "BowlesABC4MatFoundation",
    "MeyerhofABC4PadFoundation",
    "MeyerhofABC4MatFoundation",
    "TerzaghiABC4PadFoundation",
    "TerzaghiABC4MatFoundation",
]

kPa = UNIT.kPa


class SettlementError(ValueError):
    pass


def _chk_settlement(tol_settlement: float, max_tol_settlement: float):
    if tol_settlement > max_tol_settlement:
        err_msg = "tol_settlement should not be greater than 25.4."
        raise SettlementError(err_msg)


class _AbstractABC(ABC):

    MAX_TOL_SETTLEMENT = 25.4

    _unit = kPa

    def __init__(
        self,
        corrected_spt_number: float,
        tol_settlement: float,
        foundation_size: FoundationSize,
    ) -> None:

        self.corrected_spt_number = corrected_spt_number
        self.tol_settlement = tol_settlement
        self.foundation_size = foundation_size

        _chk_settlement(self.tol_settlement, self.MAX_TOL_SETTLEMENT)

    @property
    def unit(self) -> str:
        return self._unit

    @property
    def f_depth(self) -> float:
        """Depth of foundation."""
        return self.foundation_size.depth

    @f_depth.setter
    def f_depth(self, __val: float):
        self.foundation_size.depth = __val

    @property
    def f_width(self) -> float:
        """Width of foundation footing."""
        return self.foundation_size.width

    @f_width.setter
    def f_width(self, __val):
        self.foundation_size.width = __val

    @property
    def FD(self) -> float:
        """Depth factor."""
        return min(1 + 0.33 * self.f_depth / self.f_width, 1.33)

    @property
    def SR(self) -> float:
        """Settlement ratio."""
        return self.tol_settlement / self.MAX_TOL_SETTLEMENT

    @abstractmethod
    def bearing_capacity(self) -> float:
        raise NotImplementedError


class BowlesABC4PadFoundation(_AbstractABC):
    r"""Allowable bearing capacity for mat foundation on cohesionless
    soils according to ``Bowles (1997)``.

    Parameters
    ----------
    corrected_spt_number : float
        Statistical average of corrected SPT N-value (55% energy with
        overburden pressure correction) within the foundation influence
        zone i.e ``0.5B`` to ``2B``.
    tol_settlement : float, mm
        Tolerable settlement.
    foundation_size : FoundationSize
        Size of foundation.

    Attributes
    ----------
    f_depth : float
    f_width : float

    Notes
    -----
    Allowable bearing capacity for ``isolated/pad/spread`` foundations:

    .. math::

        q_a(kPa) &= 19.16(N_1)_{55} f_d\left(\dfrac{S}{25.4}\right),
                    \ B \ \le \ 1.2m

        q_a(kPa) &= 11.98(N_1)_{55}\left(\dfrac{3.28B + 1}{3.28B} \right)^2
                    f_d \left(\dfrac{S}{25.4}\right), \ B \ \gt 1.2m

    Depth factor:

    .. math:: f_d = 1 + 0.33 \cdot \frac{D_f}{B} \le 1.33

    Examples
    --------
    >>> from geolysis.core.abc_4_cohl_soils import BowlesABC4PadFoundation
    >>> from geolysis.core.foundation import create_foundation, Shape

    >>> foundation_size = create_foundation(depth=1.5, thickness=0.3,
    ...                                     width=1.2, footing_shape=Shape.SQUARE)
    >>> bowles_abc = BowlesABC4PadFoundation(corrected_spt_number=17.0,
    ...                                      tol_settlement=20.0,
    ...                                      foundation_size=foundation_size)
    >>> bowles_abc.bearing_capacity()
    341.1083
    """

    @round_
    def bearing_capacity(self) -> float:
        """Return allowable bearing capacity for isolated foundation on
        cohesionless soils. |rarr| :math:`kN/m^2`
        """
        if self.f_width <= 1.2:
            return 19.16 * self.corrected_spt_number * self.FD * self.SR

        return (
            11.98
            * self.corrected_spt_number
            * ((3.28 * self.f_width + 1) / (3.28 * self.f_width)) ** 2
            * self.FD
            * self.SR
        )


class BowlesABC4MatFoundation(_AbstractABC):
    r"""Allowable bearing capacity for mat foundation on cohesionless
    soils according to ``Bowles (1997)``.

    Parameters
    ----------
    corrected_spt_number : float
        Statistical average of corrected SPT N-value (55% energy with
        overburden pressure correction) within the foundation influence
        zone i.e ``0.5B`` to ``2B``.
    tol_settlement : float, mm
        Tolerable settlement.
    foundation_size : FoundationSize
        Size of foundation.

    Attributes
    ----------
    f_depth : float
    f_width : float

    Notes
    -----
    Allowable bearing capacity for ``raft/mat`` foundations:

    .. math:: q_a(kPa) = 11.98(N_1)_{55}f_d\left(\dfrac{S}{25.4}\right)

    Depth factor:

    .. math:: f_d = 1 + 0.33 \cdot \frac{D_f}{B} \le 1.33

    Examples
    --------
    >>> from geolysis.core.abc_4_cohl_soils import BowlesABC4MatFoundation
    >>> from geolysis.core.foundation import create_foundation, Shape

    >>> foundation_size = create_foundation(depth=1.5, thickness=0.3,
    ...                                     width=1.2, footing_shape=Shape.SQUARE)
    >>> bowles_abc = BowlesABC4MatFoundation(corrected_spt_number=17.0,
    ...                                      tol_settlement=20.0,
    ...                                      foundation_size=foundation_size)
    >>> bowles_abc.bearing_capacity()
    213.2817
    """

    @round_
    def bearing_capacity(self) -> float:
        """Return allowable bearing capacity for raft foundation on
        cohesionless soils. |rarr| :math:`kN/m^2`
        """
        return 11.98 * self.corrected_spt_number * self.FD * self.SR


class MeyerhofABC4PadFoundation(_AbstractABC):
    r"""Allowable bearing capacity for pad foundation on cohesionless
    soils according to ``Meyerhof (1956)``.

    Parameters
    ----------
    corrected_spt_number : float
        Average uncorrected SPT N-value (60% energy with dilatancy
        (water) correction if applicable) within the foundation influence
        zone i.e :math:`D_f` to :math:`D_f + 2B`
    tol_settlement : float, mm
        Tolerable settlement
    foundation_size : FoundationSize
        Size of foundation.

    Attributes
    ----------
    f_depth : float
    f_width : float

    Notes
    -----
    Allowable bearing capacity for ``isolated/pad/spread`` foundations:

    .. math::

        q_a(kPa) &= 12N f_d\left(\dfrac{S}{25.4}\right), \ B \ \le 1.2m

        q_a(kPa) &= 8N\left(\dfrac{3.28B + 1}{3.28B} \right)^2 f_d\left(
                     \dfrac{S}{25.4}\right), \ B \ \gt 1.2m

    Depth factor:

    .. math:: f_d = 1 + 0.33 \cdot \frac{D_f}{B} \le 1.33

    Examples
    --------
    >>> from geolysis.core.abc_4_cohl_soils import MeyerhofABC4PadFoundation
    >>> from geolysis.core.foundation import create_foundation, Shape

    >>> foundation_size = create_foundation(depth=1.5, thickness=0.3,
    ...                                     width=1.2, footing_shape=Shape.SQUARE)
    >>> meyerhof_abc = MeyerhofABC4PadFoundation(corrected_spt_number=17.0,
    ...                                          tol_settlement=20.0,
    ...                                          foundation_size=foundation_size)
    >>> meyerhof_abc.bearing_capacity()
    213.6378
    """

    @round_
    def bearing_capacity(self) -> float:
        """Return allowable bearing capacity for isolated foundation on
        cohesionless soils. |rarr| :math:`kN/m^2`
        """

        if self.f_width <= 1.2:
            return 12 * self.corrected_spt_number * self.FD * self.SR

        return (
            8
            * self.corrected_spt_number
            * ((3.28 * self.f_width + 1) / (3.28 * self.f_width)) ** 2
            * self.FD
            * self.SR
        )


class MeyerhofABC4MatFoundation(_AbstractABC):
    r"""Allowable bearing capacity for mat foundation on cohesionless
    soils according to ``Meyerhof (1956)``.

    Parameters
    ----------
    corrected_spt_number : float
        Average uncorrected SPT N-value (60% energy with dilatancy
        (water) correction if applicable) within the foundation influence
        zone i.e :math:`D_f` to :math:`D_f + 2B`
    tol_settlement : float, mm
        Tolerable settlement
    foundation_size : FoundationSize
        Size of foundation.

    Attributes
    ----------
    f_depth : float
    f_width : float

    Notes
    -----
    Allowable bearing capacity for ``raft/mat`` foundations:

    .. math:: q_a(kPa) = 8 N f_d\left(\dfrac{S}{25.4}\right)

    Depth factor:

    .. math:: f_d = 1 + 0.33 \cdot \frac{D_f}{B} \le 1.33

    Examples
    --------
    >>> from geolysis.core.abc_4_cohl_soils import MeyerhofABC4MatFoundation
    >>> from geolysis.core.foundation import create_foundation, Shape

    >>> foundation_size = create_foundation(depth=1.5, thickness=0.3,
    ...                                     width=1.2, footing_shape=Shape.SQUARE)
    >>> meyerhof_abc = MeyerhofABC4MatFoundation(corrected_spt_number=17.0,
    ...                                          tol_settlement=20.0,
    ...                                          foundation_size=foundation_size)
    >>> meyerhof_abc.bearing_capacity()
    142.4252
    """

    @round_
    def bearing_capacity(self) -> float:
        """Return allowable bearing capacity for raft foundation on
        cohesionless soils. |rarr| :math:`kN/m^2`
        """
        return 8 * self.corrected_spt_number * self.FD * self.SR


class TerzaghiABC4PadFoundation(_AbstractABC):
    r"""Allowable bearing capacity for pad foundation on cohesionless
    soils according to ``Terzaghi & Peck (1948)``.

    Parameters
    ----------
    corrected_spt_number : float
        Lowest (or average) uncorrected SPT N-value (60% energy) within
        the foundation influence zone i.e :math:`D_f` to :math:`D_f + 2B`
    tol_settlement : float, mm
        Tolerable settlement.
    water_depth : float, m
        Depth of water below ground surface.
    foundation_size : float
        Size of foundation.

    Attributes
    ----------
    f_depth : float
    f_width : float

    Notes
    -----
    Allowable bearing capacity for ``isolated/pad/spread`` foundations:

    .. math::

        q_a(kPa) &= 12N \dfrac{1}{c_w f_d}\left(\dfrac{S}{25.4}\right),
                    \ B \ \le 1.2m

        q_a(kPa) &= 8N\left(\dfrac{3.28B + 1}{3.28B} \right)^2\dfrac{1}
                    {c_w f_d}\left(\dfrac{S}{25.4}\right), \ B \ \gt 1.2m

    Depth factor:

    .. math:: f_d = 1 + 0.25 \cdot \frac{D_f}{B} \le 1.25

    Water correction for surface footing:

    .. math:: c_w = 2 - \frac{D_w}{2B} \le 2

    Water correction for fully submerged footing :math:`D_w \le D_f`

    .. math:: c_w = 2 - \frac{D_f}{2B} \le 2

    Examples
    --------
    >>> from geolysis.core.abc_4_cohl_soils import TerzaghiABC4PadFoundation
    >>> from geolysis.core.foundation import create_foundation, Shape

    >>> foundation_size = create_foundation(depth=1.5, thickness=0.3,
    ...                                     width=1.2, footing_shape=Shape.SQUARE)
    >>> terzaghi_abc = TerzaghiABC4PadFoundation(corrected_spt_number=17,
    ...                                          tol_settlement=20.0, water_depth=1.2,
    ...                                          foundation_size=foundation_size)
    >>> terzaghi_abc.bearing_capacity()
    93.4574
    """

    def __init__(
        self,
        corrected_spt_number: float,
        tol_settlement: float,
        water_depth: float,
        foundation_size: FoundationSize,
    ):
        super().__init__(corrected_spt_number, tol_settlement, foundation_size)

        self.water_depth = water_depth

    @property
    @round_
    def FD(self):
        """Depth factor.

        :meta private:
        """

        return min(1 + 0.25 * self.f_depth / self.f_width, 1.25)

    @property
    @round_
    def CW(self):
        """Water correction factor.

        :meta private:
        """
        if self.water_depth <= self.f_depth:
            corr = 2 - self.f_depth / (2 * self.f_width)
        else:
            corr = 2 - self.water_depth / (2 * self.f_width)
        return min(corr, 2)

    @round_
    def bearing_capacity(self) -> float:
        """Return allowable bearing capacity for isolated foundation on
        cohesionless soils. |rarr| :math:`kN/m^2`
        """
        correction = 1 / (self.CW * self.FD)

        if self.f_width <= 1.2:
            return 12 * self.corrected_spt_number * correction * self.SR

        return (
            8
            * self.corrected_spt_number
            * ((3.28 * self.f_width + 1) / (3.28 * self.f_width)) ** 2
            * correction
            * self.SR
        )


class TerzaghiABC4MatFoundation(TerzaghiABC4PadFoundation):
    r"""Allowable bearing capacity for mat foundation on cohesionless soils
    according to ``Terzaghi & Peck (1948)``.

    Parameters
    ----------
    corrected_spt_number : float
        Lowest (or average) uncorrected SPT N-value (60% energy) within
        the foundation influence zone i.e :math:`D_f` to :math:`D_f + 2B`
    tol_settlement : float, mm
        Tolerable settlement.
    water_depth : float, m
        Depth of water below ground surface.
    foundation_size : float
        Size of foundation.

    Attributes
    ----------
    f_depth : float
    f_width : float

    Notes
    -----
    Allowable bearing capacity for ``isolated/pad/spread`` foundations:

    .. math:: q_a(kPa) = 8N\dfrac{1}{c_w f_d}\left(\dfrac{S}{25.4}\right)

    Depth factor:

    .. math:: f_d = 1 + 0.25 \cdot \frac{D_f}{B} \le 1.25

    Water correction for surface footing:

    .. math:: c_w = 2 - \frac{D_w}{2B} \le 2

    Water correction for fully submerged footing :math:`D_w \le D_f`

    .. math:: c_w = 2 - \frac{D_f}{2B} \le 2

    Examples
    --------
    >>> from geolysis.core.abc_4_cohl_soils import TerzaghiABC4MatFoundation
    >>> from geolysis.core.foundation import create_foundation, Shape

    >>> foundation_size = create_foundation(depth=1.5, thickness=0.3,
    ...                                     width=1.2, footing_shape=Shape.SQUARE)
    >>> terzaghi_abc = TerzaghiABC4MatFoundation(corrected_spt_number=17,
    ...                                          tol_settlement=20.0, water_depth=1.2,
    ...                                          foundation_size=foundation_size)
    >>> terzaghi_abc.bearing_capacity()
    62.3049
    """

    @round_
    def bearing_capacity(self) -> float:
        """Return allowable bearing capacity for raft foundation on
        cohesionless soils. |rarr| :math:`kN/m^2`
        """
        return (
            8 * self.corrected_spt_number * (1 / (self.CW * self.FD)) * self.SR
        )
