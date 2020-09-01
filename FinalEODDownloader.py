# MOnthly Download

from nsepy.history import get_price_list
from datetime import date
from calendar import month_name, monthrange
import os

# Yearly EOD
def year_eod():
    y = input('Year: ')

    if not os.path.exists(y): os.makedirs(y); print(y + ' : Dir Created.')
    else: print(y + ': dir already exists.')

    for mon in range(1, 13):
        month = month_name[mon]
        if not os.path.exists(y+'/'+str(mon)+'-'+month):
            os.makedirs(y+'/'+str(mon)+'-'+month); print(y+'/'+str(mon)+'-'+month + ' : Dir Created.')
        else:
            print(y+'/'+str(mon)+'-'+month + ': dir already exists.');

        days = monthrange(int(y), mon)[1]
        print('No. of days in %s: %d'% (month, days))

        for dy in range(1, days+1):
            dt = date(int(y), mon, dy)
            try:
                if not os.path.exists(y+'/'+str(mon)+'-'+month +'/%s.csv' % (dt)):
                    df = get_price_list(dt)
                    df = df[(df.SERIES == 'EQ')]
                    df = df.drop(['TOTTRDVAL','ISIN', 'PREVCLOSE'], axis=1)
                    df.to_csv(y+'/'+str(mon)+'-'+month+'/%s.csv' % (dt), index=False)
                else: print(y+'/'+month + +'/%s.csv: file already exists.' % (dt))
            except Exception as e:
                print(e); continue;
            else: print('Downloaded : %s' % dt)

        else: print('Done: ' + month)
    else: print('Done: ' + y)


# Monthly EOD
def month_eod():
    year = input('Year: ')
    month_no = int(input('Month(1-12): '))
    
    if not os.path.exists(year): os.makedirs(year); print(year + ' : Dir Created.')
    else: print(year + ': dir already exists.')

    month = month_name[int(month_no)]

    if not os.path.exists(year+'/'+str(month_no)+'-'+month):
        os.makedirs(year+'/'+str(month_no)+'-'+month)
        print(year+'/'+str(month_no)+'-'+month + ' : Dir Created.')
    else:
        print(year+'/'+str(month_no)+'-'+month + ': dir already exists.')

    days = monthrange(int(year), month_no)[1]

    print('No. of days in %s: %d'% (month, days))

    for dy in range(1, days+1):
        dt = date(int(year), month_no, dy)
        try:
            if not os.path.exists(year+'/'+str(month_no)+'-'+month +'/%s.csv' % (dt)):
                df = get_price_list(dt)
                df = df[(df.SERIES == 'EQ')]
                df = df.drop(['TOTTRDVAL','ISIN', 'PREVCLOSE'], axis=1)
                df.to_csv(year+'/'+str(month_no)+'-'+month+'/%s.csv' % (dt), index=False)
                print('Downloaded : %s' % dt)
            else: print(year+'/'+month + '/%s.csv: file already exists.' % (dt))
        except Exception as e:
            print(e); continue;	# 'Error While Dwnlding: ' +
        
    else: print('Done: ' + month)


# Today's EOD
def today_eod():
    dt = date.today()
    year = str(dt.year)
    month_no = dt.month

    if not os.path.exists(year): os.makedirs(year); print(year + ' : Dir Created.')
    else: print(year + ': dir already exists.')

    month = month_name[month_no]

    if not os.path.exists(year+'/'+str(month_no)+'-'+month):
        os.makedirs(year+'/'+str(month_no)+'-'+month)
        print(year+'/'+str(month_no)+'-'+month + ' : Dir Created.')
    else:
        print(year+'/'+str(month_no)+'-'+month + ': dir already exists.')

    try:
        if not os.path.exists(year+'/'+str(month_no)+'-'+month +'/%s.csv' % (dt)):
            df = get_price_list(dt)
            df = df[(df.SERIES == 'EQ')]
            df = df.drop(['TOTTRDVAL','ISIN', 'PREVCLOSE'], axis=1)
            df.to_csv(year+'/'+str(month_no)+'-'+month+'/%s.csv' % (dt), index=False)
            print('Downloaded : %s' % dt)
        else: print(year+'/'+month + '/%s.csv: file already exists.' % (dt))
    except Exception as e:
        print(e);

month_eod()
input('Enter to Exit')
quit()
