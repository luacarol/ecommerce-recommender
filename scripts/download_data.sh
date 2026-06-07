#!/bin/bash
# Download RetailRocket dataset from Kaggle
# Prerequisite: pip install kaggle && configure ~/.kaggle/kaggle.json

set -e

DATA_DIR="data/raw"

echo "Baixando dataset RetailRocket do Kaggle..."
kaggle datasets download -d retailrocket/ecommerce-dataset -p "$DATA_DIR" --unzip

echo ""
echo "Download concluído. Arquivos em $DATA_DIR:"
ls -lh "$DATA_DIR"/*.csv
