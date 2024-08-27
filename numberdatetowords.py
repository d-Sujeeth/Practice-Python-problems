date_str = "19/01/2004"
month_dict = {
    1: "January", 2: "February", 3: "March", 4: "April", 5: "May",
    6: "June", 7: "July", 8: "August", 9: "September", 10: "October",
    11: "November", 12: "December"
}

parts = date_str.split("/")

day,month,year=parts
month=int(month)
monthstr=month_dict[month]
print(day+"th",monthstr,year)