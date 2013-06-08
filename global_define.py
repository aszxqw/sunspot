import datetime
TODAY = datetime.date.today()
YESTD = TODAY - datetime.timedelta(1)

CONFIG_FILE_NAME = "sunspot.conf"

options = {
    "pickle_dir": "./pickles",
    "verbose": False,
    "date": TODAY,
}
