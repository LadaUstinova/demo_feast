from google.protobuf.duration_pb2 import Duration
from feast import Entity, Feature, FeatureView, FileSource, ValueType
from feast_postgres import PostgreSQLSource

dataset_socdem = PostgreSQLSource(
    query="SELECT * FROM dataset_socdem",
    event_timestamp_column="report_dttm",
)
customer = Entity(name="customer_rk", value_type=ValueType.STRING, description="customer id",)

dataset_socdem_view = FeatureView(
    name="dataset_socdem",
    entities=["customer_rk"],
    ttl=Duration(seconds=86400 * 1),
    features=[
        Feature(name="customer_age", dtype=ValueType.FLOAT),
        Feature(name="gender", dtype=ValueType.STRING),
        Feature(name="vip_flg", dtype=ValueType.STRING),      #Признак вип
        Feature(name="industry_nm", dtype=ValueType.STRING),  #Отрасль
        Feature(name="bki_cons_flg", dtype=ValueType.STRING), #Признак согласия на запросы в БКИ
    ],
    online=True,
    batch_source=dataset_socdem,
    tags={},
)




