import pytest
import math
from render import contact_shadow as mod

CASES = [
    ("offset", 'm.ray_start_offset((0.5, 0.5), 0.01) == approx((0.51, 0.51))'),
    ("step", 'm.step_scale(2, 0.5) == approx(1.0)'),
    ("thick", 'm.thickness(10, 0.02) == approx(0.2)'),
    ("sign", 'm.depth_sign(-1) == -1'),
    ("normal", 'm.normal_offset((0, 1), 0.1) == approx((0.0, 0.1))'),
    ("reset", 'm.reset_history(True) is True'),
    ("transparent", 'm.transparent_occluder(0.5) is False'),
    ("offscreen", 'm.offscreen_result((1.2, 0.5)) == 0.0'),
    ("light", 'm.light_dir((0, -1)) == (0, -1)'),
    ("amount", 'm.contact_amount(True, True) == 1.0'),
    ("key", 'm.shadow_key("L", 2) == "L:2"'),
    ("project", 'm.project_uv((0.5, 0.5), 100) == (50.0, 50.0)'),
    ("valid", 'm.valid_uv((0.5, 0.5)) is True'),
    ("blend", 'm.history_blend(1, 3, 0.5) == approx(2.0)'),
    ("id", 'm.contact_id(3, 2) == "3:2"')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
