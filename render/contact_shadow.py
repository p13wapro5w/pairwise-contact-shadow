import math

def ray_start_offset(uv, pixel):
    """射线起点偏移。"""
    raise NotImplementedError("TODO: ray_start_offset")

def step_scale(distance, base):
    """步长缩放。"""
    raise NotImplementedError("TODO: step_scale")

def thickness(depth, scale):
    """厚度阈值。"""
    raise NotImplementedError("TODO: thickness")

def depth_sign(delta):
    """深度符号。"""
    raise NotImplementedError("TODO: depth_sign")

def normal_offset(normal, scale):
    """法线偏移。"""
    raise NotImplementedError("TODO: normal_offset")

def reset_history(moved):
    """移动重置。"""
    raise NotImplementedError("TODO: reset_history")

def transparent_occluder(alpha):
    """透明遮挡。"""
    raise NotImplementedError("TODO: transparent_occluder")

def offscreen_result(uv):
    """出屏结果。"""
    raise NotImplementedError("TODO: offscreen_result")

def light_dir(direction):
    """光源方向。"""
    raise NotImplementedError("TODO: light_dir")

def contact_amount(occluded, thickness_ok):
    """接触量。"""
    raise NotImplementedError("TODO: contact_amount")

def shadow_key(camera, index):
    """阴影键。"""
    raise NotImplementedError("TODO: shadow_key")

def project_uv(position, resolution):
    """屏幕投影。"""
    raise NotImplementedError("TODO: project_uv")

def valid_uv(uv):
    """UV 合法性。"""
    raise NotImplementedError("TODO: valid_uv")

def history_blend(history, current, alpha):
    """历史混合。"""
    raise NotImplementedError("TODO: history_blend")

def contact_id(seed, index):
    """接触 id。"""
    raise NotImplementedError("TODO: contact_id")
