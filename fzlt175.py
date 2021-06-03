def amort(rate, bal, term, num_payments):
    r = rate / 1200
    c = r * bal / (1 - (1 + r) ** (-term))
    for _ in range(1, num_payments):
        bal -= (c - r * bal)
    return f"num_payment {num_payments} c {round(c)} princ {round(c - r * bal)} int {round(r * bal)} balance {round(bal - (c - r * bal))}"
