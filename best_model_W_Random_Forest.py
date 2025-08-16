import pickle

# Ruta al archivo .pkl
filename = "best_model_W_Random_Forest.pkl"

# Cargar el modelo desde el archivo
with open(filename, "rb") as f:
    model = pickle.load(f)

# Mostrar el modelo cargado
print("✅ Modelo cargado correctamente:")
print(model)
