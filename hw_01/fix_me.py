def calculate_average(numbers):
    """Возвращает среднее арифметическое чисел массива

    Args:
        numbers (list[int]): массив чисел

    Returns:
        float: среднее арифметическое

    Examples:
        >>> calculate_average([10, 15, 20])
        15.0

        >>> calculate_average([])
        0.0
    """

    total = sum(numbers)
    count = len(numbers)
    average = total / (count or 1)

    return average


nums = [10, 15, 20]
result = calculate_average(nums)

print("The average is:", result)
