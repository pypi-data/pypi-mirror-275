# Test file for ADASYN

import pandas
from ImbalancedLearningRegression import adasyn

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

housing_basic = adasyn(
    data = housing, 
    y = "SalePrice" 
)

college_basic = adasyn(
    data = college, 
    y = "Grad.Rate"  
)

red_wine_basic = adasyn(
    data = red_wine,
    y = "quality"
)

# avocado_basic = adasyn(
#     data = avocado,
#     y = "AveragePrice"
# )

insurance_basic = adasyn(
    data = insurance,
    y = "charges"
)

housing_extreme = adasyn(
    data = housing, 
    y = "SalePrice", 
    samp_method = "extreme"
)

college_extreme = adasyn(
    data = college, 
    y = "Grad.Rate",  
    samp_method = "extreme"
)

red_wine_extreme = adasyn(
    data = red_wine,
    y = "quality",
    samp_method = "extreme"
)

# avocado_extreme = adasyn(
#     data = avocado,
#     y = "AveragePrice",
#     samp_method = "extreme"
# )

insurance_extreme = adasyn(
    data = insurance,
    y = "charges",
    samp_method = "extreme"
)

housing_thres = adasyn(
    data = housing, 
    y = "SalePrice", 
    rel_thres = 0.8
)

college_thres = adasyn(
    data = college, 
    y = "Grad.Rate",  
    rel_thres = 0.4
)

red_wine_thres = adasyn(
    data = red_wine,
    y = "quality",
    rel_thres = 0.6
)

# avocado_thres = adasyn(
#     data = avocado,
#     y = "AveragePrice",
#     rel_thres = 0.3
# )

insurance_thres = adasyn(
    data = insurance,
    y = "charges",
    rel_thres = 0.7
)

housing_k = adasyn(
    data = housing, 
    y = "SalePrice", 
    k = 6
)

college_k = adasyn(
    data = college, 
    y = "Grad.Rate",  
    k = 5
)

red_wine_k = adasyn(
    data = red_wine,
    y = "quality",
    k = 4
)

# avocado_k = adasyn(
#     data = avocado,
#     y = "AveragePrice",
#     k = 3
# )

insurance_k = adasyn(
    data = insurance,
    y = "charges",
    k = 2
)

housing_combined = adasyn(
    data = housing, 
    y = "SalePrice",
    samp_method = "extreme", 
    rel_thres = 0.8,
    k = 6
)

college_combined = adasyn(
    data = college, 
    y = "Grad.Rate",
    samp_method = "extreme", 
    rel_thres = 0.4,
    k = 5
)

red_wine_combined = adasyn(
    data = red_wine,
    y = "quality",
    samp_method = "extreme", 
    rel_thres = 0.6,
    k = 4
)

# avocado_combined = adasyn(
#     data = avocado,
#     y = "AveragePrice",
#     samp_method = "extreme", 
#     rel_thres = 0.3,
#     k = 3
# )

insurance_combined = adasyn(
    data = insurance,
    y = "charges",
    samp_method = "extreme", 
    rel_thres = 0.7,
    k = 2
)



