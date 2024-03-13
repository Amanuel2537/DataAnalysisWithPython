# using head to select whatever we went starting from the first row
import pandas as pd
data=pd.read_json("https://www.w3schools.com/python/pandas/data.js")
print(data.head(5))
print(data.info())
# Json file as python dictionary 
# import pandas as pd

# data = {
#   "Duration":{
#     "0":60,
#     "1":60,
#     "2":60,
#     "3":45,
#     "4":45,
#     "5":60
#   },
#   "Pulse":{
#     "0":110,
#     "1":117,
#     "2":103,
#     "3":109,
#     "4":117,
#     "5":102
#   },
#   "Maxpulse":{
#     "0":130,
#     "1":145,
#     "2":135,
#     "3":175,
#     "4":148,
#     "5":127
#   },
#   "Calories":{
#     "0":409,
#     "1":479,
#     "2":340,
#     "3":282,
#     "4":406,
#     "5":300
#   }
# }

# df = pd.DataFrame(data)

# print(df) 

#importing Jason File
# import pandas as pd
# data=pd.read_json("https://www.w3schools.com/python/pandas/data.js")
# print(data.to_string())

#importing CSV files and returning maximum row

# import pandas as pd
# pd.options.display.max_rows=9999
# df=pd.read_csv(r"C:\Users\USER\Documents\Pyton\data.csv")
# print(df.to_string())



# #importing CSV files
# import pandas as pd
# df=pd.read_csv(r"C:\Users\USER\Documents\Pyton\data.csv")
# print(df.to_string())


#DataFrame exercise
# import pandas as pd

# myvar={
#     "Calories":[22,33,56],
#     "duration":[40,55,44]
# }
# data=pd.DataFrame(myvar)
# print(data)
# print(data.loc[0])
# print(data.loc[[0,1]])
# import pandas as pd

# calories = {"day1": 420, "day2": 380, "day3": 390}

# myvar = pd.Series(calories, index = ["day1", "day2"])

# print(myvar)

#pandas in indexing
# import pandas as pd
# a=[1,3,6,7]
# myvar=pd.Series(a,index=["x","y","z","b"])
# print(myvar)
# print(myvar["y"])

#pandas series Example

# import pandas as pd
# a=[1,2,7,5,7,8]
# myvar=pd.Series(a)
# print(myvar)









# import pandas as pd

# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }

# myvar = pd.DataFrame(mydataset)

# print(myvar)
# import pandas as pd
# df=pd.read_csv(r"C:\Users\USER\Documents\Coursera Class\Course 6\CSV tables\PATIENTS.csv")
# print(df.to_string())
#
#pandas Version
# import pandas as pd
# print(pd.__version__)