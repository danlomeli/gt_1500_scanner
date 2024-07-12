def test_sample_data(sample_data):
    """Test using the sample_data fixture."""
    assert sample_data["key"] == "value", "The value should be 'value'"


def test_example():
    """A simple test example."""
    assert 1 + 1 == 2, "1 + 1 should equal 2"
