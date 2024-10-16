from growth_data import WEIGHT_DATA, HEIGHT_DATA

def calculate_percentile(value, data_points):
    if value <= data_points[0]:
        return 3
    elif value >= data_points[2]:
        return 97
    elif value <= data_points[1]:
        return 3 + (value - data_points[0]) / (data_points[1] - data_points[0]) * 47
    else:
        return 50 + (value - data_points[1]) / (data_points[2] - data_points[1]) * 47

def get_growth_percentiles(age, weight, height, gender):
    age = min(24, max(0, age))  # Clamp age between 0 and 24 months
    
    weight_data = WEIGHT_DATA[gender]
    height_data = HEIGHT_DATA[gender]
    
    # Simple linear interpolation between known data points
    if age in weight_data:
        weight_percentile = calculate_percentile(weight, weight_data[age])
        height_percentile = calculate_percentile(height, height_data[age])
    else:
        lower_age = max(key for key in weight_data.keys() if key <= age)
        upper_age = min(key for key in weight_data.keys() if key >= age)
        
        weight_lower = calculate_percentile(weight, weight_data[lower_age])
        weight_upper = calculate_percentile(weight, weight_data[upper_age])
        weight_percentile = weight_lower + (weight_upper - weight_lower) * (age - lower_age) / (upper_age - lower_age)
        
        height_lower = calculate_percentile(height, height_data[lower_age])
        height_upper = calculate_percentile(height, height_data[upper_age])
        height_percentile = height_lower + (height_upper - height_lower) * (age - lower_age) / (upper_age - lower_age)
    
    return round(weight_percentile, 1), round(height_percentile, 1)