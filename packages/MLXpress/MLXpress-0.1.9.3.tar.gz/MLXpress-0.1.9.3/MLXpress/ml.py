class LinearReg:
    """
    Example:
# Example usage:
# Assuming you have x and y data
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

model = LinearReg(x, y)
x_pred = [6, 7, 8]
y_pred = model.predict(x_pred)

print("Slope:", model.slope)
print("Intercept:", model.intercept)
print("Predictions for", x_pred, ":", y_pred)
    """

    def __init__(self, x, y):
        """
        Initialize the LinearReg object with input data.

        Parameters:
        - x (list): List of x-values (independent variable).
        - y (list): List of y-values (dependent variable).
        """
        self.x = x
        self.y = y
        self.slope, self.intercept = self.calculate_regression_parameters()

    def calculate_mean(self, values):
        """
        Calculate the mean of a list of values.

        Parameters:
        - values (list): List of numerical values.

        Returns:
        - mean (float): Mean of the input values.
        """
        return sum(values) / len(values)

    def calculate_slope(self, x, y, x_mean, y_mean):
        """
        Calculate the slope of the linear regression line.

        Parameters:
        - x (list): List of x-values (independent variable).
        - y (list): List of y-values (dependent variable).
        - x_mean (float): Mean of x.
        - y_mean (float): Mean of y.

        Returns:
        - slope (float): Slope of the linear regression line.
        """
        numerator = sum((xi - x_mean) * (yi - y_mean) for xi, yi in zip(x, y))
        denominator = sum((xi - x_mean) ** 2 for xi in x)
        return numerator / denominator

    def calculate_intercept(self, x_mean, y_mean, slope):
        """
        Calculate the intercept of the linear regression line.

        Parameters:
        - x_mean (float): Mean of x.
        - y_mean (float): Mean of y.
        - slope (float): Slope of the linear regression line.

        Returns:
        - intercept (float): Intercept of the linear regression line.
        """
        return y_mean - slope * x_mean

    def calculate_regression_parameters(self):
        """
        Calculate the slope and intercept of the linear regression line.

        Returns:
        - slope (float): Slope of the linear regression line.
        - intercept (float): Intercept of the linear regression line.
        """
        x_mean = self.calculate_mean(self.x)
        y_mean = self.calculate_mean(self.y)
        slope = self.calculate_slope(self.x, self.y, x_mean, y_mean)
        intercept = self.calculate_intercept(x_mean, y_mean, slope)
        return slope, intercept

    def predict(self, x_pred):
        """
        Make predictions using the linear regression model.

        Parameters:
        - x_pred (list): List of x-values for prediction.

        Returns:
        - predictions (list): List of predicted y-values.
        """
        return [self.slope * xi + self.intercept for xi in x_pred]


from collections import Counter


class KNN:
    def __init__(self, k=3):
        """
        Initialize the KNN classifier.

        Parameters:
        - k (int): Number of neighbors to consider.
        """
        self.k = k
        self.X_train = None
        self.y_train = None

    def fit(self, X_train, y_train):
        """
        Fit the KNN model to the training data.

        Parameters:
        - X_train (list of lists): Training feature vectors.
        - y_train (list): Corresponding labels for the training data.
        """
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test):
        """
        Predict labels for the test data.

        Parameters:
        - X_test (list of lists): Test feature vectors.

        Returns:
        - y_pred (list): Predicted labels for the test data.
        """
        y_pred = []
        for x_test in X_test:
            distances = [self._euclidean_distance(x_test, x_train) for x_train in self.X_train]
            sorted_indices = sorted(range(len(distances)), key=lambda k: distances[k])
            k_nearest_labels = [self.y_train[i] for i in sorted_indices[:self.k]]
            most_common_label = self._majority_vote(k_nearest_labels)
            y_pred.append(most_common_label)
        return y_pred

    def _euclidean_distance(self, x1, x2):
        """
        Compute the Euclidean distance between two vectors.

        Parameters:
        - x1 (list): First vector.
        - x2 (list): Second vector.

        Returns:
        - distance (float): Euclidean distance between x1 and x2.
        """
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(x1, x2)))

    def _majority_vote(self, labels):
        """
        Perform majority voting to determine the most common label.

        Parameters:
        - labels (list): List of labels.

        Returns:
        - majority_label: Most common label.
        """
        counter = Counter(labels)
        majority_label = counter.most_common(1)[0][0]
        return majority_label


from collections import defaultdict


class NaiveBayes:
    """
    # Example usage:
# Assuming you have X (features) and y (labels)
X = [[1, 1], [1, 0], [0, 1], [0, 0]]
y = [1, 0, 1, 0]

# Initialize and train the Naive Bayes classifier
nb_classifier = NaiveBayes()
nb_classifier.train(X, y)

# Make predictions
new_X = [[1, 1], [0, 0]]
predictions = nb_classifier.predict(new_X)

print("Predictions:", predictions)
    """

    def __init__(self):
        """
        Initialize the NaiveBayes object.
        """
        self.class_probs = defaultdict(float)
        self.feature_probs = defaultdict(lambda: defaultdict(float))

    def calculate_class_probs(self, labels):
        """
        Calculate class probabilities.

        Parameters:
        - labels (list): List of labels (0 or 1).

        Returns:
        - class_probs (dict): Dictionary containing class probabilities.
        """
        total_samples = len(labels)
        class_probs = defaultdict(float)

        for label in labels:
            class_probs[label] += 1

        for label in class_probs:
            class_probs[label] /= total_samples

        return class_probs

    def calculate_feature_probs(self, features, labels):
        """
        Calculate feature probabilities given the class.

        Parameters:
        - features (list of lists): List of feature vectors.
        - labels (list): List of labels (0 or 1).

        Returns:
        - feature_probs (dict): Dictionary containing feature probabilities for each class.
        """
        total_samples = len(labels)
        feature_probs = defaultdict(lambda: defaultdict(float))

        for feature_vector, label in zip(features, labels):
            for i, feature in enumerate(feature_vector):
                feature_probs[label][i, feature] += 1

        for label in feature_probs:
            for feature, count in feature_probs[label].items():
                feature_probs[label][feature] = count / total_samples

        return feature_probs

    def train(self, features, labels):
        """
        Train the Naive Bayes classifier.

        Parameters:
        - features (list of lists): List of feature vectors.
        - labels (list): List of labels (0 or 1).
        """
        self.class_probs = self.calculate_class_probs(labels)
        self.feature_probs = self.calculate_feature_probs(features, labels)

    def calculate_posterior(self, feature_vector, label):
        """
        Calculate the posterior probability for a given feature vector and class.

        Parameters:
        - feature_vector (list): Feature vector.
        - label (int): Class label.

        Returns:
        - posterior (float): Posterior probability.
        """
        posterior = 1.0
        for i, feature in enumerate(feature_vector):
            posterior *= self.feature_probs[label][i, feature]

        return posterior * self.class_probs[label]

    def predict_single(self, feature_vector):
        """
        Predict the label for a single feature vector.

        Parameters:
        - feature_vector (list): Feature vector.

        Returns:
        - label (int): Predicted label (0 or 1).
        """
        class_scores = {label: self.calculate_posterior(feature_vector, label) for label in self.class_probs}
        return max(class_scores, key=class_scores.get)

    def predict(self, features):
        """
        Predict labels for a set of feature vectors.

        Parameters:
        - features (list of lists): List of feature vectors.

        Returns:
        - predictions (list): List of predicted labels.
        """
        return [self.predict_single(feature_vector) for feature_vector in features]


class SVM:
    """
    # Example usage:
# Assuming you have training data X_train, y_train
X_train = np.array([[1, 2], [2, 3], [3, 4], [1.5, 2.5], [3.5, 4.5]])
y_train = np.array([1, 1, 1, -1, -1])

# Initialize and fit the SVM model
svm_model = SVM()
svm_model.fit(X_train, y_train)

# Test data
X_test = np.array([[2, 2], [3, 3]])

# Make predictions
predictions = svm_model.predict(X_test)

# Print the predicted labels
print("Predicted Labels:", predictions)
    """

    def __init__(self, learning_rate=0.01, max_epochs=1000):
        """
        Initialize the SVM object.

        Parameters:
        - learning_rate (float): The learning rate for the optimization.
        - max_epochs (int): The maximum number of training epochs.
        """
        self.learning_rate = learning_rate
        self.max_epochs = max_epochs
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        """
        Fit the SVM model to the training data.

        Parameters:
        - X (numpy array): Input feature matrix.
        - y (numpy array): Target labels.
        """
        # Initialize weights and bias
        num_features = X.shape[1]
        self.weights = np.zeros(num_features)
        self.bias = 0

        # Perceptron training
        for epoch in range(1, self.max_epochs + 1):
            for i in range(len(X)):
                if y[i] * (np.dot(X[i], self.weights) + self.bias) <= 1:
                    # Update weights and bias
                    self.weights += self.learning_rate * (y[i] * X[i] - 2 / epoch * self.weights)
                    self.bias += self.learning_rate * y[i]

    def predict(self, X):
        """
        Make predictions using the trained SVM model.

        Parameters:
        - X (numpy array): Input feature matrix for prediction.

        Returns:
        - predictions (numpy array): Predicted labels.
        """
        return np.sign(np.dot(X, self.weights) + self.bias)


import numpy as np


class KMeans:
    """
    # Example usage:
# Assuming you have X (data points)
X = np.array([[1, 2], [5, 8], [1.5, 1.8], [8, 8], [1, 0.6], [9, 11]])

# Initialize and fit the KMeans model
kmeans = KMeans(k=2)
kmeans.fit(X)

# Make predictions for new data
new_data = np.array([[0, 0], [10, 10]])
predictions = kmeans.predict(new_data)

print("Cluster Labels:", predictions)
    """

    def __init__(self, k, max_iterations=100):
        """
        Initialize the KMeans object.

        Parameters:
        - k (int): Number of clusters.
        - max_iterations (int): Maximum number of iterations for the algorithm.
        """
        self.k = k
        self.max_iterations = max_iterations
        self.centroids = None
        self.labels = None

    def initialize_centroids(self, data):
        """
        Initialize centroids randomly from the data.

        Parameters:
        - data (numpy array): Input data.

        Returns:
        - centroids (numpy array): Initial centroids.
        """
        np.random.shuffle(data)
        return data[:self.k]

    def assign_labels(self, data, centroids):
        """
        Assign labels to data points based on the closest centroid.

        Parameters:
        - data (numpy array): Input data.
        - centroids (numpy array): Current centroids.

        Returns:
        - labels (numpy array): Assigned labels.
        """
        distances = np.linalg.norm(data[:, np.newaxis] - centroids, axis=2)
        labels = np.argmin(distances, axis=1)
        return labels

    def update_centroids(self, data, labels):
        """
        Update centroids based on the mean of the data points in each cluster.

        Parameters:
        - data (numpy array): Input data.
        - labels (numpy array): Assigned labels.

        Returns:
        - centroids (numpy array): Updated centroids.
        """
        centroids = np.array([np.mean(data[labels == i], axis=0) for i in range(self.k)])
        return centroids

    def fit(self, data):
        """
        Fit the KMeans model to the data.

        Parameters:
        - data (numpy array): Input data.
        """
        self.centroids = self.initialize_centroids(data)

        for _ in range(self.max_iterations):
            old_centroids = self.centroids.copy()
            self.labels = self.assign_labels(data, self.centroids)
            self.centroids = self.update_centroids(data, self.labels)

            if np.all(old_centroids == self.centroids):
                break

    def predict(self, data):
        """
        Predict cluster labels for new data.

        Parameters:
        - data (numpy array): New data.

        Returns:
        - labels (numpy array): Predicted cluster labels.
        """
        distances = np.linalg.norm(data[:, np.newaxis] - self.centroids, axis=2)
        labels = np.argmin(distances, axis=1)
        return labels


import math


class LogisticRegression:
    """
    # Example usage:
# Assuming you have X (features) and y (labels)
X = [[1, 2], [2, 3], [3, 4], [4, 5]]
y = [0, 0, 1, 1]

# Initialize and train the logistic regression model
logreg = LogisticRegression(X, y, learning_rate=0.01, epochs=1000)
logreg.gradient_descent()

# Make predictions
new_X = [[5, 6], [1, 2]]
predictions = logreg.predict(new_X)

print("Predictions:", predictions)
    """

    def __init__(self, X, y, learning_rate=0.01, epochs=1000):
        """
        Initialize the LogisticRegression object.

        Parameters:
        - X (list): List of input features.
        - y (list): List of target labels (0 or 1).
        - learning_rate (float): Learning rate for gradient descent.
        - epochs (int): Number of training epochs.
        """
        self.X = X
        self.y = y
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = [0.0] * len(X[0])  # Initialize weights to zeros

    def sigmoid(self, z):
        """
        Sigmoid function.

        Parameters:
        - z (float): Input to the sigmoid function.

        Returns:
        - result (float): Result of the sigmoid function.
        """
        return 1 / (1 + math.exp(-z))

    def predict_proba(self, X):
        """
        Predict probabilities for the given input features.

        Parameters:
        - X (list): List of input features.

        Returns:
        - probabilities (list): List of predicted probabilities.
        """
        return [self.sigmoid(sum(w * x_i for w, x_i in zip(self.weights, x))) for x in X]

    def predict(self, X, threshold=0.5):
        """
        Predict binary labels (0 or 1) for the given input features.

        Parameters:
        - X (list): List of input features.
        - threshold (float): Threshold for classification.

        Returns:
        - predictions (list): List of predicted labels.
        """
        return [1 if prob >= threshold else 0 for prob in self.predict_proba(X)]

    def cost_function(self, y_true, y_pred):
        """
        Calculate the logistic regression cost function.

        Parameters:
        - y_true (list): List of true labels.
        - y_pred (list): List of predicted probabilities.

        Returns:
        - cost (float): Logistic regression cost.
        """
        m = len(y_true)
        return (-1 / m) * sum(
            y_i * math.log(prob) + (1 - y_i) * math.log(1 - prob) for y_i, prob in zip(y_true, y_pred))

    def gradient_descent(self):
        """
        Perform gradient descent to update weights.
        """
        m = len(self.y)
        for epoch in range(self.epochs):
            predictions = self.predict_proba(self.X)
            errors = [pred - y_i for pred, y_i in zip(predictions, self.y)]

            for j in range(len(self.weights)):
                gradient = (1 / m) * sum(errors[i] * self.X[i][j] for i in range(m))
                self.weights[j] -= self.learning_rate * gradient

            cost = self.cost_function(self.y, predictions)
            print(f"Epoch {epoch + 1}/{self.epochs}, Cost: {cost}")


class DecisionTree:
    def __init__(self, max_depth=None):
        """
        Initialize the DecisionTree object.

        Parameters:
        - max_depth (int or None): Maximum depth of the tree. If None, the tree will grow until all leaves are pure.
        """
        self.max_depth = max_depth
        self.tree = None

    def calculate_entropy(self, data):
        """
        Calculate the entropy of a dataset.

        Parameters:
        - data (list): List of labels (0 or 1).

        Returns:
        - entropy (float): Entropy of the dataset.
        """
        total_samples = len(data)
        if total_samples == 0:
            return 0

        p_positive = sum(label == 1 for label in data) / total_samples
        p_negative = 1 - p_positive

        if p_positive == 0 or p_negative == 0:
            return 0

        entropy = -p_positive * math.log2(p_positive) - p_negative * math.log2(p_negative)
        return entropy

    def calculate_information_gain(self, feature, labels, threshold):
        """
        Calculate the information gain for a split.

        Parameters:
        - feature (list): List of feature values.
        - labels (list): List of labels (0 or 1).
        - threshold (float): Threshold for splitting the feature.

        Returns:
        - information_gain (float): Information gain for the split.
        """
        total_samples = len(labels)
        left_labels = [label for label, value in zip(labels, feature) if value <= threshold]
        right_labels = [label for label, value in zip(labels, feature) if value > threshold]

        entropy_parent = self.calculate_entropy(labels)
        entropy_left = (len(left_labels) / total_samples) * self.calculate_entropy(left_labels)
        entropy_right = (len(right_labels) / total_samples) * self.calculate_entropy(right_labels)

        information_gain = entropy_parent - entropy_left - entropy_right
        return information_gain

    def find_best_split(self, X, y):
        """
        Find the best split for a node.

        Parameters:
        - X (list of lists): List of feature vectors.
        - y (list): List of labels (0 or 1).

        Returns:
        - best_split (dict): Dictionary containing the best split information.
        """
        features = len(X[0])
        total_samples = len(y)
        best_split = {'feature_index': None, 'threshold': None, 'information_gain': 0}

        for feature_index in range(features):
            unique_values = set(row[feature_index] for row in X)
            for value in unique_values:
                information_gain = self.calculate_information_gain([row[feature_index] for row in X], y, value)
                if information_gain > best_split['information_gain']:
                    best_split['feature_index'] = feature_index
                    best_split['threshold'] = value
                    best_split['information_gain'] = information_gain

        return best_split

    def build_tree(self, X, y, depth):
        """
        Recursively build the decision tree.

        Parameters:
        - X (list of lists): List of feature vectors.
        - y (list): List of labels (0 or 1).
        - depth (int): Current depth of the tree.

        Returns:
        - node (dict): Dictionary representing a tree node.
        """
        if depth == 0 or len(set(y)) == 1:
            # If max depth is reached or all labels are the same, create a leaf node
            return {'leaf': True, 'label': max(set(y), key=y.count)}

        best_split = self.find_best_split(X, y)

        if best_split['information_gain'] == 0:
            # If no information gain, create a leaf node
            return {'leaf': True, 'label': max(set(y), key=y.count)}

        left_indices = [i for i, value in enumerate(X) if value[best_split['feature_index']] <= best_split['threshold']]
        right_indices = [i for i, value in enumerate(X) if value[best_split['feature_index']] > best_split['threshold']]

        left_child = self.build_tree([X[i] for i in left_indices], [y[i] for i in left_indices], depth - 1)
        right_child = self.build_tree([X[i] for i in right_indices], [y[i] for i in right_indices], depth - 1)

        return {'leaf': False, 'feature_index': best_split['feature_index'],
                'threshold': best_split['threshold'], 'left_child': left_child, 'right_child': right_child}

    def train(self, X, y):
        """
        Train the decision tree.

        Parameters:
        - X (list of lists): List of feature vectors.
        - y (list): List of labels (0 or 1).
        """
        self.tree = self.build_tree(X, y, self.max_depth)

    def predict_single(self, node, sample):
        """
        Predict the label for a single sample.

        Parameters:
        - node (dict): Tree node.
        - sample (list): Feature vector.

        Returns:
        - label (int): Predicted label (0 or 1).
        """
        if node['leaf']:
            return node['label']
        else:
            if sample[node['feature_index']] <= node['threshold']:
                return self.predict_single(node['left_child'], sample)
            else:
                return self.predict_single(node['right_child'], sample)

    def predict(self, X):
        """
        Predict labels for a set of samples.

        Parameters:
        - X (list of lists): List of feature vectors.

        Returns:
        - predictions (list): List of predicted labels.
        """
        return [self.predict_single(self.tree, sample) for sample in X]


class DecisionTree:
    """
    # Example usage:
# Assuming you have X (features) and y (labels)
X = [[1, 2], [2, 3], [3, 4], [4, 5]]
y = [0, 0, 1, 1]

# Initialize and train the decision tree
dt = DecisionTree(max_depth=3)
dt.train(X, y)

# Make predictions
new_X = [[5, 6], [1, 2]]
predictions = dt.predict(new_X)

print("Predictions:", predictions)
    """

    def __init__(self, max_depth=None):
        """
        Initialize the DecisionTree object.

        Parameters:
        - max_depth (int or None): Maximum depth of the tree. If None, the tree will grow until all leaves are pure.
        """
        self.max_depth = max_depth
        self.tree = None

    def calculate_entropy(self, data):
        """
        Calculate the entropy of a dataset.

        Parameters:
        - data (list): List of labels (0 or 1).

        Returns:
        - entropy (float): Entropy of the dataset.
        """
        total_samples = len(data)
        if total_samples == 0:
            return 0

        p_positive = sum(label == 1 for label in data) / total_samples
        p_negative = 1 - p_positive

        if p_positive == 0 or p_negative == 0:
            return 0

        entropy = -p_positive * math.log2(p_positive) - p_negative * math.log2(p_negative)
        return entropy

    def calculate_information_gain(self, feature, labels, threshold):
        """
        Calculate the information gain for a split.

        Parameters:
        - feature (list): List of feature values.
        - labels (list): List of labels (0 or 1).
        - threshold (float): Threshold for splitting the feature.

        Returns:
        - information_gain (float): Information gain for the split.
        """
        total_samples = len(labels)
        left_labels = [label for label, value in zip(labels, feature) if value <= threshold]
        right_labels = [label for label, value in zip(labels, feature) if value > threshold]

        entropy_parent = self.calculate_entropy(labels)
        entropy_left = (len(left_labels) / total_samples) * self.calculate_entropy(left_labels)
        entropy_right = (len(right_labels) / total_samples) * self.calculate_entropy(right_labels)

        information_gain = entropy_parent - entropy_left - entropy_right
        return information_gain

    def find_best_split(self, X, y):
        """
        Find the best split for a node.

        Parameters:
        - X (list of lists): List of feature vectors.
        - y (list): List of labels (0 or 1).

        Returns:
        - best_split (dict): Dictionary containing the best split information.
        """
        features = len(X[0])
        total_samples = len(y)
        best_split = {'feature_index': None, 'threshold': None, 'information_gain': 0}

        for feature_index in range(features):
            unique_values = set(row[feature_index] for row in X)
            for value in unique_values:
                information_gain = self.calculate_information_gain([row[feature_index] for row in X], y, value)
                if information_gain > best_split['information_gain']:
                    best_split['feature_index'] = feature_index
                    best_split['threshold'] = value
                    best_split['information_gain'] = information_gain

        return best_split

    def build_tree(self, X, y, depth):
        """
        Recursively build the decision tree.

        Parameters:
        - X (list of lists): List of feature vectors.
        - y (list): List of labels (0 or 1).
        - depth (int): Current depth of the tree.

        Returns:
        - node (dict): Dictionary representing a tree node.
        """
        if depth == 0 or len(set(y)) == 1:
            # If max depth is reached or all labels are the same, create a leaf node
            return {'leaf': True, 'label': max(set(y), key=y.count)}

        best_split = self.find_best_split(X, y)

        if best_split['information_gain'] == 0:
            # If no information gain, create a leaf node
            return {'leaf': True, 'label': max(set(y), key=y.count)}

        left_indices = [i for i, value in enumerate(X) if value[best_split['feature_index']] <= best_split['threshold']]
        right_indices = [i for i, value in enumerate(X) if value[best_split['feature_index']] > best_split['threshold']]

        left_child = self.build_tree([X[i] for i in left_indices], [y[i] for i in left_indices], depth - 1)
        right_child = self.build_tree([X[i] for i in right_indices], [y[i] for i in right_indices], depth - 1)

        return {'leaf': False, 'feature_index': best_split['feature_index'],
                'threshold': best_split['threshold'], 'left_child': left_child, 'right_child': right_child}

    def train(self, X, y):
        """
        Train the decision tree.

        Parameters:
        - X (list of lists): List of feature vectors.
        - y (list): List of labels (0 or 1).
        """
        self.tree = self.build_tree(X, y, self.max_depth)

    def predict_single(self, node, sample):
        """
        Predict the label for a single sample.

        Parameters:
        - node (dict): Tree node.
        - sample (list): Feature vector.

        Returns:
        - label (int): Predicted label (0 or 1).
        """
        if node['leaf']:
            return node['label']
        else:
            if sample[node['feature_index']] <= node['threshold']:
                return self.predict_single(node['left_child'], sample)
            else:
                return self.predict_single(node['right_child'], sample)

    def predict(self, X):
        """
        Predict labels for a set of samples.

        Parameters:
        - X (list of lists): List of feature vectors.

        Returns:
        - predictions (list): List of predicted labels.
        """
        return [self.predict_single(self.tree, sample) for sample in X]
