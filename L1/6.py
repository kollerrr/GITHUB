# сколько руб стоит один евро исходя из первых двух строк

def exchange_rate(rub_to_usd, usd_to_eur):

    eur_to_rub = 1/(rub_to_usd * usd_to_eur)
    return(eur_to_rub)

rub_to_usd = float(input())
usd_to_eur = float(input())


print(round(exchange_rate(rub_to_usd, usd_to_eur), 2))