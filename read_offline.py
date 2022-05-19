from datetime import datetime, timedelta
from feast import FeatureStore

# Initialize a FeatureStore with our current repository's configurations
store = FeatureStore(repo_path=".")

# Get training data
now = datetime.now()
two_days_ago = datetime.now() - timedelta(days=2)

training_data = store.get_historical_features(
    entity_df=f"""
    select 
        src_account as user_id,
        timestamp,
        is_fraud
    from
        feast-oss.fraud_tutorial.transactions
    where
        timestamp between timestamp('{two_days_ago.isoformat()}') 
        and timestamp('{now.isoformat()}')""",
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

training_data.head()