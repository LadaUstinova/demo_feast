from feast import FeatureStore

features = [
    "dataset_credit_history:cnt_ch_req_eqs_3m",
    "dataset_socdem:customer_age",
    "dataset_sal:avg_sal_amt_all_1y",
    "dataset_trn:min_trn_amt_usd_cash_4w"
]

fs = FeatureStore(repo_path=".")
feature_vector = fs.get_online_features(
    features=features,
    entity_rows=[
        {"customer_rk": 687},
        {"customer_rk": 689},
        {"customer_rk": 699}]
).to_dict()

print(feature_vector)
