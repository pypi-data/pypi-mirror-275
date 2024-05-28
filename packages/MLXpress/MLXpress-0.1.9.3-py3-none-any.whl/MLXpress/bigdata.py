def cal_pagerank(graph, pagerank=None, iterations=10, df=0.85):
    """
Mandatory Argument:
graph: The user shall pass a dictionary to the function which shall denote the graph linkage of pages

Optional Arguments:
pagerank: The user may pass a graph denoting the inital pagerank values to the argument. By default this value is set to 1.0 for all nodes.
iterations: The user may pass an Integer value as an argument to specify number of iterations to be performed. By default this value is set to 10.
df: The user may pass a floating point value to specify the damping_factor. By default this value is set to 0.85
}
"""

    if pagerank is None:
        pagerank = {node: 1.0 for node in graph}

    for __ in range(iterations):
        new_pr = {}
        for page in graph:
            new_rank = 1 - df
            new_rank += df * sum(pagerank[link] / len(graph[link]) for link in graph if page in graph[link])
            new_pr[page] = new_rank
        pagerank = new_pr

    for page, rank in pagerank.items():
        print(f' Page:{page} - PageRank:{rank : .4f}')


class BloomFilter:
    """
    # Example usage:
bloom_filter = BloomFilter(size=10, num_hashes=3)

# Add items to the Bloom Filter
bloom_filter.add("apple")
bloom_filter.add("banana")
bloom_filter.add("orange")

# Check if items are in the Bloom Filter
print("Contains 'apple':", bloom_filter.contains("apple"))  # True
print("Contains 'grape':", bloom_filter.contains("grape"))  # False
print("Contains 'orange':", bloom_filter.contains("orange"))  # True
    """

    def _init_(self, size, num_hashes):
        """
        Initialize the BloomFilter object.

        Parameters:
        - size (int): Size of the bit array.
        - num_hashes (int): Number of hash functions.
        """
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = [0] * size

    def add(self, item):
        """
        Add an item to the Bloom Filter.

        Parameters:
        - item (str): The item to add.
        """
        for i in range(self.num_hashes):
            index = hash(item + str(i)) % self.size
            self.bit_array[index] = 1

    def contains(self, item):
        """
        Check if the Bloom Filter contains an item.

        Parameters:
        - item (str): The item to check.

        Returns:
        - contains (bool): True if the item is possibly in the set, False if it is definitely not.
        """
        for i in range(self.num_hashes):
            index = hash(item + str(i)) % self.size
            if not self.bit_array[index]:
                return False
        return True


def apriori(dataset, min_support):
    """
    Apriori algorithm for generating frequent itemsets from a dataset.

    Parameters:
    - dataset (list): List of transactions, where each transaction is a list of items.
    - min_support (float): Minimum support threshold for frequent itemsets.

    Returns:
    - frequent_itemsets (list): List of frequent itemsets.
    """

    transactions = dataset
    items = list({item for transaction in transactions for item in transaction})

    frequent_itemsets = []
    k = 1

    # Function to generate candidate itemsets of size k
    def generate_candidates(prev_candidates, k):
        candidates = []
        n = len(prev_candidates)

        for i in range(n):
            for j in range(i + 1, n):
                itemset1 = prev_candidates[i]
                itemset2 = prev_candidates[j]

                if itemset1[:k - 2] == itemset2[:k - 2]:
                    candidates.append(sorted(set(itemset1) | set(itemset2)))

        return candidates

    # Pruning candidates that do not meet the threshold
    def prune_candidates(candidates, dataset, min_support):
        support_counts = {}

        for transaction in dataset:
            for candidate in candidates:
                if set(candidate).issubset(set(transaction)):
                    support_counts.setdefault(tuple(candidate), 0)
                    support_counts[tuple(candidate)] += 1

        total_transactions = len(dataset)
        frequent_candidates = []

        for candidate, count in support_counts.items():
            support = count / total_transactions
            if support >= min_support:
                frequent_candidates.append(list(candidate))

        return frequent_candidates

    while True:
        # Generate candidates of size k
        candidates = [[item] for item in items]
        frequent_candidates = prune_candidates(candidates, transactions, min_support)

        if not frequent_candidates:
            break

        # Extend the list of frequent itemsets
        frequent_itemsets.extend(frequent_candidates)
        k += 1

        # Generate candidates of size k+1
        candidates = generate_candidates(frequent_candidates, k)
        frequent_candidates = prune_candidates(candidates, transactions, min_support)

        if not frequent_candidates:
            break

        # Extend the list of frequent itemsets
        frequent_itemsets.extend(frequent_candidates)
        k += 1

        # Generate candidates of size k+2
        candidates = generate_candidates(frequent_candidates, k)
        frequent_candidates = prune_candidates(candidates, transactions, min_support)

        if not frequent_candidates:
            break

        # Extend the list of frequent itemsets
        frequent_itemsets.extend(frequent_candidates)
        k += 1

    return frequent_itemsets
