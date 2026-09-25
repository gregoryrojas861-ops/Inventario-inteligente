from ai.recommendation import recommend_purchase

def test_recommendation():
    result = recommend_purchase(10, 50)
    assert result["recommended"] is True
    assert result["quantity"] == 40
