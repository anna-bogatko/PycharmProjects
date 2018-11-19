
# car = {'make': 'bmw', 'model': 'i550', 'year': '2011'}
#
# def carFeatures():
#     try:
#         print(car['color'])
#     except:
#         print("There is no color present in the dictionary")
#     finally:
#         print("I do not care what values have been given :-)")
#
# carFeatures()


def carFeatures():
    try:
        car = {'make': 'bmw', 'model': 'i550', 'year': '2011'}
        print(car['color'])
    except:
        print("There is no color present in the dictionary")
    finally:
        print("I do not care what values have been given :-)")

carFeatures()