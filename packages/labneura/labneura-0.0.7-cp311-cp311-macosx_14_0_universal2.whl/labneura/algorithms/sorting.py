import algocpp
class Sorting:
    def __init__(self, data) -> None:
        self.data = data
        self.size = len(self.data)
        self.cpp_sorting = algocpp.Sorting(self.data)

    def selection_cpp(self):
        self.cpp_sorting.selection()
        self.data = self.cpp_sorting.data

    def selection(self):
        """
        (n-1)*(n-2)*...1 = n(n-1)/2 = O(n^2)
        Irrespective of the input.
        Max no of swaps n-1 -> Max element at first and remaining all are sorted.
        Min no of swaps 0 -> Already sorted.
        """
        n_swaps = 0
        n_time_units = 0
        for i in range(self.size-1):
            minIdx = i
            for j in range(i+1,self.size):
                if self.data[minIdx] > self.data[j]:
                    minIdx = j
                n_time_units += 1
            if minIdx != i:
                n_swaps += 1
                (self.data[minIdx],self.data[i]) = (self.data[i],self.data[minIdx])
        print(f"{n_swaps=}")
        print(f"{n_time_units=}")

    def bubble_cpp(self):
        self.cpp_sorting.bubble()
        self.data = self.cpp_sorting.data

    def bubble_sort(self):
        """
        (n-1)+(n-2)+....1 = n(n-1)/2 = O(n^2)
        Sorted list -> (n-1) = O(n) = 0 Swaps
        Worst Case -> Descending Order -> O(n^2) = (n-1)+(n-2)+..+1 = n(n-1)/2 Swaps
        """
        n_swaps = 0
        n_time_units = 0
        for i in range(self.size-1):
            swapped = False
            for j in range(self.size-i-1):
                if self.data[j]>self.data[j+1]:
                    (self.data[j],self.data[j+1]) = (self.data[j+1],self.data[j])
                    swapped = True
                    n_swaps += 1
                n_time_units += 1
            if not swapped:
                break
        print(f"{n_swaps=}")
        print(f"{n_time_units=}")

    def insertion_cpp(self):
        self.cpp_sorting.insertion()
        self.data = self.cpp_sorting.data

    def insertion(self):
        """
        1 + 2 + .. + (n-1) = n(n-1)/2
        Sorted List -> n = 0 insertions
        Descending List -> (n(n-1)/2) no of insertions
        """
        n_insertions = 0
        n_time_units = 0
        for i in range(1,self.size):
            mini = self.data[i]
            j = i-1
            while (j>=0 and self.data[j]>mini):
                self.data[j+1] = self.data[j]
                j = j-1
                n_insertions += 1
                n_time_units += 1
            self.data[j+1] = mini
        print(f"{n_insertions=}")
        print(f"{n_time_units=}")

    def merge_cpp(self):
        self.cpp_sorting.merge_sort()
        self.data = self.cpp_sorting.data

    def merge(self):
        self.no_recursive_calls = 0
        self.n_time_units = 0
        self.list_space = []
        self.merge_sort(self.data)
        print(f"{self.no_recursive_calls=}")
        print(f"{self.n_time_units}")
        print(f"{self.list_space=}")

    def merge_sort(self, arr):
        """
        Stack trace -> logn -> memory
        Each stack -> n1+n2 -> extra memory (left, and right)
        Time -> nlogn
        """
        self.no_recursive_calls += 1
        if len(arr) == 1:
            self.list_space.append("reverse")
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]
            self.list_space.append(len(arr))
            self.merge_sort(left)
            self.merge_sort(right)

            i = j = k = 0

            while i<len(left) and j<len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i+=1
                    k+=1
                else:
                    arr[k] = right[j]
                    j+=1
                    k+=1
                self.n_time_units += 1
            while i<len(left):
                arr[k] = left[i]
                i+=1
                k+=1
                self.n_time_units += 1
            while j<len(right):
                arr[k] = right[j]
                j+=1
                k+=1
                self.n_time_units += 1

    def quick_cpp(self):
        self.cpp_sorting.quick_sort()
        self.data = self.cpp_sorting.data

    def quick(self):
        self.n_time_units = 0
        self.list_space = []
        self.quick_sort(self.data, 0, len(self.data)-1)
        print(f"{self.n_time_units=}")

    def quick_sort(self, arr, lower, upper):
        if lower < upper:
            pi = self.partition(arr, lower, upper)
            self.quick_sort(arr, lower, pi-1)
            self.quick_sort(arr, pi+1, upper)
        
    def partition(self, arr, lower, upper):
        pivot = arr[upper]
        i = lower-1
        for j in range(lower,upper):
            self.n_time_units += 1
            if arr[j]<pivot:
                i+=1
                if i!=j:
                    (arr[i],arr[j]) = (arr[j], arr[i]) 
        (arr[i+1],arr[upper]) = (arr[upper], arr[i+1])
        return i+1