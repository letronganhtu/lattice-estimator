from estimator import LWE, ND
    
params = LWE.Parameters(
    n = 495 * 2,      # LWE dimension
    q = 37001558813,  # modulus
    Xs = ND.CenteredBinomial(eta = 3), # secret distribution (eta = 3 for Kyber-512)
    Xe = ND.CenteredBinomial(eta = 2), # error distribution
    m = 512,          # number of LWE samples
    tag = "Kyber-512 (unrolled)",
)

# Run all attacks and print results
result = LWE.estimate(params)
print(result)