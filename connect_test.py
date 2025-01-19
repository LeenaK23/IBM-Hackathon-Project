import ibm_db
from datetime import datetime

dsn = (
    "DATABASE=bludb;"
    "HOSTNAME=0c77d6f2-5da9-48a9-81f8-86b520b87518.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;"
    "PORT=31198;"
    "PROTOCOL=TCPIP;"
    "UID=qsj67798;"
    "PWD=LKc0qT2omrUoA6qm;"
    "SECURITY=SSL"
)

try:
    print("Attempting to connect...")
    conn = ibm_db.connect(dsn, "", "")
    if conn:
        print("Connection successful!")
        while True:
            print(datetime.now())
    else:
        print("Connection failed!")
except Exception as e:
    print(f"Error: {e}")
