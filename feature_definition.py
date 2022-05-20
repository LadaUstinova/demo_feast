#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

# This is an example feature definition file
from google.protobuf.duration_pb2 import Duration
from feast import Entity, Feature, FeatureView, FileSource, ValueType
from feast_postgres import PostgreSQLSource

# Read data from parquet files. Parquet is convenient for local development mode. For
# production, you can use your favorite DWH, such as BigQuery. See Feast documentation
# for more info.
dataset_trn = PostgreSQLSource(
    query="SELECT * FROM dataset_trn",
    event_timestamp_column="report_dttm",
)

dataset_socdem = PostgreSQLSource(
    query="SELECT * FROM dataset_socdem",
    event_timestamp_column="report_dttm",
)

dataset_sal = PostgreSQLSource(
   query="SELECT * FROM dataset_sal",
   event_timestamp_column="report_dttm",
)
dataset_credit_history = PostgreSQLSource(
   query="SELECT * FROM dataset_credit_history",
   event_timestamp_column="report_dttm",
)

# Define an entity for the driver. You can think of entity as a primary key used to
# fetch features.
customer = Entity(name="customer_rk", value_type=ValueType.STRING, description="customer id",)
#Our parquet files contain sample data that includes a driver_id column, timestamps and
# three feature column. Here we define a Feature View that will allow us to serve this
# data to our model online.

dataset_credit_history_view = FeatureView(
    name="dataset_credit_history",
    entities=["customer_rk"],
    ttl=Duration(seconds=86400 * 1),
    features=[
        Feature(name="cnt_ch_req_eqs_3m", dtype=ValueType.INT64),  #Êîëè÷åñòâî çàïðîñîâ â ÁÊÈ Ýêâèôàêñ çà 3 ìåñ
        Feature(name="cnt_ch_req_nbki_3m", dtype=ValueType.INT64), #Êîëè÷åñòâî çàïðîñîâ â ÁÊÈ ÍÁÊÈ çà 3 ìåñ
        Feature(name="cnt_ch_req_okb_3m", dtype=ValueType.INT64),  #Êîëè÷åñòâî çàïðîñîâ â ÁÊÈ ÎÊÁ çà 3 ìåñ 
        Feature(name="cnt_ch_req_eqs_2m", dtype=ValueType.INT64),
        Feature(name="cnt_ch_req_nbki_2m", dtype=ValueType.INT64),
        Feature(name="cnt_ch_req_okb_2m", dtype=ValueType.INT64),
        Feature(name="cnt_ch_req_eqs_1m", dtype=ValueType.INT64),
        Feature(name="cnt_ch_req_nbki_1m", dtype=ValueType.INT64),
        Feature(name="cnt_ch_req_okb_1m", dtype=ValueType.INT64),
    ],
    online=True,
    batch_source=dataset_credit_history,
    tags={},
)

dataset_socdem_view = FeatureView(
    name="dataset_socdem",
    entities=["customer_rk"],
    ttl=Duration(seconds=86400 * 1),
    features=[
        Feature(name="customer_age", dtype=ValueType.FLOAT),
        Feature(name="gender", dtype=ValueType.STRING),
        Feature(name="vip_flg", dtype=ValueType.STRING),      #Ïðèçíàê âèï
        Feature(name="industry_nm", dtype=ValueType.STRING),  #Îòðàñëü
        Feature(name="bki_cons_flg", dtype=ValueType.STRING), #Ïðèçíàê ñîãëàñèÿ íà çàïðîñû â ÁÊÈ
    ],
    online=True,
    batch_source=dataset_socdem,
    tags={},
)

dataset_sal_view = FeatureView(
    name="dataset_sal",
    entities=["customer_rk"],
    ttl=Duration(seconds=86400 * 1),
    features=[
        Feature(name="avg_sal_amt_all_1y", dtype=ValueType.FLOAT), #Ñðåäíåå çï-íà÷èñëåíèå èç âñåõ èñòî÷íèêîâ çà 1 ãîä
        Feature(name="avg_sal_amt_all_6m", dtype=ValueType.FLOAT), #Ñðåäíåå çï-íà÷èñëåíèå èç âñåõ èñòî÷íèêîâ çà 6 ìåñ
        Feature(name="avg_sal_amt_all_3m", dtype=ValueType.FLOAT), #Ñðåäíåå çï-íà÷èñëåíèå èç âñåõ èñòî÷íèêîâ çà 3 ìåñ
        Feature(name="avg_sal_amt_all_2m", dtype=ValueType.FLOAT), 
        Feature(name="avg_sal_amt_all_1m", dtype=ValueType.FLOAT), 
        
        Feature(name="sum_sal_amt_all_1y", dtype=ValueType.FLOAT), #Ñóììà çï-íà÷èñëåíèå èç âñåõ èñòî÷íèêîâ çà 1 ãîä
        Feature(name="sum_sal_amt_all_6m", dtype=ValueType.FLOAT), #Ñóììà çï-íà÷èñëåíèå èç âñåõ èñòî÷íèêîâ çà 6 ìåñ
        Feature(name="sum_sal_amt_all_3m", dtype=ValueType.FLOAT), #Ñóììà çï-íà÷èñëåíèå èç âñåõ èñòî÷íèêîâ çà 3 ìåñ
        Feature(name="sum_sal_amt_all_2m", dtype=ValueType.FLOAT), #Ñóììà çï-íà÷èñëåíèå èç âñåõ èñòî÷íèêîâ çà 2 ìåñ
        Feature(name="sum_sal_amt_all_1m", dtype=ValueType.FLOAT), #Ñóììà çï-íà÷èñëåíèå èç âñåõ èñòî÷íèêîâ çà 1 ìåñ
                
        Feature(name="max_sal_amt_all_1y", dtype=ValueType.FLOAT), #Ìàêñèìàëüíîå çï-íà÷èñëåíèå èç âñåõ èñòî÷íèêîâ çà 1 ãîä
        Feature(name="max_sal_amt_all_6m", dtype=ValueType.FLOAT), #Ìàêñèìàëüíîå çï-íà÷èñëåíèå èç âñåõ èñòî÷íèêîâ çà 6 ìåñ
        Feature(name="max_sal_amt_all_3m", dtype=ValueType.FLOAT), #Ìàêñèìàëüíîå çï-íà÷èñëåíèå èç âñåõ èñòî÷íèêîâ çà 3 ìåñ
        Feature(name="max_sal_amt_all_2m", dtype=ValueType.FLOAT), #Ìàêñèìàëüíîå çï-íà÷èñëåíèå èç âñåõ èñòî÷íèêîâ çà 2 ìåñ
        Feature(name="max_sal_amt_all_1m", dtype=ValueType.FLOAT), #Ìàêñèìàëüíîå çï-íà÷èñëåíèå èç âñåõ èñòî÷íèêîâ çà 1 ìåñ
    ], 
    online=True,
    batch_source=dataset_sal,
    tags={},
)

dataset_trn_view = FeatureView(
    name="dataset_trn",
    entities=["customer_rk"],
    ttl=Duration(seconds=86400 * 1),
    features=[
        Feature(name="min_trn_amt_usd_cash_4w", dtype=ValueType.INT64), #Ìèíèìàëüíàÿ ñóììà òðàíçàêöèè â äîëëàðàõ ïî ñíÿòèþ íàëè÷íûõ çà 4 íåäåëè
        Feature(name="min_trn_amt_rub_cash_4w", dtype=ValueType.INT64), #Ìèíèìàëüíàÿ ñóììà òðàíçàêöèè â ðóáëÿõ ïî ñíÿòèþ íàëè÷íûõ çà 4 íåäåëè
        Feature(name="min_trn_amt_usd_rtl_4w", dtype=ValueType.INT64),  #Ìèíèìàëüíàÿ ñóììà òðàíçàêöèè â äîëëàðàõ â êàòåãîðèè Retail çà 4 íåäåëè
        Feature(name="min_trn_amt_rub_rtl_4w", dtype=ValueType.INT64),  #Ìèíèìàëüíàÿ ñóììà òðàíçàêöèè â ðóáëÿõ â êàòåãîðèè Retail çà 4 íåäåëè
        
        Feature(name="min_trn_amt_usd_cash_3w", dtype=ValueType.INT64), #Ìèíèìàëüíàÿ ñóììà òðàíçàêöèè â äîëëàðàõ ïî ñíÿòèþ íàëè÷íûõ çà 3 íåäåëè
        Feature(name="min_trn_amt_rub_cash_3w", dtype=ValueType.INT64), #Ìèíèìàëüíàÿ ñóììà òðàíçàêöèè â ðóáëÿõ ïî ñíÿòèþ íàëè÷íûõ çà 3 íåäåëè
        Feature(name="min_trn_amt_usd_rtl_3w", dtype=ValueType.INT64),  #Ìèíèìàëüíàÿ ñóììà òðàíçàêöèè â äîëëàðàõ â êàòåãîðèè Retail çà 3 íåäåëè
        Feature(name="min_trn_amt_rub_rtl_3w", dtype=ValueType.INT64),  #Ìèíèìàëüíàÿ ñóììà òðàíçàêöèè â ðóáëÿõ â êàòåãîðèè Retail çà 3 íåäåëè
        
        Feature(name="min_trn_amt_usd_cash_3w", dtype=ValueType.INT64), #Ìèíèìàëüíàÿ ñóììà òðàíçàêöèè â äîëëàðàõ ïî ñíÿòèþ íàëè÷íûõ çà 2 íåäåëè
        Feature(name="min_trn_amt_rub_cash_3w", dtype=ValueType.INT64), #Ìèíèìàëüíàÿ ñóììà òðàíçàêöèè â ðóáëÿõ ïî ñíÿòèþ íàëè÷íûõ çà 2 íåäåëè
        Feature(name="min_trn_amt_usd_rtl_3w", dtype=ValueType.INT64),  #Ìèíèìàëüíàÿ ñóììà òðàíçàêöèè â äîëëàðàõ â êàòåãîðèè Retail çà 2 íåäåëè
        Feature(name="min_trn_amt_rub_rtl_3w", dtype=ValueType.INT64),  #Ìèíèìàëüíàÿ ñóììà òðàíçàêöèè â ðóáëÿõ â êàòåãîðèè Retail çà 2 íåäåëè
        
        Feature(name="min_trn_amt_usd_cash_3w", dtype=ValueType.INT64), #Ìèíèìàëüíàÿ ñóììà òðàíçàêöèè â äîëëàðàõ ïî ñíÿòèþ íàëè÷íûõ çà 1 íåäåëþ
        Feature(name="min_trn_amt_rub_cash_3w", dtype=ValueType.INT64), #Ìèíèìàëüíàÿ ñóììà òðàíçàêöèè â ðóáëÿõ ïî ñíÿòèþ íàëè÷íûõ çà 1 íåäåëþ
        Feature(name="min_trn_amt_usd_rtl_3w", dtype=ValueType.INT64),  #Ìèíèìàëüíàÿ ñóììà òðàíçàêöèè â äîëëàðàõ â êàòåãîðèè Retail çà 1 íåäåëþ
        Feature(name="min_trn_amt_rub_rtl_3w", dtype=ValueType.INT64),  #Ìèíèìàëüíàÿ ñóììà òðàíçàêöèè â ðóáëÿõ â êàòåãîðèè Retail çà 1 íåäåëþ
        
        Feature(name="max_trn_amt_usd_cash_4w", dtype=ValueType.INT64), #Ìèíèìàëüíàÿ ñóììà òðàíçàêöèè â äîëëàðàõ ïî ñíÿòèþ íàëè÷íûõ çà 4 íåäåëè
        Feature(name="max_trn_amt_rub_cash_4w", dtype=ValueType.INT64), #Ìèíèìàëüíàÿ ñóììà òðàíçàêöèè â ðóáëÿõ ïî ñíÿòèþ íàëè÷íûõ çà 4 íåäåëè
        Feature(name="max_trn_amt_usd_rtl_4w", dtype=ValueType.INT64),  #Ìèíèìàëüíàÿ ñóììà òðàíçàêöèè â äîëëàðàõ â êàòåãîðèè Retail çà 4 íåäåëè
        Feature(name="max_trn_amt_rub_rtl_4w", dtype=ValueType.INT64),  #Ìèíèìàëüíàÿ ñóììà òðàíçàêöèè â ðóáëÿõ â êàòåãîðèè Retail çà 4 íåäåëè
        
        Feature(name="max_trn_amt_usd_cash_3w", dtype=ValueType.INT64), #Ìèíèìàëüíàÿ ñóììà òðàíçàêöèè â äîëëàðàõ ïî ñíÿòèþ íàëè÷íûõ çà 3 íåäåëè
        Feature(name="max_trn_amt_rub_cash_3w", dtype=ValueType.INT64), #Ìèíèìàëüíàÿ ñóììà òðàíçàêöèè â ðóáëÿõ ïî ñíÿòèþ íàëè÷íûõ çà 3 íåäåëè
        Feature(name="max_trn_amt_usd_rtl_3w", dtype=ValueType.INT64),  #Ìèíèìàëüíàÿ ñóììà òðàíçàêöèè â äîëëàðàõ â êàòåãîðèè Retail çà 3 íåäåëè
        Feature(name="max_trn_amt_rub_rtl_3w", dtype=ValueType.INT64),  #Ìèíèìàëüíàÿ ñóììà òðàíçàêöèè â ðóáëÿõ â êàòåãîðèè Retail çà 3 íåäåëè
        
        Feature(name="max_trn_amt_usd_cash_3w", dtype=ValueType.INT64), #Ìèíèìàëüíàÿ ñóììà òðàíçàêöèè â äîëëàðàõ ïî ñíÿòèþ íàëè÷íûõ çà 2 íåäåëè
        Feature(name="max_trn_amt_rub_cash_3w", dtype=ValueType.INT64), #Ìèíèìàëüíàÿ ñóììà òðàíçàêöèè â ðóáëÿõ ïî ñíÿòèþ íàëè÷íûõ çà 2 íåäåëè
        Feature(name="max_trn_amt_usd_rtl_3w", dtype=ValueType.INT64),  #Ìèíèìàëüíàÿ ñóììà òðàíçàêöèè â äîëëàðàõ â êàòåãîðèè Retail çà 2 íåäåëè
        Feature(name="max_trn_amt_rub_rtl_3w", dtype=ValueType.INT64),  #Ìèíèìàëüíàÿ ñóììà òðàíçàêöèè â ðóáëÿõ â êàòåãîðèè Retail çà 2 íåäåëè
        
        Feature(name="max_trn_amt_usd_cash_3w", dtype=ValueType.INT64), #Ìèíèìàëüíàÿ ñóììà òðàíçàêöèè â äîëëàðàõ ïî ñíÿòèþ íàëè÷íûõ çà 1 íåäåëþ
        Feature(name="max_trn_amt_rub_cash_3w", dtype=ValueType.INT64), #Ìèíèìàëüíàÿ ñóììà òðàíçàêöèè â ðóáëÿõ ïî ñíÿòèþ íàëè÷íûõ çà 1 íåäåëþ
        Feature(name="max_trn_amt_usd_rtl_3w", dtype=ValueType.INT64),  #Ìèíèìàëüíàÿ ñóììà òðàíçàêöèè â äîëëàðàõ â êàòåãîðèè Retail çà 1 íåäåëþ
        Feature(name="max_trn_amt_rub_rtl_3w", dtype=ValueType.INT64),  #Ìèíèìàëüíàÿ ñóììà òðàíçàêöèè â ðóáëÿõ â êàòåãîðèè Retail çà 1 íåäåëþ
    ],
    online=True,
    batch_source=dataset_trn,
    tags={},
)
