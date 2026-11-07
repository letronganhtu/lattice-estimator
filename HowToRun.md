**How to run the lattice estimator:** You need to install python (https://www.python.org/downloads) and conda (https://www.anaconda.com/download)
1. ``git clone https://github.com/malb/lattice-estimator`` to clone the lattice-estimator project into your local computer
2. Enter ``cd lattice-estimator``
3. To test the security level of the LWE instance, we generate a file named ``<file_name>.py`` and paste the following example source code
```python
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
```
4. ``conda create -n <env_name> python=<python_version>``
5. ``conda activate <env_name>``
6. ``conda install -c conda-forge sage``
7. ``python main.py`` to see the output, then the security level is the lowest rop values among all attacks