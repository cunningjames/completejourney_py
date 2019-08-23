# Sample Test passing with nose and pytest

from completejourney_py import get_data

def test_get_data():
    data = get_data()

    assert len(data) == 8
    assert set(data.keys()) == set(['campaign_descriptions', 'coupons', 'promotions',
                                    'campaigns', 'demographics', 'transactions',
                                    'coupon_redemptions', 'products'])
    for _, item in data.items():
        assert item.shape[0] > 0 and item.shape[1] > 0
