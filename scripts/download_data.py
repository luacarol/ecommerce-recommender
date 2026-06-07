"""Download RetailRocket dataset from Kaggle (works on Mac, Linux, and Windows).

Prerequisite: pip install kaggle && configure ~/.kaggle/kaggle.json
"""

from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

print("Baixando dataset RetailRocket do Kaggle...")
api.dataset_download_files("retailrocket/ecommerce-dataset", path="data/raw", unzip=True)
print("Download concluído. Arquivos salvos em data/raw/")
