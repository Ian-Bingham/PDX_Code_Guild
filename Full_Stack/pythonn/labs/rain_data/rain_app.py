# rain_data.py 6/25/18

from operator import itemgetter
import matplotlib.pyplot as plt

inches_per_tick = 0.01


# calculate the mean total rain
def mean_rain(rain_list):
    total_sum = 0
    for date, total in rain_list:
        total_sum += total * inches_per_tick

    mean = total_sum / len(rain_list)
    return mean


# calculate the variance of rain
def variance_rain(rain_list, mean):
    total_diff = 0
    for date, total in rain_list:
        total_diff += ((total * inches_per_tick) - mean) ** 2

    variance = total_diff / len(rain_list)
    return variance


# find the day with the most rain
def rainiest_day(rain_list):
    # create a copy of the list so we don't alter the original
    # list when we do .sort()
    temp_rain_list = rain_list[::]

    # sort the list of tuples by value, reverse it,
    # then grab the the first tuple to get the date with the most rain
    temp_rain_list.sort(key=itemgetter(1), reverse=True)
    rainiestDay = temp_rain_list[0][0]
    return rainiestDay


# find the year with the most average rain
def rainiest_year(rain_list):
    current_year = rain_list[0][0][-4:]
    year_rain_dict = {}
    i = 0
    total_sum = 0

    for date, total in rain_list:
        # update variables for calculating mean
        if date[-4:] == current_year and date != rain_list[-1][0]:
            i += 1
            total_sum += total

        # calculate the mean once we've gathered all the data
        # for the current year and add it to the dictionary {year: mean}
        else:
            year_rain_dict[current_year] = total_sum * inches_per_tick / i
            i = 0
            total_sum = 0
            current_year = date[-4:]

    return max(year_rain_dict.items(), key=itemgetter(1))[0]


def main():
    with open('rain_data.txt', 'r', encoding='utf-8') as f:
        date_total_list = []  # list of tuples: (date, total rain)
        day_list = []
        total_rain_list = []
        i = 0

        # extract the date and total rain from each line (first two things)
        for line in f.readlines():
            i += 1
            text = line.split(None, 2)
            if text[1] == '-':
                continue
            day_list.append(i)
            total_rain_list.append(int(text[1]) * inches_per_tick)
            date_total_list.append((text[0], int(text[1])))

    mean = mean_rain(date_total_list)
    variance = variance_rain(date_total_list, mean)
    most_rain_day = rainiest_day(date_total_list)
    most_rain_year = rainiest_year(date_total_list)

    print("Mean rain: {} inches".format(mean))
    print("Variance rain: {} inches".format(variance))
    print("Rainiest day: {}".format(most_rain_day))
    print("Rainiest year: {}".format(most_rain_year))

    # plot the daily total rain vs day number
    plt.plot(day_list, total_rain_list)
    plt.xlabel('Day Number')
    plt.ylabel('Rain in Inches')
    plt.show()


main()
