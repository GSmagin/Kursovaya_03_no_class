from funkcion import operation
from funkcion import operation_sort
from funkcion import print_operation
from funkcion import open_json


def main():
    operation_data = operation(open_json())
    operation_data_sort = operation_sort(operation_data)
    print_operation(operation_data_sort)

    # print_operation(operation_limit_sort(5))


if __name__ == '__main__':
    main()
