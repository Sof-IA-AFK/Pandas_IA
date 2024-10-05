import pandas as pd

datos = {'Nombre':['Hermione', 'Harry', 'Ron'],
          'Edad': [14, 13, 14],
          'Ciudad': ['Inglaterra','Estados Unidos', 'Londres']}

df = pd.DataFrame(datos)
print(df)