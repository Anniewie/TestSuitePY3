import os
import datetime


def createDirIfNotExist(path):

    if not os.path.exists(path):
        os.mkdir(path)
        print('the folder {0} is already existed'.format(path))

def init_folder_at_beginning(date):
    html_folder_path = './../report/html/'
    new_html_folder_path = './../report/html/' + date
    png_folder_path = './../report/png/'
    log_folder_path = './../report/log/'
    new_log_folder_path = './../report/log/' + date

    createDirIfNotExist(html_folder_path)
    createDirIfNotExist(new_html_folder_path)
    createDirIfNotExist(png_folder_path)
    createDirIfNotExist(log_folder_path)
    createDirIfNotExist(new_log_folder_path)

if __name__ == '__main__':
    date_time = datetime.datetime.now()
    date = date_time.strftime('%Y-%m-%d')
    init_folder_at_beginning(date)

