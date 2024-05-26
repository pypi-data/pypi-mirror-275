# Test file for TomekLinks

import pandas
from ImbalancedLearningRegression import tomeklinks

## housing
housing = pandas.read_csv(
    "https://raw.githubusercontent.com/paobranco/ImbalancedLearningRegression/master/data/housing.csv"
)

## college
college = pandas.read_csv(
    "https://raw.githubusercontent.com/paobranco/ImbalancedLearningRegression/master/data/College.csv"
)

## red wine
red_wine = pandas.read_csv(
    "https://raw.githubusercontent.com/paobranco/ImbalancedLearningRegression/master/data/red_wine.csv"
)

# ## avocado
# avocado = pandas.read_csv(
#     "https://raw.githubusercontent.com/paobranco/ImbalancedLearningRegression/master/data/avocado.csv"
# )

## insurance
insurance = pandas.read_csv(
    "https://raw.githubusercontent.com/paobranco/ImbalancedLearningRegression/master/data/insurance.csv"
)

housing_basic = tomeklinks(
    data = housing, 
    y = "SalePrice" 
)

college_basic = tomeklinks(
    data = college, 
    y = "Grad.Rate"  
)

red_wine_basic = tomeklinks(
    data = red_wine,
    y = "quality"
)

# avocado_basic = tomeklinks(
#     data = avocado,
#     y = "AveragePrice"
# )

insurance_basic = tomeklinks(
    data = insurance,
    y = "charges"
)

housing_option = tomeklinks(
    data = housing, 
    y = "SalePrice", 
    option = "majority"
)

college_option = tomeklinks(
    data = college, 
    y = "Grad.Rate",  
    option = "minority"
)

red_wine_option = tomeklinks(
    data = red_wine,
    y = "quality",
    option = "both"
)

# avocado_option = tomeklinks(
#     data = avocado,
#     y = "AveragePrice",
#     option = "majority"
# )

insurance_option = tomeklinks(
    data = insurance,
    y = "charges",
    option = "both"
)

housing_thres = tomeklinks(
    data = housing, 
    y = "SalePrice", 
    rel_thres = 0.8
)

college_thres = tomeklinks(
    data = college, 
    y = "Grad.Rate",  
    rel_thres = 0.4
)

red_wine_thres = tomeklinks(
    data = red_wine,
    y = "quality",
    rel_thres = 0.6
)

# avocado_thres = tomeklinks(
#     data = avocado,
#     y = "AveragePrice",
#     rel_thres = 0.3
# )

insurance_thres = tomeklinks(
    data = insurance,
    y = "charges",
    rel_thres = 0.7
)

housing_combined = tomeklinks(
    data = housing, 
    y = "SalePrice",
    option = "minority",
    rel_thres = 0.8
)

college_combined = tomeklinks(
    data = college, 
    y = "Grad.Rate",
    option = "majority",
    rel_thres = 0.4
)

red_wine_combined = tomeklinks(
    data = red_wine,
    y = "quality",
    option = "minority",
    rel_thres = 0.6
)

# avocado_combined = tomeklinks(
#     data = avocado,
#     y = "AveragePrice",
#     option = "both",
#     rel_thres = 0.3
# )

insurance_combined = tomeklinks(
    data = insurance,
    y = "charges",
    option = "majority",
    rel_thres = 0.7
)



