# Менеджер операций
Класс OperationsManager представляет собой компонент для обработки операций клиентов банка. Он позволяет фильтровать, сортировать и отображать последние выполненные операции.

# Методы
## filtering_completed_operations()
Метод filtering_completed_operations() фильтрует список всех операций и возвращает только выполненные операции (со статусом "EXECUTED").

## sorted_last_five_operations()
Метод sorted_last_five_operations() сортирует выполненные операции по дате в обратном порядке и возвращает пять наиболее последних операций.

## reformat_date(date)
Статический метод reformat_date(date) преобразует дату из формата "YYYY-MM-DDTHH:MM:SS" в формат "DD.MM.YYYY".

## hide_order(order)
Статический метод hide_order(order) скрывает конфиденциальную информацию, заменяя часть номера карты или счета на символы "*". Номер карты замаскирован в формате "XXXX XX** **** XXXX", где видны первые 6 цифр и последние 4 цифры, разделенные пробелами. Номер счета замаскирован в формате "**XXXX", где видны только последние 4 цифры.

## check_from_operation(operation)
Метод check_from_operation(operation) форматирует информацию об операции, включая номера карты и счета, с помощью метода hide_order(). Возвращает отформатированную строку в формате "<откуда> -> <куда>".

## show_last_operation()
Метод show_last_operation() выводит на экран последние пять выполненных операций клиента в заданном формате.

# Класс DataManager
Класс DataManager предоставляет методы для работы с данными.

## read_from_json(path)
Статический метод read_from_json(path) считывает данные из файла в формате JSON и возвращает их. Принимает путь к файлу в качестве параметра.

