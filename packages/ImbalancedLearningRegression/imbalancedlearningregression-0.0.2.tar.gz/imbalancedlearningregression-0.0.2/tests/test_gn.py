# Test file for Gaussian Noise

import pandas
from ImbalancedLearningRegression import gn

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

housing_basic = gn(
    data = housing, 
    y = "SalePrice" 
)

college_basic = gn(
    data = college, 
    y = "Grad.Rate"  
)

red_wine_basic = gn(
    data = red_wine,
    y = "quality"
)

# avocado_basic = gn(
#     data = avocado,
#     y = "AveragePrice"
# )

insurance_basic = gn(
    data = insurance,
    y = "charges"
)

housing_extreme = gn(
    data = housing, 
    y = "SalePrice", 
    samp_method = "extreme"
)

college_extreme = gn(
    data = college, 
    y = "Grad.Rate",  
    samp_method = "extreme"
)

red_wine_extreme = gn(
    data = red_wine,
    y = "quality",
    samp_method = "extreme"
)

# avocado_extreme = gn(
#     data = avocado,
#     y = "AveragePrice",
#     samp_method = "extreme"
# )

insurance_extreme = gn(
    data = insurance,
    y = "charges",
    samp_method = "extreme"
)

housing_replace = gn(
    data = housing, 
    y = "SalePrice", 
    replace = True
)

college_replace = gn(
    data = college, 
    y = "Grad.Rate",  
    replace = True
)

red_wine_replace = gn(
    data = red_wine,
    y = "quality",
    replace = True
)

# avocado_replace = gn(
#     data = avocado,
#     y = "AveragePrice",
#     replace = True
# )

insurance_replace = gn(
    data = insurance,
    y = "charges",
    replace = True
)

housing_thres = gn(
    data = housing, 
    y = "SalePrice", 
    rel_thres = 0.8
)

college_thres = gn(
    data = college, 
    y = "Grad.Rate",  
    rel_thres = 0.4
)

red_wine_thres = gn(
    data = red_wine,
    y = "quality",
    rel_thres = 0.6
)

# avocado_thres = gn(
#     data = avocado,
#     y = "AveragePrice",
#     rel_thres = 0.3
# )

insurance_thres = gn(
    data = insurance,
    y = "charges",
    rel_thres = 0.7
)

housing_pert = gn(
    data = housing, 
    y = "SalePrice", 
    pert = 0.1
)

college_pert = gn(
    data = college, 
    y = "Grad.Rate",  
    pert = 0.05
)

red_wine_pert = gn(
    data = red_wine,
    y = "quality",
    pert = 0.15
)

# avocado_pert = gn(
#     data = avocado,
#     y = "AveragePrice",
#     pert = 0.2
# )

insurance_pert = gn(
    data = insurance,
    y = "charges",
    pert = 0.08
)

housing_perc = gn(
    data = housing, 
    y = "SalePrice", 
    manual_perc = True,
    perc_u = 0.5,
    perc_o = 1.2
)

college_perc = gn(
    data = college, 
    y = "Grad.Rate",  
    manual_perc = True,
    perc_u = 0.7,
    perc_o = 0.8
)

red_wine_perc = gn(
    data = red_wine,
    y = "quality",
    manual_perc = True,
    perc_u = 0.2,
    perc_o = 3
)

# avocado_perc = gn(
#     data = avocado,
#     y = "AveragePrice",
#     manual_perc = True,
#     perc_u = 0.9,
#     perc_o = 2.8
# )

insurance_perc = gn(
    data = insurance,
    y = "charges",
    manual_perc = True,
    perc_u = 0.4,
    perc_o = 4.3
)

housing_combined = gn(
    data = housing, 
    y = "SalePrice",
    samp_method = "extreme", 
    replace = True,
    rel_thres = 0.8,
    pert = 0.1
)

college_combined = gn(
    data = college, 
    y = "Grad.Rate",
    samp_method = "extreme", 
    replace = True,  
    rel_thres = 0.4,
    pert = 0.05
)

red_wine_combined = gn(
    data = red_wine,
    y = "quality",
    samp_method = "extreme", 
    replace = True,
    rel_thres = 0.6,
    pert = 0.15
)

# avocado_combined = gn(
#     data = avocado,
#     y = "AveragePrice",
#     samp_method = "extreme", 
#     replace = True,
#     rel_thres = 0.3,
#     pert = 0.2
# )

insurance_combined = gn(
    data = insurance,
    y = "charges",
    samp_method = "extreme", 
    replace = True,
    rel_thres = 0.7,
    pert = 0.08
)



