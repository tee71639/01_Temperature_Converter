# component that converts degrees celsius to fahrenheit
# function takes in value, converts it and puts answer into a list


def to_c(from_f):
    celsius = (from_f - 32) * 5/9 
    return celsius


# main routine
temperatures = [0, 40, 100]
converted = []

for item in temperatures:
    answer = to_c(item)
    ans_statement = "{} degrees F is {} degrees C".format(item, answer)
    converted.append(ans_statement)


print(converted)