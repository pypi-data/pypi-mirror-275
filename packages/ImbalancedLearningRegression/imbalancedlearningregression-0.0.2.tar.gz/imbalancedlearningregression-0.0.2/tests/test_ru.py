# Test file for Random Under-sampling

import pandas
from ImbalancedLearningRegression import random_under

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

housing_basic = random_under(
    data = housing, 
    y = "SalePrice" 
)

college_basic = random_under(
    data = college, 
    y = "Grad.Rate"  
)

red_wine_basic = random_under(
    data = red_wine,
    y = "quality"
)

# avocado_basic = random_under(
#     data = avocado,
#     y = "AveragePrice"
# )

insurance_basic = random_under(
    data = insurance,
    y = "charges"
)

housing_extreme = random_under(
    data = housing, 
    y = "SalePrice", 
    samp_method = "extreme"
)

college_extreme = random_under(
    data = college, 
    y = "Grad.Rate",  
    samp_method = "extreme"
)

red_wine_extreme = random_under(
    data = red_wine,
    y = "quality",
    samp_method = "extreme"
)

# avocado_extreme = random_under(
#     data = avocado,
#     y = "AveragePrice",
#     samp_method = "extreme"
# )

insurance_extreme = random_under(
    data = insurance,
    y = "charges",
    samp_method = "extreme"
)

housing_replace = random_under(
    data = housing, 
    y = "SalePrice", 
    replacement = False
)

college_replace = random_under(
    data = college, 
    y = "Grad.Rate",  
    replacement = False
)

red_wine_replace = random_under(
    data = red_wine,
    y = "quality",
    replacement = False
)

# avocado_replace = random_under(
#     data = avocado,
#     y = "AveragePrice",
#     replacement = False
# )

insurance_replace = random_under(
    data = insurance,
    y = "charges",
    replacement = False
)

housing_thres = random_under(
    data = housing, 
    y = "SalePrice", 
    rel_thres = 0.8
)

college_thres = random_under(
    data = college, 
    y = "Grad.Rate",  
    rel_thres = 0.4
)

red_wine_thres = random_under(
    data = red_wine,
    y = "quality",
    rel_thres = 0.6
)

# avocado_thres = random_under(
#     data = avocado,
#     y = "AveragePrice",
#     rel_thres = 0.3
# )

insurance_thres = random_under(
    data = insurance,
    y = "charges",
    rel_thres = 0.7
)

housing_combined = random_under(
    data = housing, 
    y = "SalePrice",
    samp_method = "extreme", 
    replacement = False,
    rel_thres = 0.8
)

college_combined = random_under(
    data = college, 
    y = "Grad.Rate",
    samp_method = "extreme", 
    replacement = False,  
    rel_thres = 0.4
)

red_wine_combined = random_under(
    data = red_wine,
    y = "quality",
    samp_method = "extreme", 
    replacement = False,
    rel_thres = 0.6
)

# avocado_combined = random_under(
#     data = avocado,
#     y = "AveragePrice",
#     samp_method = "extreme", 
#     replace = False,
#     rel_thres = 0.3
# )

insurance_combined = random_under(
    data = insurance,
    y = "charges",
    samp_method = "extreme", 
    replacement = False,
    rel_thres = 0.7
)



