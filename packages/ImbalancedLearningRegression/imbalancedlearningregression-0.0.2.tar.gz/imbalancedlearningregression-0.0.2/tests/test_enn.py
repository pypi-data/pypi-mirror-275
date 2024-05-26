# Test file for Edited Nearest Neighbor

import pandas
from sklearn.neighbors import KNeighborsClassifier
from ImbalancedLearningRegression import enn

## user-defined estimator
customized_estimator = KNeighborsClassifier(n_neighbors = 5, leaf_size = 60, metric = "manhattan", n_jobs = 2)

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

housing_basic = enn(
    data = housing, 
    y = "SalePrice" 
)

college_basic = enn(
    data = college, 
    y = "Grad.Rate"  
)

red_wine_basic = enn(
    data = red_wine,
    y = "quality"
)

# avocado_basic = enn(
#     data = avocado,
#     y = "AveragePrice"
# )

insurance_basic = enn(
    data = insurance,
    y = "charges"
)

housing_extreme = enn(
    data = housing, 
    y = "SalePrice", 
    samp_method = "extreme"
)

college_extreme = enn(
    data = college, 
    y = "Grad.Rate",  
    samp_method = "extreme"
)

red_wine_extreme = enn(
    data = red_wine,
    y = "quality",
    samp_method = "extreme"
)

# avocado_extreme = enn(
#     data = avocado,
#     y = "AveragePrice",
#     samp_method = "extreme"
# )

insurance_extreme = enn(
    data = insurance,
    y = "charges",
    samp_method = "extreme"
)

housing_thres = enn(
    data = housing, 
    y = "SalePrice", 
    rel_thres = 0.8
)

college_thres = enn(
    data = college, 
    y = "Grad.Rate",  
    rel_thres = 0.4
)

red_wine_thres = enn(
    data = red_wine,
    y = "quality",
    rel_thres = 0.6
)

# avocado_thres = enn(
#     data = avocado,
#     y = "AveragePrice",
#     rel_thres = 0.3
# )

insurance_thres = enn(
    data = insurance,
    y = "charges",
    rel_thres = 0.7
)

housing_k = enn(
    data = housing, 
    y = "SalePrice", 
    k = 6
)

college_k = enn(
    data = college, 
    y = "Grad.Rate",  
    k = 5
)

red_wine_k = enn(
    data = red_wine,
    y = "quality",
    k = 4
)

# avocado_k = enn(
#     data = avocado,
#     y = "AveragePrice",
#     k = 3
# )

insurance_k = enn(
    data = insurance,
    y = "charges",
    k = 2
)

housing_k_neighbors_classifier = enn(
    data = housing, 
    y = "SalePrice", 
    k_neighbors_classifier = customized_estimator
)

college_k_neighbors_classifier = enn(
    data = college, 
    y = "Grad.Rate",  
    k_neighbors_classifier = customized_estimator
)

red_wine_k_neighbors_classifier = enn(
    data = red_wine,
    y = "quality",
    k_neighbors_classifier = customized_estimator
)

# avocado_k_neighbors_classifier = enn(
#     data = avocado,
#     y = "AveragePrice",
#     k_neighbors_classifier = customized_estimator
# )

insurance_k_neighbors_classifier = enn(
    data = insurance,
    y = "charges",
    k_neighbors_classifier = customized_estimator
)

housing_combined = enn(
    data = housing, 
    y = "SalePrice",
    samp_method = "extreme", 
    rel_thres = 0.8,
    k = 6
)

college_combined = enn(
    data = college, 
    y = "Grad.Rate",
    samp_method = "extreme", 
    rel_thres = 0.4,
    k = 5
)

red_wine_combined = enn(
    data = red_wine,
    y = "quality",
    samp_method = "extreme", 
    rel_thres = 0.6,
    k = 4
)

# avocado_combined = enn(
#     data = avocado,
#     y = "AveragePrice",
#     samp_method = "extreme", 
#     rel_thres = 0.3,
#     k = 3
# )

insurance_combined = enn(
    data = insurance,
    y = "charges",
    samp_method = "extreme", 
    rel_thres = 0.7,
    k = 2
)



