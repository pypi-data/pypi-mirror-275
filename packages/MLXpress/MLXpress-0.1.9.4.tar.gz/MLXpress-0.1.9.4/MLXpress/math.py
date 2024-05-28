from math import sqrt

import scipy.stats as stats


def pdf(x, distribution):
    """Calculate the probability density function (PDF) of a given distribution at a specific point and print the result."""
    pdf1 = distribution.pdf(x)
    print("Probability Density Function (PDF):", pdf1)


def hypothesis_test(data1, data2):
    """Perform a t-test to compare the means of two datasets and print the results."""
    t_statistic, p_value = stats.ttest_ind(data1, data2)
    print("T-Statistic:", t_statistic)
    print("P-Value:", p_value)


def _euclidean_distance(self, x1, x2):
    """
    Compute the Euclidean distance between two vectors.

    Parameters:
    - x1 (list): First vector.
    - x2 (list): Second vector.

    Returns:
    - distance (float): Euclidean distance between x1 and x2.
    """
    return sqrt(sum((a - b) ** 2 for a, b in zip(x1, x2)))


def calculate_covariance_matrix(data):
    """
    Calculate the covariance matrix for a given dataset.

    Parameters:
    - data (list of lists): Input data with variables in inner lists and observations in outer lists.

    Returns:
    - cov_matrix (list of lists): Covariance matrix of the input data.
    """
    num_variables = len(data[0])
    num_observations = len(data)

    # Calculate means for each variable
    means = [sum(variable) / num_observations for variable in zip(*data)]

    # Initialize covariance matrix
    cov_matrix = [[0.0] * num_variables for _ in range(num_variables)]

    # Calculate covariances
    for i in range(num_variables):
        for j in range(num_variables):
            cov_matrix[i][j] = sum(
                (data[k][i] - means[i]) * (data[k][j] - means[j]) for k in range(num_observations)) / (
                                           num_observations - 1)

    return cov_matrix


def cosine_sim(v1, v2):
    """
    Calculate the cosine similarity between two vectors.

    Parameters:
    - v1 (list): The first vector.
    - v2 (list): The second vector.

    Returns:
    float: The cosine similarity between the two vectors.

    Notes:
    The cosine similarity is a measure of similarity between two non-zero vectors
    of an inner product space that measures the cosine of the angle between them.
    It is often used as a similarity metric for documents or vectors in N-dimensional space.

    The formula for cosine similarity between two vectors v1 and v2 is given by:
    cosine_sim(v1, v2) = dot_product(v1, v2) / (magnitude(v1) * magnitude(v2))

    where dot_product is the dot product of v1 and v2, and magnitude is the magnitude of a vector.
    """

    def magnitude(v):
        """
        Calculate the magnitude of a vector.

        Parameters:
        - v (list): The vector.

        Returns:
        float: The magnitude of the vector.
        """
        return sqrt(sum(x ** 2 for x in v))

    def dot_product(v1, v2):
        """
        Calculate the dot product between two vectors.

        Parameters:
        - v1 (list): The first vector.
        - v2 (list): The second vector.

        Returns:
        float: The dot product of the two vectors.
        """
        return sum(x * y for x, y in zip(v1, v2))

    return dot_product(v1, v2) / (magnitude(v1) * magnitude(v2))
