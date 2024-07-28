def main():
    total = average = highest = lowest = 0.0
    monthlow = ''
    monthhigh = ''
    monthrain = [0.0]*12
    monthlist = ['January', 'February', 'March', 'April', 'May',
                  'June', 'July', 'August', 'September', 'October',
                  'November', 'December']

    for i in range(len(monthrain)):
            monthrain[i] = float(input('Enter the rainfall for ' + monthlist[i] + ': '))

    total = sum(monthrain)
    average = total / 12.0
    highest = max(monthrain)
    lowest = min(monthrain)

    # Highest
    monthhigh = monthrain.index(highest)
    highestmonth = monthlist[monthhigh]

    # Lowest
    monthlow = monthrain.index(lowest)
    lowestmonth = monthlist[monthlow]

    print('-------')
    print('Total rainfall:', total)
    print('Average rainfall:', average)
    print('Highest rainfall:', highestmonth, 'at', highest)
    print('Lowest rainfall:', lowestmonth, 'at', lowest)

main()
