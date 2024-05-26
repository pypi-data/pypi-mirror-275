# Test file for Random Over-sampling

import pandas
from ImbalancedLearningRegression import ro

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

housing_basic = ro(
    data = housing, 
    y = "SalePrice" 
)

college_basic = ro(
    data = college, 
    y = "Grad.Rate"  
)

red_wine_basic = ro(
    data = red_wine,
    y = "quality"
)

# avocado_basic = ro(
#     data = avocado,
#     y = "AveragePrice"
# )

insurance_basic = ro(
    data = insurance,
    y = "charges"
)

housing_extreme = ro(
    data = housing, 
    y = "SalePrice", 
    samp_method = "extreme"
)

college_extreme = ro(
    data = college, 
    y = "Grad.Rate",  
    samp_method = "extreme"
)

red_wine_extreme = ro(
    data = red_wine,
    y = "quality",
    samp_method = "extreme"
)

# avocado_extreme = ro(
#     data = avocado,
#     y = "AveragePrice",
#     samp_method = "extreme"
# )

insurance_extreme = ro(
    data = insurance,
    y = "charges",
    samp_method = "extreme"
)

housing_replace = ro(
    data = housing, 
    y = "SalePrice", 
    replace = False
)

college_replace = ro(
    data = college, 
    y = "Grad.Rate",  
    replace = False
)

red_wine_replace = ro(
    data = red_wine,
    y = "quality",
    replace = False
)

# avocado_replace = ro(
#     data = avocado,
#     y = "AveragePrice",
#     replace = False
# )

insurance_replace = ro(
    data = insurance,
    y = "charges",
    replace = False
)

housing_thres = ro(
    data = housing, 
    y = "SalePrice", 
    rel_thres = 0.8
)

college_thres = ro(
    data = college, 
    y = "Grad.Rate",  
    rel_thres = 0.4
)

red_wine_thres = ro(
    data = red_wine,
    y = "quality",
    rel_thres = 0.6
)

# avocado_thres = ro(
#     data = avocado,
#     y = "AveragePrice",
#     rel_thres = 0.3
# )

insurance_thres = ro(
    data = insurance,
    y = "charges",
    rel_thres = 0.7
)

housing_combined = ro(
    data = housing, 
    y = "SalePrice",
    samp_method = "extreme", 
    replace = False,
    rel_thres = 0.8
)

college_combined = ro(
    data = college, 
    y = "Grad.Rate",
    samp_method = "extreme", 
    replace = False,  
    rel_thres = 0.4
)

red_wine_combined = ro(
    data = red_wine,
    y = "quality",
    samp_method = "extreme", 
    replace = False,
    rel_thres = 0.6
)

# avocado_combined = ro(
#     data = avocado,
#     y = "AveragePrice",
#     samp_method = "extreme", 
#     replace = False,
#     rel_thres = 0.3
# )

insurance_combined = ro(
    data = insurance,
    y = "charges",
    samp_method = "extreme", 
    replace = False,
    rel_thres = 0.7
)



