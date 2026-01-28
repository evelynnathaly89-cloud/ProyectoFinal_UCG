from mi_pipeline_utils import is_monthly_contract

def test_is_monthly_contract_month_to_month():
    assert is_monthly_contract("Month-to-month") == 1

def test_is_monthly_contract_one_year():
    assert is_monthly_contract("One year") == 0
