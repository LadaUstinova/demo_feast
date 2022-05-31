from datetime import datetime
from datetime import timedelta
from feast import FeatureStore
import pandas as pd

entity_df = pd.DataFrame.from_dict(
    {
        "customer_rk": [688, 689, 699],
        "event_timestamp": [
            datetime.now() - timedelta(days=60, minutes=36),
            datetime.now() - timedelta(days=60, minutes=36),
            datetime.now() - timedelta(days=60, minutes=36),
        ],
    }
)
store = FeatureStore(repo_path=".")
training_data = store.get_historical_features(
    entity_df=entity_df,
    features=[
        "dataset_credit_history:cnt_ch_req_eqs_3m",
        "dataset_credit_history:cnt_ch_req_eqs_2m",
        "dataset_credit_history:cnt_ch_req_eqs_1m",
        "dataset_sal:avg_sal_amt_all_1y",
        "dataset_socdem:vip_flg",
        "dataset_socdem:gender",
        "dataset_trn:min_trn_amt_usd_cash_4w"
    ],
    full_feature_names=True
).to_df()

print(training_data.head())


