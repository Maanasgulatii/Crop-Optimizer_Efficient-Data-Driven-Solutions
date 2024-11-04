 #Temperature, Humidity, Rainfall, Soil pH, Nitrogen Content, Phosphorus Content, Potassium Content
new_conditions_1 = [85, 35, 120, 6.8, 65.0, 30.0, 100.0]  # All 7 features
recommended_crop_1 = predict_crop(new_conditions_1)
print(f"The recommended crop for all 7 features is: {recommended_crop_1}")


new_conditions_2 = [75, 45, 110, 6.5, 60.0]  # 5 features
recommended_crop_2 = predict_crop(new_conditions_2)
print(f"The recommended crop for 5 features (Temperature, Humidity, Rainfall, Soil pH, Nitrogen Content) is: {recommended_crop_2}")


new_conditions_3 = [90, 50, 100, 6.0]  # 4 features
recommended_crop_3 = predict_crop(new_conditions_3)
print(f"The recommended crop for 4 features (Temperature, Humidity, Rainfall, Soil pH) is: {recommended_crop_3}")


new_conditions_4 = [60, 30, 80]  # 3 features
recommended_crop_4 = predict_crop(new_conditions_4)
print(f"The recommended crop for 3 features (Temperature, Humidity, Rainfall) is: {recommended_crop_4}")


new_conditions_5 = [50, 20]  # 2 features
recommended_crop_5 = predict_crop(new_conditions_5)
print(f"The recommended crop for 2 features (Temperature, Humidity) is: {recommended_crop_5}")

