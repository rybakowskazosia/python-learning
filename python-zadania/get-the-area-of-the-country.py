# country_name = input("Name the country: ")
# country_area = float(input("Specify the area of the country: "))


# total_world_landmass = 148940000

# ratio = (country_area / total_world_landmass) * 100
# rounded_ratio = round(ratio, 2)
# print(rounded_ratio)

def area_of_country():
    total_world_landmass = 148940000

    country_name = input("Name the country: ")
    country_area = float(input("Specify the area of the country: "))

    ratio = (country_area / total_world_landmass) * 100
    rounded_ratio = round(ratio,2)

    return f"Area of {country_name} accounts for {rounded_ratio:.4f}% of the world's total landmass."  #z chatu GPT, jak wyświetlić wartości zmiennych w sroodku napisu

result = area_of_country()
print(result)

    
