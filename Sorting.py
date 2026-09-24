import time
import random
import sys

# Increase recursion limit to handle deeper recursion for Quick Sort
sys.setrecursionlimit(10000)

# ==================== SORTING ALGORITHMS ====================

def bubble_sort(arr):
    """Bubble Sort - O(n²)"""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def merge_sort(arr):
    """Merge Sort - O(n log n)"""
    if len(arr) <= 1:
        return arr
    m = len(arr) // 2
    left = merge_sort(arr[:m])
    right = merge_sort(arr[m:])
    return linear_merge(left, right)


def linear_merge(A, B):
    """Helper function for merge sort"""
    output = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            output.append(A[i])
            i += 1
        else:
            output.append(B[j])
            j += 1
    output.extend(A[i:])
    output.extend(B[j:])
    return output


def quick_sort(arr):
    """Quick Sort with middle pivot - O(n log n) average"""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def quick_sort_ver_1(arr):
    
    """Quick Sort Version 1 - First element as pivot."""
    
    if len(arr) <= 1:
        return arr
    
    # For large lists, use iterative approach to avoid recursion depth issues
    if len(arr) > 2000:
        return quick_sort_ver_1_iterative(arr)
    
    pivot = arr[0]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort_ver_1(left) + middle + quick_sort_ver_1(right)


def quick_sort_ver_1_iterative(arr):
    """Iterative version of Quick Sort Ver 1 to avoid recursion depth issues"""
    if len(arr) <= 1:
        return arr
    
    stack = [(0, len(arr) - 1)]
    result = arr.copy()
    
    while stack:
        low, high = stack.pop()
        if low < high:
            # Use first element as pivot
            pivot = result[low]
            left = []
            middle = []
            right = []
            
            for x in result[low:high+1]:
                if x < pivot:
                    left.append(x)
                elif x == pivot:
                    middle.append(x)
                else:
                    right.append(x)
            
            # Rebuild the section
            new_section = left + middle + right
            result[low:high+1] = new_section
            
            # Push subproblems
            stack.append((low, low + len(left) - 1))
            stack.append((high - len(right) + 1, high))
    
    return result


def quick_sort_ver_2(arr):
    """Quick Sort Version 2 - Iterative with last element pivot (in-place)"""
    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pi = partition(low, high)
            stack.append((low, pi - 1))
            stack.append((pi + 1, high))
    return arr


# ==================== HELPER FUNCTIONS ====================

def generate_lists(size):
    """Generate random and sorted lists of given size"""
    random_list = [random.randint(1, 10000) for _ in range(size)]
    sorted_list = sorted(random_list)
    return random_list, sorted_list


def measure_time(sort_function, arr, returns_new_list=True):
    """
    Measure execution time in milliseconds.
    returns_new_list: True if function returns a new list (Quick Sort, Merge Sort)
                      False if sorts in-place (Bubble Sort, Quick Sort Ver 2)
    """
    try:
        start = time.perf_counter()
        if returns_new_list:
            result = sort_function(arr.copy())
        else:
            sort_function(arr)
        end = time.perf_counter()
        return (end - start) * 1000  # Convert to milliseconds
    except RecursionError:
        # Return a very large number to indicate failure
        return float('inf')


# ==================== BENCHMARKING ====================

def run_benchmarks(runs=3):
    """Run benchmarks for all sorting algorithms"""
    sizes = [1, 2, 3, 4, 5, 10, 100, 1000, 3000, 5000, 10000]
    
    # Store results in dictionaries
    results = {
        'bubble_random': [],
        'bubble_sorted': [],
        'merge_random': [],
        'merge_sorted': [],
        'quick_random': [],
        'quick_sorted': [],
        'quick_v1_random': [],
        'quick_v1_sorted': [],
        'quick_v2_random': [],
        'quick_v2_sorted': []
    }
    
    print("Running benchmarks... (this may take several minutes for large sizes)")
    print("Note: Quick Sort Ver 1 may fail on large sorted lists (RecursionError)")
    print("-" * 80)
    
    for size in sizes:
        print(f"Testing size: {size}...")
        
        # Initialise accumulators for this size
        b_rand_total = 0
        b_sorted_total = 0
        m_rand_total = 0
        m_sorted_total = 0
        q_rand_total = 0
        q_sorted_total = 0
        q1_rand_total = 0
        q1_sorted_total = 0
        q2_rand_total = 0
        q2_sorted_total = 0
        
        successful_runs = runs
        
        for run_idx in range(runs):
            rand_list, sorted_list = generate_lists(size)
            
            # Bubble Sort (in-place)
            b_rand_total += measure_time(bubble_sort, rand_list.copy(), returns_new_list=False)
            b_sorted_total += measure_time(bubble_sort, sorted_list.copy(), returns_new_list=False)
            
            # Merge Sort (returns new list)
            m_rand_total += measure_time(merge_sort, rand_list.copy(), returns_new_list=True)
            m_sorted_total += measure_time(merge_sort, sorted_list.copy(), returns_new_list=True)
            
            # Quick Sort (middle pivot, returns new list)
            q_rand_total += measure_time(quick_sort, rand_list.copy(), returns_new_list=True)
            q_sorted_total += measure_time(quick_sort, sorted_list.copy(), returns_new_list=True)
            
            # Quick Sort Ver 1 (first pivot, returns new list)
            t1 = measure_time(quick_sort_ver_1, rand_list.copy(), returns_new_list=True)
            t2 = measure_time(quick_sort_ver_1, sorted_list.copy(), returns_new_list=True)
            
            # If recursion error occurs, mark as infinite
            if t1 == float('inf'):
                print(f"  Warning: Quick Sort Ver 1 failed on random list size {size}")
                t1 = 0  # Skip this run
                successful_runs -= 1
            if t2 == float('inf'):
                print(f"  Warning: Quick Sort Ver 1 failed on sorted list size {size}")
                t2 = 0
                successful_runs -= 1
            
            q1_rand_total += t1
            q1_sorted_total += t2
            
            # Quick Sort Ver 2 (iterative, in-place)
            q2_rand_total += measure_time(quick_sort_ver_2, rand_list.copy(), returns_new_list=False)
            q2_sorted_total += measure_time(quick_sort_ver_2, sorted_list.copy(), returns_new_list=False)
        
        # Calculate averages (avoid division by zero)
        runs_used = runs if successful_runs > 0 else 1
        results['bubble_random'].append(b_rand_total / runs)
        results['bubble_sorted'].append(b_sorted_total / runs)
        results['merge_random'].append(m_rand_total / runs)
        results['merge_sorted'].append(m_sorted_total / runs)
        results['quick_random'].append(q_rand_total / runs)
        results['quick_sorted'].append(q_sorted_total / runs)
        results['quick_v1_random'].append(q1_rand_total / runs_used if runs_used > 0 else float('inf'))
        results['quick_v1_sorted'].append(q1_sorted_total / runs_used if runs_used > 0 else float('inf'))
        results['quick_v2_random'].append(q2_rand_total / runs)
        results['quick_v2_sorted'].append(q2_sorted_total / runs)
    
    return sizes, results


def print_table_1(sizes, results):
    """Print Table-1 for B1.1 (Bubble, Merge, Quick - random and sorted)"""
    print("\n" + "=" * 120)
    print("TABLE-1: Average execution times (milliseconds)")
    print("=" * 120)
    print(f"{'Size':<8} {'Bubble (Random)':<18} {'Bubble (Sorted)':<18} {'Merge (Random)':<18} {'Merge (Sorted)':<18} {'Quick (Random)':<18} {'Quick (Sorted)':<18}")
    print("-" * 120)
    
    for i, size in enumerate(sizes):
        # Handle infinite values
        br = results['bubble_random'][i]
        bs = results['bubble_sorted'][i]
        mr = results['merge_random'][i]
        ms = results['merge_sorted'][i]
        qr = results['quick_random'][i]
        qs = results['quick_sorted'][i]
        
        print(f"{size:<8} {br:<16.6f} {bs:<16.6f} {mr:<16.6f} {ms:<16.6f} {qr:<16.6f} {qs:<16.6f}")


def print_table_2(sizes, results):
    """Print Table-2 for B1.2 (including Quick Sort v1 and v2)"""
    print("\n" + "=" * 180)
    print("TABLE-2: Average execution times including Quick Sort variants (milliseconds)")
    print("=" * 180)
    print(f"{'Size':<8} {'Bubble R':<12} {'Bubble S':<12} {'Merge R':<12} {'Merge S':<12} "
          f"{'Quick R':<12} {'Quick S':<12} {'Quick v1 R':<12} {'Quick v1 S':<12} "
          f"{'Quick v2 R':<12} {'Quick v2 S':<12}")
    print("-" * 180)
    
    for i, size in enumerate(sizes):
        # Handle infinite values
        q1r = results['quick_v1_random'][i]
        q1s = results['quick_v1_sorted'][i]
        
        q1r_str = "FAILED" if q1r == float('inf') else f"{q1r:<12.6f}"
        q1s_str = "FAILED" if q1s == float('inf') else f"{q1s:<12.6f}"
        
        print(f"{size:<8} {results['bubble_random'][i]:<12.6f} {results['bubble_sorted'][i]:<12.6f} "
              f"{results['merge_random'][i]:<12.6f} {results['merge_sorted'][i]:<12.6f} "
              f"{results['quick_random'][i]:<12.6f} {results['quick_sorted'][i]:<12.6f} "
              f"{q1r_str:<12} {q1s_str:<12} "
              f"{results['quick_v2_random'][i]:<12.6f} {results['quick_v2_sorted'][i]:<12.6f}")


# ==================== MAIN ====================

if __name__ == "__main__":
    # Reduce runs to 3 for faster execution
    sizes, results = run_benchmarks(runs=3)
    
    # Print both tables
    print_table_1(sizes, results)
    print_table_2(sizes, results)
    
    print("\n" + "=" * 80)
    print("Benchmark complete!")
    print("Note: 'FAILED' indicates RecursionError (quick_sort_ver_1 on large lists)")
    print("=" * 80)