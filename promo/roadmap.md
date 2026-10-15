# Roadmap: the path to the opencircuitlab Target

This is the path, not the code. Each milestone says what you learn, what you build, and how you know it works. Pick one and open a pull request. See [CONTRIBUTING.md](../CONTRIBUTING.md).

## Session 4: Read a netlist

**You will learn:** How circuit simulators describe a circuit as lines of text (name, two nodes, value) and how to parse them.

**You will build:** A function that reads lines such as 'R1 1 2 1k' and 'V1 1 0 12' and returns the input of the solver.

**Checkpoint (not met by the shipped code):** The text form of the Session 2 two-loop circuit gives V_A = 6.545 V (the shipped solver only accepts Python lists of tuples), including 'k' and 'm' value suffixes.

**Difficulty:** beginner

## Session 5: A nonlinear part: the diode

**You will learn:** Why a diode breaks G v = i, and how Newton's method repeats a linear solve until KCL holds.

**You will build:** A diode stamp linearised at each iteration, solved inside a loop around the nodal solver.

**Checkpoint (not met by the shipped code):** A 5 V source, a 1 kohm resistor and a diode converge to a KCL residual below 1e-9 A in at most 10 iterations (the shipped solver is linear and cannot represent a diode at all).

**Difficulty:** intermediate

## Session 6: An amplifier from a controlled source

**You will learn:** Dependent sources and the ideal operational amplifier as a very high gain voltage-controlled source.

**You will build:** A controlled-source stamp and an inverting amplifier built with it.

**Checkpoint (not met by the shipped code):** An inverting amplifier with Rf = 10 kohm and Rin = 1 kohm gives a gain within 0.1 percent of -10 (the shipped solver has only resistors and independent sources).

**Difficulty:** intermediate

## Session 7: Sensitivity without Monte Carlo

**You will learn:** How the adjoint idea gives the derivative of an output with respect to every resistor from a single extra solve.

**You will build:** A function returning dVout/dR for every resistor of any network.

**Checkpoint (not met by the shipped code):** For the Wheatstone bridge all four sensitivities match finite differences to 1e-6 relative error, and the predicted spread for 5 percent parts is within 1 percent of the 20000-draw Monte Carlo value (shipped: 20000 solves; the shipped prediction only handles four equal resistors).

**Difficulty:** advanced

## Session 8: Time enters: the RC circuit

**You will learn:** Capacitors as time-dependent stamps and the backward Euler step.

**You will build:** A transient solver for a resistor and a capacitor on a step input.

**Checkpoint (not met by the shipped code):** The time to reach 63.2 percent of the final voltage is within 1 percent of R C for a stable time step (the shipped solver has no time at all).

**Difficulty:** advanced

## The final step

Combine the milestones: read a netlist from a text file, sweep one component, and export an animated schematic that shows every node voltage, every branch current and the Thevenin load line of a chosen port, like the Target animation. If your result looks like the Target, open a pull request and tell us how you did it.
