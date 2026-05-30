
from pyspark.sql import functions as F
from pyspark.sql import types as T
from transforms.api import transform_df, Input, Output


@transform_df(
    Output(
        "/Hirendra_project-829831/Learning (Hirendra)/Code Repo Training/Prepared/claims"
    ),
    claims_df=Input("ri.foundry.main.dataset.3bbe6bea-9476-4ce2-a470-1af7b9d2f145"),
    policies_df=Input("ri.foundry.main.dataset.63c4572e-1126-45dc-bf1a-b5555d871bc0"),
)
def compute(claims_df, policies_df):

    # 1. Clean malformed date column — strip '###' artifacts before casting
    claims = claims_df.withColumn(
        "date", F.regexp_replace("date", "###", "").cast(T.DateType())
    )

    # 2. Keep only accepted claims
    claims = claims.filter(F.col("is_accepted") == True)

    # 3. Enrich claims with policy metadata
    claims = claims.join(policies_df, on="policy_id", how="left")

    # 4. Aggregate: average claim value per line of business
    claims_aggregated = claims.groupBy("line_of_business").agg(
        F.avg("claim_value").alias("avg_claim_cost")
    )

    return claims_aggregated
