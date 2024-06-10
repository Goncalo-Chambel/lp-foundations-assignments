from ..region import Region

def test_get_actual_countries(actual_countries):
    """Test to assert if the class method get_actual_countries is working"""
    assert actual_countries == Region.get_actual_countries()
    