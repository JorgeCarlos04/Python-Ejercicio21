#  Matriz de confusión(variables)
TP = 45
TN = 20
FP = 50
FN = 32

# Medida de evaluacion para la Matriz
rentabilidad = (TP + TN) / (TP + TN + FP + FN) 
precision = TP / (TP + FP)
llamada  = TP / (TP + FN) 
F1M = 2 * (precision * llamada) / (precision + llamada)


print(f"Accuracy: {rentabilidad}")
print(f"Precision: {precision}")
print(f"Llamada:{llamada}")
print(f"F1-Measure: {F1M}")
