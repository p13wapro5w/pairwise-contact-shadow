import math

def ray_start_offset(uv, pixel):
    """射线起点偏移：沿对角方向加一个像素级偏移，避免起点与表面采样点重合。"""
    return (uv[0] + pixel, uv[1] + pixel)

def step_scale(distance, base):
    """步长缩放：按屏幕距离自适应，步长 = base * distance。"""
    return base * distance

def thickness(depth, scale):
    """厚度阈值：随深度缩放，避免远处物体被整体判为遮挡。"""
    return depth * scale

def depth_sign(delta):
    """深度符号：带符号比较，区分正面遮挡与背面墙体。"""
    if delta > 0:
        return 1
    if delta < 0:
        return -1
    return 0

def normal_offset(normal, scale):
    """法线偏移：按视角/表面缩放，消除斜面漏光。"""
    return tuple(n * scale for n in normal)

def reset_history(moved):
    """移动重置：物体移动时丢弃 TAA 历史，防止阴影粘滞。"""
    return bool(moved)

def transparent_occluder(alpha):
    """透明遮挡：alpha < 1 的透明物体不写遮挡。"""
    return alpha >= 1.0

def offscreen_result(uv):
    """出屏结果：射线飞出屏幕边界返回未遮挡（0.0）。"""
    if not valid_uv(uv):
        return 0.0
    return 1.0

def light_dir(direction):
    """光源方向：按光源在屏幕空间的投影方向发射射线。"""
    return direction

def contact_amount(occluded, thickness_ok):
    """接触量：被遮挡且厚度有效时为完全接触。"""
    return 1.0 if (occluded and thickness_ok) else 0.0

def shadow_key(camera, index):
    """阴影键。"""
    return f"{camera}:{index}"

def project_uv(position, resolution):
    """屏幕投影：UV 坐标乘以分辨率得到像素坐标。"""
    return (position[0] * resolution, position[1] * resolution)

def valid_uv(uv):
    """UV 合法性：必须落在 [0, 1] 范围内。"""
    return 0.0 <= uv[0] <= 1.0 and 0.0 <= uv[1] <= 1.0

def history_blend(history, current, alpha):
    """历史混合：半分辨率噪声的时域累积。"""
    return history * (1.0 - alpha) + current * alpha

def contact_id(seed, index):
    """接触 id。"""
    return f"{seed}:{index}"
