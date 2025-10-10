from typing import Dict, Set
import pandas as pd
from completejourney_py import get_data

def test_get_data() -> None:
    data: Dict[str, pd.DataFrame] = get_data()

    assert len(data) == 8
    expected_keys: Set[str] = {'campaign_descriptions', 'coupons', 'promotions',
                               'campaigns', 'demographics', 'transactions',
                               'coupon_redemptions', 'products'}
    assert set(data.keys()) == expected_keys
    for _, item in data.items():
        assert item.shape[0] > 0 and item.shape[1] > 0
