from src.shared.bikecalc import calculate_gear_ratios_rotated


def test_calculate_gear_ratios():
    gear_ratios = calculate_gear_ratios_rotated(36, 52, 14, 36)
    assert gear_ratios[48][16] == 3.0
    assert gear_ratios[40][20] == 2.0
    assert gear_ratios[36][36] == 1.0
