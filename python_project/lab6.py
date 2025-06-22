# Lab 6: Harmonic series sum up to n terms

n = int(input("Enter number of terms for harmonic series: "))  # Prompt user for the number of terms and convert input to integer

harmonic_sum = 0.0  # Initialize the sum of the harmonic series to 0.0

for i in range(1, n + 1):  # Loop from 1 to n (inclusive)
    harmonic_sum += 1 / i  # Add the reciprocal of i to the sum

print(f"Harmonic sum up to {n} terms is: {harmonic_sum:.4f}")  # Print the result rounded to 4 decimal places
