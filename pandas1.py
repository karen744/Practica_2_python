import pandas as pd
import sys

def print_python_version():
    #Print the version of Python that this
    print(sys.version)

data  = {
    'Nombres' : ['Juan', 'Maria', 'Carlos'],
    'Edad' : [20, 22, 23 ],
    'Ciudad' : ['Madrid','Barcelona','Valencia']

}

df = pd.DataFrame(data)
df.head
df.dtypes #tipo de datos
df['Nombres']
df['Edad'].plot.hist()
print_python_version()

