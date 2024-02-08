#variance

# average of the squared differences between each data point and mean

# def variance(data):
#     n=len(data)
#     mean=sum(data)/n
    
#     squared_diff = sum((x-mean)**2 for x in data)
    
#     varience = squared_diff / n-1   # n for  population varience 
#                                     # n-1 for sample varience
#     return varience

# # using numpy
# np.var(data,ddof=1) -  sample varience
# np.var(data) - population varience

# std_deviation
# def cal_mean(x):
#     return sum(x)/len(x)

# def cal_var(xx):
#     mean=cal_mean(xx)
#     var=sum((x-mean)**2 for x in xx)/len(xx)-1
#     return var

# def cal_std(data):
#     var=cal_var(data)
#     std= var**0.5
#     return std
        
# # covarience
# def covarience(x,y):
#     n=len(x)
#     if n!= len(y):
#         return -1
#     mean_x = sum(x)/n
#     mean_y = sum(y)/n
    
#     sum_xy = sum((x[i]-mean_x)*(y[i]-mean_y) for i in range(n))
    
#     covarience = sum_xy/(n-1)
    
#     return covarience

# def correlation(x,y):
#     n=len(x)
    
#     mean_x=sum(x)/n
#     mean_y=sum(y)/n
    
#     covar=sum((x[i]-mean_x)*(y[i]-mean_y) for i in range(n)) / n-1
#     std_x = (sum((xi - mean_x)**2 for xi in x)/n-1)**0.5
#     std_y = (sum((yi-mean_y)**2 for yi in y)/n-1)**0.5
    
#     corr=covar/(std_x*std_y)
#     return corr

    
