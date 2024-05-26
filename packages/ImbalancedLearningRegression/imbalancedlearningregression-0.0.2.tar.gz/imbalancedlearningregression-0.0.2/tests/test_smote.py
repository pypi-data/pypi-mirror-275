# Test file for SMOTE

import pandas
from ImbalancedLearningRegression import smote

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

housing_basic = smote(
    data = housing, 
    y = "SalePrice" 
)

college_basic = smote(
    data = college, 
    y = "Grad.Rate"  
)

red_wine_basic = smote(
    data = red_wine,
    y = "quality"
)

# avocado_basic = smote(
#     data = avocado,
#     y = "AveragePrice"
# )

insurance_basic = smote(
    data = insurance,
    y = "charges"
)

housing_extreme = smote(
    data = housing, 
    y = "SalePrice", 
    samp_method = "extreme"
)

college_extreme = smote(
    data = college, 
    y = "Grad.Rate",  
    samp_method = "extreme"
)

red_wine_extreme = smote(
    data = red_wine,
    y = "quality",
    samp_method = "extreme"
)

# avocado_extreme = smote(
#     data = avocado,
#     y = "AveragePrice",
#     samp_method = "extreme"
# )

insurance_extreme = smote(
    data = insurance,
    y = "charges",
    samp_method = "extreme"
)

housing_thres = smote(
    data = housing, 
    y = "SalePrice", 
    rel_thres = 0.8
)

college_thres = smote(
    data = college, 
    y = "Grad.Rate",  
    rel_thres = 0.4
)

red_wine_thres = smote(
    data = red_wine,
    y = "quality",
    rel_thres = 0.6
)

# avocado_thres = smote(
#     data = avocado,
#     y = "AveragePrice",
#     rel_thres = 0.3
# )

insurance_thres = smote(
    data = insurance,
    y = "charges",
    rel_thres = 0.7
)

housing_k = smote(
    data = housing, 
    y = "SalePrice", 
    k = 6
)

college_k = smote(
    data = college, 
    y = "Grad.Rate",  
    k = 5
)

red_wine_k = smote(
    data = red_wine,
    y = "quality",
    k = 4
)

# avocado_k = smote(
#     data = avocado,
#     y = "AveragePrice",
#     k = 3
# )

insurance_k = smote(
    data = insurance,
    y = "charges",
    k = 2
)

housing_combined = smote(
    data = housing, 
    y = "SalePrice",
    samp_method = "extreme", 
    rel_thres = 0.8,
    k = 6
)

college_combined = smote(
    data = college, 
    y = "Grad.Rate",
    samp_method = "extreme", 
    rel_thres = 0.4,
    k = 5
)

red_wine_combined = smote(
    data = red_wine,
    y = "quality",
    samp_method = "extreme", 
    rel_thres = 0.6,
    k = 4
)

# avocado_combined = smote(
#     data = avocado,
#     y = "AveragePrice",
#     samp_method = "extreme", 
#     rel_thres = 0.3,
#     k = 3
# )

insurance_combined = smote(
    data = insurance,
    y = "charges",
    samp_method = "extreme", 
    rel_thres = 0.7,
    k = 2
)



