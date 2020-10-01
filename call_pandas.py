import pandas as pd
from opendp.whitenoise.sql import PandasReader, PrivateReader
from opendp.whitenoise.metadata import CollectionMetadata

pums = pd.read_csv('PUMS.csv')
meta = CollectionMetadata.from_file('PUMS.yaml')

query = 'SELECT married, AVG(income) AS income, COUNT(*) AS n FROM PUMS.PUMS GROUP BY married'

reader = PandasReader(meta, pums)
private_reader = PrivateReader(meta, reader)

result = private_reader.execute_typed(query)
print(result)