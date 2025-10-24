import logging
import os
from datetime import datetime

Log_file=f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

Log_path=os.path.join(os.getcwd(),"Logs") 

os.makedirs(Log_path,exist_ok=True)

LOG_FILEPATH=os.path.join(Log_path,Log_file)

logging.basicConfig(level=logging.INFO,
                    filename=LOG_FILEPATH,
                    format="[%(asctime)s] %(name)s:%(lineno)d - %(levelname)s - %(message)s"
)