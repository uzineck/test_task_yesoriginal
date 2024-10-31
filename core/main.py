from core.utils import Utils
from entrypoint import task_in_dict
from excel import create_excel

if __name__ == '__main__':
    Utils().write_to_file_json(file_to_write=task_in_dict, name_of_file="result")
    create_excel(result=task_in_dict)
