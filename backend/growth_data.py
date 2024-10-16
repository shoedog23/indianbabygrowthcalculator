# Simplified growth data for demonstration
# In a real scenario, you'd have more comprehensive data
WEIGHT_DATA = {
    'male': {
        0: [2.5, 3.3, 4.0],  # 3rd, 50th, 97th percentiles at 0 months
        12: [8.0, 10.0, 12.0],  # 3rd, 50th, 97th percentiles at 12 months
        24: [10.0, 12.5, 15.0],  # 3rd, 50th, 97th percentiles at 24 months
    },
    'female': {
        0: [2.4, 3.2, 3.9],
        12: [7.5, 9.5, 11.5],
        24: [9.5, 12.0, 14.5],
    }
}

HEIGHT_DATA = {
    'male': {
        0: [46.0, 50.0, 54.0],
        12: [71.0, 75.0, 79.0],
        24: [82.0, 87.0, 92.0],
    },
    'female': {
        0: [45.5, 49.5, 53.5],
        12: [70.0, 74.0, 78.0],
        24: [81.0, 86.0, 91.0],
    }
}