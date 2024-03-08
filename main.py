from funkcion import operation_limit
from funkcion import operation_sort
from funkcion import print_operation
from funkcion import open_json


def main():
    operation = operation_limit(5, open_json())
    operation_data_sort = operation_sort(operation)
    print_operation(operation_data_sort)

    # print_operation(operation_limit_sort(5))


if __name__ == '__main__':
    main()
