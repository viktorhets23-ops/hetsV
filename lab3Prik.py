vnesok_uah = 25000
uah_rate = 11.5 / 100
usd_rate = 4.0 / 100
buy_usd_rate = 27.0
sell_usd_rate_future = 28.6
total_uah = vnesok_uah * (1 + uah_rate)
vnesok_usd = vnesok_uah / buy_usd_rate
total_usd_in_usd = vnesok_usd * (1 + usd_rate)
total_usd_in_uah = total_usd_in_usd * sell_usd_rate_future

print(f"Сума через рік у гривні: {total_uah:.2f} грн")
print(f"Сума через рік у доларах (конвертована в грн): {total_usd_in_uah:.2f} грн")

if total_uah > total_usd_in_uah:
    print("Вигідніше зробити внесок у гривні.")
else:
    print("Вигідніше зробити внесок у доларах.")