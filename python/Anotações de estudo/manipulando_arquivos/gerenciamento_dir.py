import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

#os.mkdir(ROOT_PATH / "novo-diretorio")

#arquivo = open(ROOT_PATH / "novo.txt", "w")
#arquivo.close()

#renomear 
#os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt")

#os.remove(ROOT_PATH / " alterado.txt")

#move para outra pasta
shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo-diretorio" / "novo.txt")