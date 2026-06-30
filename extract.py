#%%

import os
import zipfile
from rich.progress import track
import argparse

DATA_PATH = './data'

class ExtractFromZip:
    
    def __init__(self):
        pass

    def extract_zip(self, zip_file_path, extract_to):
        if not os.path.exists(zip_file_path):
            raise FileExistsError(f'The zip file {zip_file_path} does not exist.')
        
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)

    def extract_year(self, year):
        folder = os.path.join(DATA_PATH, str(year))

        files = [i for i in os.listdir(folder) if i.endswith('.zip')]
        for file in files:

            extract_to = os.path.join(folder, file.replace('.zip', ''))
            zip_file_path = os.path.join(folder, file)
            self.extract_zip(zip_file_path, extract_to)

        print(f'Arquivos do ano {year} extraídos com sucesso!')

    def extract_years(self, years):
        for year in track(years, description="Descompactando arquivos zip..."):
            self.extract_year(year)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Baixando dados do TSE')
    parser.add_argument('--inicio', '-i', type=int, help='Ano inicial a ser baixado')
    parser.add_argument('--fim', '-f', type=int, help='Ano final a ser baixado')
    parser.add_argument('--intervalo', type=int, default= 2, help='Intervalo entre os anos a serem baixados')
    args = parser.parse_args()

    extractor = ExtractFromZip()
    extractor.extract_years(range(args.inicio, args.fim + 1, args.intervalo))

# %%

# extractor = ExtractFromZip()
# extractor.extract_years(range(2000, 2025, 2))