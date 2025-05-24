import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

# Ruta base donde están las carpetas
base_path = "./Polipos_DeepLearning"

# Buscar todos los archivos .ipynb dentro de subcarpetas, omitiendo carpetas específicas
notebooks = []
for root, dirs, files in os.walk(base_path):
    # Excluir las carpetas .ipynb_checkpoints y cualquier carpeta que tenga "datos" en su nombre
    dirs[:] = [d for d in dirs if d != ".ipynb_checkpoints" and "datos" not in d.lower()]
    
    for file in files:
        if file.endswith(".ipynb"):  # Buscar cualquier archivo .ipynb
            notebooks.append(os.path.join(root, file))

# Ejecutar cada notebook sin límite de tiempo por celda
for notebook_path in notebooks:
    print(f"🟡 Ejecutando: {notebook_path}")
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
        ep = ExecutePreprocessor(timeout=-1, kernel_name='python3')

        try:
            ep.preprocess(nb, {'metadata': {'path': os.path.dirname(notebook_path)}})
            print(f"✔️ Ejecutado correctamente: {notebook_path}")
        except Exception as e:
            print(f"❌ Error ejecutando {notebook_path}:\n{e}")

        # Guardar el resultado con el mismo nombre de archivo
        output_path = notebook_path  # Guardar con el mismo nombre
        with open(output_path, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)

