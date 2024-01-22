import sys


def loading_scrap(i, max_value):
    progress = i / max_value
    bar_length = 40
    progress_bar = "#" * int(bar_length * progress)
    spaces = " " * (bar_length - len(progress_bar))

    sys.stdout.write(f"\r[{progress_bar}{spaces}] {int(progress * 100)}%")
    sys.stdout.flush()


from datetime import datetime


def format_date(date):
    date_formats = ["%Y-%m-%d", "%d-%m-%Y", "%Y/%m/%d", "%d/%m/%Y"]

    date_formated = None

    for date_format in date_formats:
        try:
            date_formated = datetime.strptime(date, date_format)
            break
        except:
            pass

    return date_formated
