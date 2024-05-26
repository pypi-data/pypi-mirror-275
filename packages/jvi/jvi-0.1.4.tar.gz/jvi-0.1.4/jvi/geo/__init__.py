# from jvi.geo.point2d import Point
# from jvi.geo.rectangle import Rect
# from jvi.geo.size2d import Size


def is_normalized(v: float) -> bool:
    """判断坐标是否被归一化, 允许稍微越界, 这在绘图中常见"""
    return -0.01 <= v <= 1.01


def to_zero(v: float) -> float:
    """接近零的数据转为零"""
    return v if abs(v) > 0.00001 else 0
