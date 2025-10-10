from typing import Dict, List, Optional, Sequence, Union
import pandas as pd
from importlib import resources

def get_data(which: Optional[Union[str, Sequence[str]]] = None) -> Dict[str, pd.DataFrame]:
    """Returns datasets from the complete journey set.

    Args:
        which: which dataset(s) to read. Can be a string for a single dataset,
            a sequence of strings for multiple datasets, or left blank for all
            available datasets.
    Returns:
        A dictionary mapping dataset name to pandas data frames.
    """

    sources: List[str] = ["campaign_descriptions",
                          "coupons",
                          "promotions",
                          "campaigns",
                          "demographics",
                          "transactions",
                          "coupon_redemptions",
                          "products"]

    if which is None:
        which = sources
    elif isinstance(which, str):
        which = [which]
    else:
        which = list(which)

    def load_dataset(src: str) -> pd.DataFrame:
        data_file = resources.files("completejourney_py").joinpath(f"data/{src}.parquet")
        with data_file.open("rb") as f:
            return pd.read_parquet(f)
    
    return dict(map(lambda src: (src, load_dataset(src)), which))
