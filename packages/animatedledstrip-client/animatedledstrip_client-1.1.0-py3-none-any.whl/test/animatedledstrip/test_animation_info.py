from animatedledstrip import AnimationInfo


def test_constructor():
    info = AnimationInfo()

    assert info.name == ''
    assert info.abbr == ''
    assert info.description == ''
    assert info.run_count_default == 0
    assert info.minimum_colors == 0
    assert info.unlimited_colors is False
    assert info.dimensionality == []
    assert info.int_params == []
    assert info.double_params == []
    assert info.string_params == []
    assert info.location_params == []
    assert info.distance_params == []
    assert info.rotation_params == []
    assert info.equation_params == []
