def convert_date(date):
    parts = date.split('/')

    if len(parts) != 3:
        return "Wrong date format!"

    month, day, year = parts

    #zastosowanie f-stringa

    new_date_format = f"{year}{day.zfill(2)}{month.zfill(2)}" #zfill- uzupełnia zerami

    return new_date_format

date_input = input("Specify a date, in format: MM/DD/YYYY ")
converted_date = convert_date(date_input)

if converted_date != "Błędny format":
    print("Converted date: ", converted_date)
else:
    print("Wrong date format.Specify a date, in format: MM/DD/YYYY")

