# def future_value(present_value,annual_rate,period_per_year,years):
#     rate_per_peroid = annual_rate / period_per_year
#     periods = period_per_year = years
#     print("$1000 at 2% compounded daily for 4 years yields $",future_value{1000,7,365,4})


def future_value(present_value,annual_rate,period_per_year,years):
    rate_per_peroid = annual_rate / period_per_year
    periods = period_per_year * years
    ans = present_value*pow(1+rate_per_peroid,periods)
    return ans


a = future_value(500,0.04,10,10)
print(a)
