from argparse import ArgumentParser
import os
import shutil

MAPPING = {
    # 'tutorials/retired/intro_rydberg_blockade.ipynb' : '1. First steps/1.1 intro_rydberg_blockade.ipynb',
    # 'tutorials/creating_sequences.ipynb' : '1. First steps/1.2. creating_sequences.ipynb',
    # 'tutorials/retired/simulating_sequences.ipynb' : '1. First steps/1.3. simulating_sequences.ipynb',
    # 'tutorials/classical_simulation/Simulating Sequences with Errors and Noise.ipynb' : '3. Classical simulation/3.1. Simulating Sequences with Errors and Noise.ipynb',
    # 'tutorials/classical_simulation/Simulating with SPAM errors.ipynb' : '3. Classical simulation/3.2. Simulating with SPAM errors.ipynb',
    # 'tutorials/classical_simulation/Simulating with laser noises.ipynb' : '3. Classical simulation/3.3. Simulating with laser noises.ipynb',
    # 'tutorials/classical_simulation/Simulating with effective noise channels.ipynb' : '3. Classical simulation/3.4. Simulating with effective noise channels.ipynb',
    # 'tutorials/advanced_features/Composite Waveforms.ipynb' : '4. Advanced features/4.1. Composite Waveforms.ipynb',
    # 'tutorials/advanced_features/Parametrized Sequences.ipynb' : '4. Advanced features/4.2. Parametrized Sequences.ipynb',
    # 'tutorials/advanced_features/Register Layouts.ipynb' : '4. Advanced features/4.3. Register Layouts.ipynb',
    # 'tutorials/advanced_features/Interpolated Waveforms.ipynb' : '4. Advanced features/4.4. Interpolated Waveforms.ipynb',
    # 'tutorials/advanced_features/Serialization.ipynb' : '4. Advanced features/4.5. Serialization.ipynb',
    # 'tutorials/advanced_features/Local addressability with DMM.ipynb' : '4. Advanced features/4.6. Local addressability with DMM.ipynb',
    # 'tutorials/advanced_features/State Preparation with the SLM Mask.ipynb' : '4. Advanced features/4.7. State Preparation with the SLM Mask.ipynb',
    # 'tutorials/advanced_features/Output Modulation and EOM Mode.ipynb' : '4. Advanced features/4.8. Output Modulation and EOM Mode.ipynb',
    # 'tutorials/advanced_features/Virtual Devices.ipynb' : '4. Advanced features/4.9. Virtual Devices.ipynb',
    # 'tutorials/retired/Preparing state with antiferromagnetic order in the Ising model.ipynb' : '5. Quantum simulation/5.1. Preparing state with antiferromagnetic order in the Ising model.ipynb',
    # 'tutorials/quantum_simulation/Bayesian Optimisation for antiferromagnetic state preparation.ipynb' : '5. Quantum simulation/5.2. Bayesian Optimisation for antiferromagnetic state preparation.ipynb',
    # 'tutorials/quantum_simulation/Spin chain of 3 atoms in XY mode.ipynb' : '5. Quantum simulation/5.3. Spin chain of 3 atoms in XY mode.ipynb',
    # 'tutorials/retired/Microwave-engineering of programmable XXZ Hamiltonians in arrays of Rydberg atoms.ipynb' : '5. Quantum simulation/5.4. Microwave-engineering of programmable XXZ Hamiltonians in arrays of Rydberg atoms.ipynb',
    'tutorials/retired/Shadow estimation for VQS.ipynb' : '5. Quantum simulation/5.4. Shadow estimation for VQS.ipynb',
    # 'tutorials/applications/QAOA and QAA to solve a QUBO problem.ipynb' : '6. Other applications/6.1. QAOA and QAA to solve a QUBO problem.ipynb',
}

if __name__ == "__main__":
    argparser = ArgumentParser()
    argparser.add_argument(
        "-p", "--ppath", type=str
    )
    argparser.add_argument(
        "-o", "--ovhpath", type=str
    )
    args = argparser.parse_args()

    for origin_path, destination_path in MAPPING.items():
        import os
        opath = os.path.join(args.ppath, origin_path)
        dpath = os.path.join(args.ovhpath, destination_path)
        shutil.copy(opath, dpath)
