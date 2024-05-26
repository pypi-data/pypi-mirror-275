# Test file for Condensed Nearest Neighbor

import pandas
from sklearn.neighbors import KNeighborsClassifier
from ImbalancedLearningRegression import cnn

## user-defined estimator
customized_estimator = KNeighborsClassifier(n_neighbors = 7, leaf_size = 60, metric = "hamming", n_jobs = 2)

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

housing_basic = cnn(
    data = housing, 
    y = "SalePrice" 
)

college_basic = cnn(
    data = college, 
    y = "Grad.Rate"  
)

red_wine_basic = cnn(
    data = red_wine,
    y = "quality"
)

# avocado_basic = cnn(
#     data = avocado,
#     y = "AveragePrice"
# )

insurance_basic = cnn(
    data = insurance,
    y = "charges"
)

housing_extreme = cnn(
    data = housing, 
    y = "SalePrice", 
    samp_method = "extreme"
)

college_extreme = cnn(
    data = college, 
    y = "Grad.Rate",  
    samp_method = "extreme"
)

red_wine_extreme = cnn(
    data = red_wine,
    y = "quality",
    samp_method = "extreme"
)

# avocado_extreme = cnn(
#     data = avocado,
#     y = "AveragePrice",
#     samp_method = "extreme"
# )

insurance_extreme = cnn(
    data = insurance,
    y = "charges",
    samp_method = "extreme"
)

housing_n_seed = cnn(
    data = housing, 
    y = "SalePrice", 
    n_seed = 2
)

college_n_seed = cnn(
    data = college, 
    y = "Grad.Rate",  
    n_seed = 3
)

red_wine_n_seed = cnn(
    data = red_wine,
    y = "quality",
    n_seed = 4
)

# avocado_n_seed = cnn(
#     data = avocado,
#     y = "AveragePrice",
#     n_seed = 5
# )

insurance_n_seed = cnn(
    data = insurance,
    y = "charges",
    n_seed = 6
)

housing_thres = cnn(
    data = housing, 
    y = "SalePrice", 
    rel_thres = 0.8
)

college_thres = cnn(
    data = college, 
    y = "Grad.Rate",  
    rel_thres = 0.4
)

red_wine_thres = cnn(
    data = red_wine,
    y = "quality",
    rel_thres = 0.6
)

# avocado_thres = cnn(
#     data = avocado,
#     y = "AveragePrice",
#     rel_thres = 0.3
# )

insurance_thres = cnn(
    data = insurance,
    y = "charges",
    rel_thres = 0.7
)

housing_k = cnn(
    data = housing, 
    y = "SalePrice", 
    k = 6
)

college_k = cnn(
    data = college, 
    y = "Grad.Rate",  
    k = 5
)

red_wine_k = cnn(
    data = red_wine,
    y = "quality",
    k = 4
)

# avocado_k = cnn(
#     data = avocado,
#     y = "AveragePrice",
#     k = 3
# )

insurance_k = cnn(
    data = insurance,
    y = "charges",
    k = 2
)

housing_k_neighbors_classifier = cnn(
    data = housing, 
    y = "SalePrice", 
    k_neighbors_classifier = customized_estimator
)

college_k_neighbors_classifier = cnn(
    data = college, 
    y = "Grad.Rate",  
    k_neighbors_classifier = customized_estimator
)

red_wine_k_neighbors_classifier = cnn(
    data = red_wine,
    y = "quality",
    k_neighbors_classifier = customized_estimator
)

# avocado_k_neighbors_classifier = cnn(
#     data = avocado,
#     y = "AveragePrice",
#     k_neighbors_classifier = customized_estimator
# )

insurance_k_neighbors_classifier = cnn(
    data = insurance,
    y = "charges",
    k_neighbors_classifier = customized_estimator
)

housing_combined = cnn(
    data = housing, 
    y = "SalePrice",
    samp_method = "extreme", 
    n_seed = 2,
    rel_thres = 0.8,
    k = 6
)

college_combined = cnn(
    data = college, 
    y = "Grad.Rate",
    samp_method = "extreme", 
    n_seed = 3,
    rel_thres = 0.4,
    k = 5
)

red_wine_combined = cnn(
    data = red_wine,
    y = "quality",
    samp_method = "extreme", 
    n_seed = 4,
    rel_thres = 0.6,
    k = 4
)

# avocado_combined = cnn(
#     data = avocado,
#     y = "AveragePrice",
#     samp_method = "extreme", 
#     n_seed = 5,
#     rel_thres = 0.3,
#     k = 3
# )

insurance_combined = cnn(
    data = insurance,
    y = "charges",
    samp_method = "extreme", 
    n_seed = 6,
    rel_thres = 0.7,
    k = 2
)



