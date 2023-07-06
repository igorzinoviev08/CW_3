from settings import PATH_OPERATION_JSON
from app.models.data import Data
from app.models.operation import Operation

if __name__ == '__main__':
    all_operations = Data.read_from_json(PATH_OPERATION_JSON)
    last_five_operation = Operation(all_operations)
    last_five_operation.show_last_operation()
