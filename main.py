from settings import PATH_OPERATION_JSON
from app.models.data_manager import DataManager
from app.models.operations_manager import OperationsManager

if __name__ == '__main__':
    all_operations = DataManager.read_from_json(PATH_OPERATION_JSON)
    last_five_operation = OperationsManager(all_operations)
    last_five_operation.show_last_operation()
