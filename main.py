from estimator import LWE, ND, SIS
from sage.all import oo
    
params_LWE = LWE.Parameters(
    n = 495 * 2,      # LWE dimension
    q = 37001558813,  # modulus
    Xs = ND.CenteredBinomial(eta = 3), # secret distribution (eta = 3 for Kyber-512)
    Xe = ND.CenteredBinomial(eta = 2), # error distribution
    m = 512,          # number of LWE samples
    tag = "Kyber-512 (unrolled)",
)

# Run all attacks and print results
result_LWE = LWE.estimate(params_LWE)
print(result_LWE)

params_SIS = SIS.Parameters(
    n = 256 * 4,
    q = 8380417,
    m = 256 * 9,
    length_bound = 350209,
    norm = 2, ## oo for the infinity norm bound, and need to import the additional library "from sage.all import oo"
    tag = "My-Module-SIS"
)

print("Module-SIS parameters:")
print(params_SIS)

print("\nRough security estimation:")
rough = SIS.estimate.rough(params_SIS)

print("\nFull security estimation:")
full = SIS.estimate(params_SIS)
print(full)