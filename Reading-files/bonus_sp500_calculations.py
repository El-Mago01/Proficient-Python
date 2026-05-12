import statistics

with open('SP500.txt', 'r') as fileobj:
    header = fileobj.readline()
    financial_entries = fileobj.readlines()
    SP_list = []
    highest_long_term_interest_rate = 0.0
    for entry in financial_entries:
        date, sp500, dividend, earnings, consumer_price_index, long_interest_rate, real_price , real_dividend, real_earnings, pe10 = entry.split(
            ',')
        month, day, year = date.split('/')
        print("month = ", month)
        print("year = ", year)
        if (int(year) == 2016 and int(month) >= 6) or (int(year) == 2017 and int(month) <= 5):
                print("sp500 = ", sp500)
                SP_list.append(float(sp500))
                if float(long_interest_rate) > highest_long_term_interest_rate:
                    highest_long_term_interest_rate = float(long_interest_rate)
    print("SP_List", SP_list)
    max_interest = highest_long_term_interest_rate
    mean_SP = statistics.mean(SP_list)

    print(f"max_interest = {max_interest} | mean_SP = {mean_SP}")
