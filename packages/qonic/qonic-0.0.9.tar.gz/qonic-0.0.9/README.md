[![Python application](https://github.com/Qonic-Team/qonic/actions/workflows/python-app.yml/badge.svg)](https://github.com/Qonic-Team/qonic/actions/workflows/python-app.yml)
[![CodeQL](https://github.com/Qonic-Team/qonic/actions/workflows/codeql.yml/badge.svg)](https://github.com/Qonic-Team/qonic/actions/workflows/codeql.yml)
<sup>[`Snyk Vulnerability Report`](https://snyk.io/test/github/Qonic-Team/qonic?targetFile=source_dir/requirements.txt)</sup>

# qonic
The Qonic project is an open source, expandable framework for solving problems using hybrid quantum computing solutions.  The base library includes tools for defining optimization problems to be run on gate quantum computers on a variety of backends or simulators, as well as on simulated or physical quantum annealers.

**To install:** `pip3 install qonic`

## QProgram
Framework for defining quantum programs with the following components:

* `skip`: corresponds to an operation that does nothing
* `q := 0` (constructor): sets the initial states of individual qubits
* `assign`: corresponds to applying a unitary operator to a set of qubits, ie. `q̅ := U q̅`
* `measurement`: corresponds to a measurement on a set of qubits, returning the measured result as a set of classical bits
* `while_loop`: corresponds to applying a sub algorithm to the quantum register while a specified qubit is measured to be equal to a specified classical bit
* A method for evaluating the correctness of a quantum program using Quantum Hoare Logic (QHL)

For more information on the specifics of how these components are implimented, see the [Qonic QHL Notes](https://github.com/Qonic-Team/qonic-QHoare-logic/blob/main/QHL.ipynb).
### _`class`_`QProgram`
**Initialization**
* `QProgram(q̅=[[1, 0]], backend=None)`

  **Description:**
  
  Declare a new QProgram object with quantum register `q̅`.  By default, the register will consist of one qubit intialized to the state [1, 0] (ie. $\ket{0}$).  Registers with multiple qubits can be initialized by passing a vecor encompassing the entire state of the register (eg. [1,0,0,0] = $\ket{00}$), or by passing a list of single qubit states (eg. [[1, 0], [1, 0]]).

  **Parameters:**
  * `q̅ <type 'list'>`: vector corresponding to quantum state that the register is initialized to
  * `backend [qiskit | tequila]`: the default backend used to compile quantum programs to quantum circuits.  The options are:
    * [Qiskit](https://github.com/Qiskit/qiskit)
    * [Tequila](https://github.com/tequilahub/tequila)

**Methods**
* `skip()`

  **Description:**
  
  This function does nothing and corresponds to the `skip` component of the quantum program grammar

* `assign(U, variables)`

  **Description:**
  
  This function corresponds to applying a unitary operator to a set of qubits, ie. q̅ := U q̅ where q̅ is a subset of the quantum register and U is a unitary operator

  **Parameters:**
  * `U <type 'np.ndarray'>`: unitary operator to be applied to the specified qubits.  The np array storing the operator should have the dimensions(2^num_qubits × 2^num_qubits) and must be unitary
  * `variables <type 'list'>`: list of qubit indices specifying which qubits to apply the operator to

  **Example:**
  ```py
  >>> S = qonic.QProgram(q̅=[[1,0],[0,1],[0,1],[1,0]]) # initial register state 0, 1, 1, 0
  >>> CNOT = np.array([[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,0,0]]) # controlled not gate
  >>> H = np.array([[1/sqrt(2), 1/sqrt(2)],[1/sqrt(2), -1/sqrt(2)]]) # hadamard gate
  >>> S.assign(H, [0]) # assign a hadamard gate on qubit 0
  >>> S.assign(CNOT, [1,3]) # assign a controlled not gate on qubits 1 and 3
  ```

* `measure(q_m)`

  **Description:**
  
  This function corresponds to measuring a set of qubits.  In addition to this, the function modifies the state of the register to be the state after wavefunction collapse, and clears the previous instructions (reflecting that measurements are non unitary)

  **Parameters:**
  * `q_m <type 'list'>`: list of qubit indices specifying which qubits to measure

  **Example:**
  ```python
  >>> S.measure([0, 1]) # measure the qbits 0 and 1
  '11'
  >>> # notice that the output of the measurement is a classical binary state
  ```

* `while_loop_body(q_m, expected_measurement, sub_algorithm, prob_threshold=0.01, iter_cutoff=10)`

  **Description:**
  
  This function corresponds to applying a sub algorithm to the quantum register while a specified qubit is measured to be equal to a specified classical bit. This is done using the principle or deferred measurements. In other words, the sub algorithm is treated as a controlled gate added to the instructions with the control qubit being the passed loop conditional qubit. The gate is applied repeatedly until the probability of the loop conditional being true is less than an arbitrary threshold (or until some maximum number of iterations is reached)

  **Parameters:**
  * `q_m <type 'list'>`: list of qubit indices specifying the conditional qubits
  * `expected_measurement <type 'string'>`: classical binary state that measurements of the conditional qubits are compared against
  * `sub_algorithm <type 'qonic.QProgram'>`: a separate sub algorithm QProgram object that is run on the quantum register each iteration
  * `prob_threshold <type 'float'>`: the minimum probability threshold for the expected measurement.  Once this threshold is reached, deferred measurements stop being applied
  * `iter_cutoff <type 'int'>`: the maximum number of iterations.  Once this cutoff is reached, deferred measurements stop being applied

  **Example:**
  ```python
  >>> # testing the while_loop_body operation
  >>> S = QProgram(q̅=[[0,1],[0,1]])
  >>> S.assign(H, [0])
  >>> S.assign(H, [1]) # put the two qubits in a superposition
  >>>
  >>> sub_algorithm = QProgram(q̅=[[0,1],[0,1]]) # define a sub algorithm that applies an X gate while qubit 0 is measured to be 1
  >>> X = np.array([[0, 1], [1, 0]])
  >>> sub_algorithm.assign(X, [1])
  >>>
  >>> S.while_loop_body([0], '1', sub_algorithm) # apply the sub algorithm while qubit 0 is measured to be '1'
  array([ 1.38777878e-16+0.5j,  0.00000000e+00-0.5j, -5.55111512e-17-0.5j, 0.00000000e+00+0.5j])
  >>> # returns the final state after the while loop
  ```

* `to_circuit(framework='tequila')`

  **Description:**
  
  This function converts the current QProgram into a quantum circuit in the Qiskit or Tequila frameworks.  Once converted to a circuit, the QProgram can be simulated or run on physical quantum libraries within these frameworks
  
  **Parameters:**
  * `framework [qiskit | tequila]`: specifies if the returned circuit should be in the Qiskit or Tequila framework

  **Example:**
  ```python
  >>> S.to_circuit(framework='tequila')
  circuit: 
  Rz(target=(0,), parameter=0.0)
  Rx(target=(0,), parameter=1.5707963267948966)
  ...
  Rx(target=(2,), parameter=-1.5707963267948966)
  Rz(target=(2,), parameter=2.5262611)
  >>> S.to_circuit(framework='qiskit')
  <qiskit.circuit.quantumcircuit.QuantumCircuit at 0x7f3348237ab0>
  ```

* `to_unitary()`
  
  **Description:**
  
  This function returns the instructions stored in the current QProgram as a single unitary matrix

  **Example:**
  ```python
  >>> S = QProgram(q̅=[[1,0],[0,1]])
  >>> S.assign(H, [0])
  >>> S.assign(CNOT, [0,1])
  >>> S.to_unitary()
  array([[ 0.70710678+0.j,  0.70710678+0.j,  0.        +0.j,  0.        +0.j],
         [ 0.        +0.j,  0.        +0.j,  0.70710678+0.j, -0.70710678+0.j],
         [ 0.        +0.j,  0.        +0.j,  0.70710678+0.j,  0.70710678+0.j],
         [ 0.70710678+0.j, -0.70710678+0.j,  0.        +0.j,  0.        +0.j]])
  ```

* `to_superop()`
  
  **Description:**
  
  This function returns the super operator form of the current QProgram

  **Example:**
  ```python
  >>> S = QProgram(q̅=[[1,0],[0,1]])
  >>> S.assign(H, [0])
  >>> S.assign(CNOT, [0,1])
  >>> S.to_superop()
  array([[ 0.5+0.j,  0.5+0.j,  0. +0.j,  0. +0.j,  0.5+0.j,  0.5+0.j,
           0. +0.j,  0. +0.j,  0. +0.j,  0. +0.j,  0. +0.j,  0. +0.j,
  ...
           0. +0.j,  0. +0.j,  0. +0.j,  0. +0.j,  0. +0.j,  0. +0.j,
           0. +0.j,  0. +0.j,  0. +0.j,  0. +0.j]])
  ```

* `correct_q_hoare_triple(Q, P)`
  
  **Description:**
  
  Hoare Logic is a logical system for reasoning about the correctness of computer programs developed by C. A. R. Hoare. Correctness is determined with respect to assertion *P* about the initial state of the computation, and assertion *Q* about the final state. If a program *S* runs when *P* holds and this establishes *Q*, it is said to be correct with respect to P and Q. This is expressed using a **Hoare Triple** as follows:

  *{P}S{Q}*

  where *P* is called the precondition and *S* is called the postcondition. Quantum Hoare Logic (QHL) extends this concept to quantum programs. This has the potential to allow for rigorous reasoning about the correctness of quantum programs. In QHL, the precondition and postcondition are not assertions but quantum predicates, represented by physical observables. This function determines if a given Quantum Hoare Triple *{P}S{Q}* is correct, where *P* and *Q* are observables and *S* is a QProgram object. For a technical explanation of this function and a description of possible use cases, see the [Qonic QHL notebook](https://github.com/Qonic-Team/qonic-QHoare-logic/blob/main/QHL.ipynb). In its current implementation, this function serves as a proof of concept. It evaluates the correctness of simple programs but quickly becomes intractable as the number of qubits in the register grows.

  **Parameters:**
  * `Q <type 'np.ndarray'>`: the postcondition observable
  * `P <type 'np.ndarray'>`: the precondition observable

  **Example:**
  ```python
  >>> # calculate if we have a valid QHoare triple
  >>> S.correct_q_hoare_triple(Q, P)
  True
  ```

## ConstraintSatisfaction
Constraint satisfaction is the process of finding a configuration of variables that satisfy a set of constraints imposed on those variables.  The `ConstraintSatisfactionProblem` class allows for mapping constraints from a CSP onto a binary quadratic model (BQM).  Once formulated as a BQM, a valid configuration can be searched for by using simulated or quantum annealing algorithms.
### _`class`_`ConstraintSatisfactionProblem`
**Methods**  
* `fromStr(constraint, binary, real, complx)`

  **Description:**
  
  This function adds a constraint to the current CSP object from a string.  The constraint string can be made up of:
  * variables
    * these can be binary bits, or 16 bit real floats, or 32 bit complex floats.  Note that the float variables are are not technically represented with floats, but rather approximations constructed from binary polynomial sentences.  This is done so that the variables can be broken up and converted into a BQM
    * ⚠️ NOTE: variables can have any name that does not contain spaces or special characters (eg ! - / etc), with the exception of names of the form `f[number]` or `j[number]` (eg `'f12'`, `'j51.34'`) as these are special names reserved for use by the constraint parser
  * binary operations `and`, `or`, `not` applied to binary variables and relational operators `==` and `!=` for requiring two terms to be equal or not equal respectively
  * polynomial expressions constructed from variables 
    * terms can be combined with `+` and `-` operations
    * coefficients can be combined with `*` and `/` operations
    * terms can be raised to a given (integer) power using `**`
    * terms can be grouped using parentheses 
    * relational operators `==`, `!=`, `<`, `<=`, `>`, `>=` can be used to require one expression to be equal to, not equal to, less than, less than or equal to, greater than, or greater than or equal to another expression.

  **Parameters:**
  * `constraint <type 'string'>`: a single string storing a constraint expression (see above description for formatting)
  * `binary <type 'list'>`: a list of the binary variables used in the constraint (variable names stored in strings)
  * `real <type 'list'>`: a list of the real 16 bit float variables used in the constraint (variable names stored in strings)
  * `complx <type 'list'>`: a list of the complex 32 bit float variables used in the constraint (variable names stored in strings)

  **Example:**
  ```python
  >>> CSP = qonic.ConstraintSatisfactionProblem()
  >>> # add a new constraint on binary variable 'd', 16 bit floats 'a' and 'b', and 32 bit complex float 'c'
  >>> CSP.fromStr('a * b > c**2 or d', ['d'], ['a', 'b'], ['c'])
  ```

* `fromFile(filename)`

  **Description:**
  
  This function adds constraint(s) to the current CSP object from a yaml file.  The yaml file should have the following structure:
  * `constraint0`: the first constraint stored in a string
  * `constraint1`: the second constraint stored in a string
    
   ⋮
  
  * `constraintN`: the (N-1)th constraint stored in a string.  Note that the constraints can use any key within the file as long as `constraint` is contained within it
  * `binary`: a list of the binary variables used in the constraint (variable names stored in strings)
  * `real`: a list of the real 16 bit float variables used in the constraint (variable names stored in strings)
  * `complx`: a list of the complex 32 bit float variables used in the constraint (variable names stored in strings)

  **Parameters:**
  * `filename <type 'string'>`: the path to the file location of the yaml file storing the constraints

  **Example:**
  * example `constraints.yaml` file:
    ```yaml
    # first the constraints
    constraint0: "a * b > c**2 or d"
    my_constraint: "a**3 > 1 and e"
    another_constraint: "d == e"

    # now specify the variables
    binary: ["d", "e"]
    real: ["a", "b"]
    complx: ["c"]
    ```
  * example python script:
    ```python
    >>> CSP = qonic.ConstraintSatisfactionProblem()
    >>> # add a new constraint from a yaml file
    >>> CSP.fromFile('constraints.yaml')
    ```

* `toQUBO()`

  **Description:**
  
  This function returns the constraints in the form of a quadratic unconstrained binary optimization problem (or QUBO)

  **Returns:**
  * `({(vars): biases}, offset) <type 'tuple'>`: a tuple containing the biases between variables as a dictionary, and the offset of the QUBO

  **Example:**
  ```python
  >>> self.toQUBO()
  ({('b0', 'b1'): -3.9999999991051727, ('b0', 'b0'): 1.999999998686436, ('b1', 'b1'): 1.9999999986863806}, 8.661749095750793e-10)
  ```

* `checkConfiguration(configuration, err=0.0)`

  **Description:**
  
  This function takes a dictionary of values of variables and returns the number of constraints satisfied by the configuration (within a margin of error specified in err)

  **Parameters:**
  * `configuration <type 'dict'>`: the configuration of variables stored in a dictionary of the form `{'variable': value}`
  * `err <type 'float'>`: the margin of error when checking constraints with relational operators `==`, `!=`, `<`, `<=`, `>`, `>=`

  **Returns:**
  * `constraintsMet <type 'int'>`: the number of constraints within the CSP that are satisfied by the passed configuration

  **Example:**
  ```python
  >>> self.fromString('(a or b) and c', ['a', 'b', 'c'], [], [])
  >>> self.checkConfiguration({'a': 1, 'b': 0, 'c': 1}, 0.1) # should return that 1 constraint is satisfied by this configuration
  1
  ```

**Attributes**
* `__b <type 'dict'>`: a dictionary storing a list of binary variables and the corresponding names
* `__f <type 'dict'>`: a dictionary storing the binary polynomial expressions approximating 16 bit real floats (stored as strings) and the corresponding float variable names
* `__j <type 'dict'>` a dictionary storing the binary polynomial expressions approximating 32 bit complex floats (stored as strings) and the corresponding float variable namesu
