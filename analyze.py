import numpy as np
from numpy.linalg import norm, svd

# Frobenius Norm
def frobenius_norm(matrix):
    return np.sqrt(np.sum(np.square(matrix)))

# Spectral Norm
def spectral_norm(matrix):
    _, singular_values, _ = svd(matrix)
    return np.max(singular_values)

# Nuclear Norm
def nuclear_norm(matrix):
    _, singular_values, _ = svd(matrix)
    return np.sum(singular_values)

# Example usage:
# Create a random matrix for demonstration purposes
random_matrix = np.random.rand(3, 3)

# Compute norms
frobenius_norm_result = frobenius_norm(random_matrix)
spectral_norm_result = spectral_norm(random_matrix)
nuclear_norm_result = nuclear_norm(random_matrix)

# Print results
print("Frobenius Norm:", frobenius_norm_result)
print("Spectral Norm:", spectral_norm_result)
print("Nuclear Norm:", nuclear_norm_result)
