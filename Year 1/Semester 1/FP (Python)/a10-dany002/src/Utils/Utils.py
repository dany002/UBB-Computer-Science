

class Utils:

    @staticmethod
    def shellSort(iterable_that_is_going_to_be_sorted, order_function):
        # Rearrange elements at each n/2, n/4, n/8, ... intervals ( u always compare elements from a constant interval distance ( n/2, n/4,... 1 )
        # Shell Sort is a generalized Insertion Sort. Time Complexity: O(n*log(n))
        interval = len(iterable_that_is_going_to_be_sorted) // 2
        while interval > 0:
            for first_index in range(interval, len(iterable_that_is_going_to_be_sorted)):
                auxiliary = iterable_that_is_going_to_be_sorted[first_index]
                second_index = first_index
                while second_index >= interval and order_function(iterable_that_is_going_to_be_sorted[second_index - interval], auxiliary) == 1:
                    iterable_that_is_going_to_be_sorted[second_index] = iterable_that_is_going_to_be_sorted[second_index - interval]
                    second_index -= interval
                iterable_that_is_going_to_be_sorted[second_index] = auxiliary
            interval //= 2
        return iterable_that_is_going_to_be_sorted


    @staticmethod
    def filter(iterable_that_is_going_to_be_filtered, acceptance_function):
        list_that_contains_the_filtered_elements = []
        for index in range(len(iterable_that_is_going_to_be_filtered)):
            if acceptance_function(iterable_that_is_going_to_be_filtered[index]) == True:
                list_that_contains_the_filtered_elements.append(iterable_that_is_going_to_be_filtered[index])
        return list_that_contains_the_filtered_elements

