# Single-drone Orienteering Aisle-graph Problem (SOAP) repository

This GitHub repository hosts the code implementation for the research paper titled "[Drone-based Bug Detection in Orchards with Nets: A Novel Orienteering Approach](https://dx.doi.org/10.1145/3653713)" recently published at ACM Transactions on Sensor Networks (TOSN): an extended version of the original paper "[Drone-based Optimal and Heuristic Orienteering Algorithms Towards Bug Detection in Orchards](https://ieeexplore.ieee.org/document/9881776)" presented at 18th Annual International Conference on Distributed Computing in Sensor Systems (DCOSS 2022).

## Abstract
The use of drones for collecting information and detecting bugs in orchards covered by nets is a challenging problem. 
The nets help in reducing pest damage, but they also constrain the drone's flight path, making it longer and more complex. 
To address this issue, we model the orchard as an aisle-graph, a regular data structure that represents consecutive aisles where trees are arranged in straight lines. 
The drone flies close to the trees and takes pictures at specific positions for monitoring the presence of bugs, but its energy is limited, so it can only visit a subset of positions. 
To tackle this challenge, we introduce the Single-drone Orienteering Aisle-graph Problem (SOAP), a variant of the orienteering problem, where likely infested locations are prioritized by assigning them a larger profit. 
Additionally, the drone's movements have a cost in terms of energy, and the objective is to plan a drone's route in the most profitable locations under a given drone's battery. 
We show that SOAP can be optimally solved in polynomial time, but for larger orchards/instances, we propose faster approximation and heuristic algorithms.
Finally, we evaluate the algorithms on synthetic and real data sets to demonstrate their effectiveness and efficiency.

## Key Contributions

:white_check_mark: We introduce a novel graph-based 3D data structure called 3D single-access aisle-graph, briefly orchard, that models the mobility of drones inside orchards with nets. The vertices of the
graph are weighted with a profit value which is based on the suggestions of entomologists and historical data.

:white_check_mark: We propose an optimization problem, called Single-drone Orienteering Aisle-graph Problem (SOAP), in which a single drone is in charge of planning an energy-feasible route inside an orchard in order to maximize the total collected profit.

:white_check_mark: We design five algorithms to solve SOAP, i.e., a dynamic programming-based optimal algorithm (OPT), two approximation algorithms (ABP and ABA), as well as two fast heuristics (GBT+ and GBA+)

:white_check_mark: We assess the effectiveness of our algorithms by testing them on both synthetic and real-world data, tailored to our specific problem.)

## Repository Contents

- `/code`: the folder contains all the Python scripts written for interacting with the algorithms depicited in the paper
  -  `/dump`: the folder contains all the running instances serialized in a dump file
  -  `/orchards`: the folder contains all the running instances in a human-like file, i.e., text file
  -  `/result`: the folder gathers the results of the execution run through the library
  - `/main.py`: the script reports the most relevant function to execute and run the algorithms on the different work package (W1, W2, and W3)
  - `/test.py`: the script provides the function's calls for executing the experiment and formatting the results obtained
  - `/aisle.py`: the script provides the function's calls needed to generate the problem instances
  - `/algorithms.py`: the script provides the function's calls required to run the different algorithms defined in the TOSN paper (the functions work like a wrapper fo the C++ code)
-  `/ccp`: the folder contains the true implementation of the algorithms in C++ code
  - `/orchards`: the folder contains the problem instances converted in format suitable for C++ code

**Remember:** put inside the code directory the C++ compiled file; the name must be `cpp.exe`.

## Python Libraries Required
```
numpy
pandas
sympy
statistics
copy
time
pickle
scipy
subprocess
```

## Run Example

To get started with using the codebase and exploring the algorithms proposed in the MDMP paper:

1. Clone this repository: `git clone https://github.com/TheAnswer96/TOSN_SOAP.git`.
2. Install the required libraries cited into the above section.
3. Uncomment one or more code example written in the `main.py` script.
4. Run the `main.py` script.

## Citation

If you find this work useful in your research, please consider citing the following paper:

```
@article{10.1145/3653713,
author = {Sorbelli, Francesco Betti and Cor\`{o}, Federico and Das, Sajal K. and Palazzetti, Lorenzo and Pinotti, Cristina M.},
title = {Drone-based Bug Detection in Orchards with Nets: A Novel Orienteering Approach},
year = {2024},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
issn = {1550-4859},
url = {https://doi.org/10.1145/3653713},
doi = {10.1145/3653713},
abstract = {The use of drones for collecting information and detecting bugs in orchards covered by nets is a challenging problem. The nets help in reducing pest damage, but they also constrain the drone’s flight path, making it longer and more complex. To address this issue, we model the orchard as an aisle-graph, a regular data structure that represents consecutive aisles where trees are arranged in straight lines. The drone flies close to the trees and takes pictures at specific positions for monitoring the presence of bugs, but its energy is limited, so it can only visit a subset of positions. To tackle this challenge, we introduce the Single-drone Orienteering Aisle-graph Problem (SOAP), a variant of the orienteering problem, where likely infested locations are prioritized by assigning them a larger profit. Additionally, the drone’s movements have a cost in terms of energy, and the objective is to plan a drone’s route in the most profitable locations under a given drone’s battery. We show that SOAP can be optimally solved in polynomial time, but for larger orchards/instances, we propose faster approximation and heuristic algorithms. Finally, we evaluate the algorithms on synthetic and real data sets to demonstrate their effectiveness and efficiency.},
note = {Just Accepted},
journal = {ACM Trans. Sen. Netw.},
month = {mar},
keywords = {Aisle-graph, Drones, Orchard, Bug detection, Approximation algorithms}
}
```
You can find our paper here:

["Francesco Betti Sorbelli, Federico Corò, Sajal K. Das, Lorenzo Palazzetti, Cristina M. Pinotti. 'Drone-based Bug Detection in Orchards with Nets: A Novel Orienteering Approach'. ACM Trans. Sen. Netw., 2024."](https://dl.acm.org/doi/10.1145/3653713)

## Contact Us

For any inquiries or feedback regarding the code or the research, please feel free to contact [Lorenzo Palazzetti](lorenzo.palazzetti@unifi.it), [Francesco Betti Sorbelli](francesco.bettisorbelli@unipg.it), or [Federico Corò](federico.coro@unipd.it).
