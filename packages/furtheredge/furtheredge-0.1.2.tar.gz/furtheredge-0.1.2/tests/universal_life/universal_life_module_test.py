# from furtheredge.abstracted_packages import furtheredge_pandas as pd
# from pandas.testing import assert_frame_equal
# from furtheredge.modules.universal_life.run import universal_life_module


# def should_return_universal_life_product():
#     # Given
#     model_points = pd.read_csv("furtheredge/inputs/model_points2.csv")
#     ri_rates = pd.read_csv(
#         "furtheredge/inputs/ri_rates.csv", sep=";", decimal=","
#     )
#     wop_rates = pd.read_csv(
#         "furtheredge/inputs/wop_rates.csv", sep=";", decimal=","
#     )
#     tech_assumptions = pd.read_csv(
#         "furtheredge/inputs/tech_assumptions.csv", sep=";", decimal=","
#     )
#     product = pd.read_csv(
#         "furtheredge/inputs/product.csv", sep=";", decimal=","
#     )

#     # expected = pd.read_csv("furtheredge/outputs/universal_life_output.csv")
#     # expected["fin_mois"] = pd.to_datetime(expected["fin_mois"])

#     # When
#     result_universal_life = universal_life_module(
#         model_points,
#         {"time_horizon": 50, "projection_date": "2023-10-01"},
#         tech_assumptions,
#         ri_rates,
#         wop_rates,
#         product,
#     )

#     # Then
#     # assert_frame_equal(result_universal_life, expected)
