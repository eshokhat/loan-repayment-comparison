# logic/calculator.py

import pandas as pd

def calculate_annuity(loan_amount: float, annual_rate: float, months: int, grace_months=None) -> pd.DataFrame:
    """
    Calculates an amortization schedule for an annuity (fixed monthly payment) loan.
    """
    if grace_months is None:
        grace_months = []

    la = loan_amount
    ar = annual_rate / 12 / 100  # Monthly interest rate
    n = months

    grace_set = set(grace_months)
    repayment_months = n - len(grace_set)

    if repayment_months <= 0:
        raise ValueError("Grace period cannot cover entire loan term.")

    try:
        # Annuity (Shpitzer) formula
        monthly_payment = la * (ar * (1 + ar) ** repayment_months) / ((1 + ar) ** repayment_months - 1)
    except ZeroDivisionError:
        raise ValueError("Invalid interest rate or term.")
    
    schedule = []
    remaining = la

    for month in range(1, n + 1):
        if month in grace_set:
            interest = remaining * ar
            principal = 0
            payment = interest
        else:
            interest = remaining * ar
            principal = monthly_payment - interest
            payment = monthly_payment
            remaining -= principal

        schedule.append({
            "Month": month,
            "Payment": round(payment, 2),
            "Principal": round(principal, 2),
            "Interest": round(interest, 2),
            "Remaining Balance": round(max(remaining, 0), 2),
            "Grace": month in grace_set
        })

    return pd.DataFrame(schedule)


def calculate_linear(loan_amount: float, annual_rate: float, months: int, grace_months=None) -> pd.DataFrame:
    """
    Calculates an amortization schedule for a linear (equal principal) loan.
    """
    if grace_months is None:
        grace_months = []

    la = loan_amount
    ar = annual_rate / 12 / 100
    n = months

    grace_set = set(grace_months)
    repayment_months = n - len(grace_set)

    if repayment_months <= 0:
        raise ValueError("Grace period cannot cover entire loan term.")

    try:
        fixed_principal = la / repayment_months
    except ZeroDivisionError:
        raise ValueError("Invalid interest rate or term.")

    schedule = []
    remaining = la

    for month in range(1, n + 1):
        if month in grace_set:
            interest = remaining * ar
            principal = 0
            payment = interest
        else:
            interest = remaining * ar
            principal = fixed_principal
            payment = principal + interest
            remaining -= principal

        schedule.append({
            "Month": month,
            "Payment": round(payment, 2),
            "Principal": round(principal, 2),
            "Interest": round(interest, 2),
            "Remaining Balance": round(max(remaining, 0), 2),
            "Grace": month in grace_set
        })

    return pd.DataFrame(schedule)
