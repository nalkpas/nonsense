from scipy.special import comb

win_rate = 0.5

match_wr = win_rate**2 + win_rate**2*(1 - win_rate)*2
p_day_two = win_rate**7 + win_rate**7*(1 - win_rate)*7 + win_rate**7*(1 - win_rate)**2*comb(7,2)
small_cash = match_wr**6*(1 - match_wr)**2*comb(6,2)
big_cash = match_wr**7 + match_wr**7*(1 - match_wr)*7
day_two_ev = small_cash * 1000 + big_cash * 2000
ev = p_day_two * day_two_ev

print(ev)
print(day_two_ev)
