import pandas as pd

def read_all():
    sources = ["campaign_descriptions",
               "coupons",
               "promotions",
               "campaigns",
               "demographics",
               "transactions",
               "coupon_redemptions",
               "products"]

    return dict(map(lambda src: (src, pd.read_parquet(f"./data/{src}.parquet")),
                    sources))
