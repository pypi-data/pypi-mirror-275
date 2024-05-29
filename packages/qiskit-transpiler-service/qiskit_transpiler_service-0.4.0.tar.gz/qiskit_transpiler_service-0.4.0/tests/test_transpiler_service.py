# -*- coding: utf-8 -*-

# (C) Copyright 2023 IBM. All Rights Reserved.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Unit-testing Transpiler Service"""

import logging

import pytest
from qiskit import QuantumCircuit, qasm2
from qiskit.circuit.library import QuantumVolume
from qiskit.circuit.random import random_circuit

from qiskit_transpiler_service.transpiler_service import TranspilerService

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@pytest.mark.parametrize(
    "optimization_level", [1, 2, 3], ids=["opt_level_1", "opt_level_2", "opt_level_3"]
)
@pytest.mark.parametrize("ai", [False, True], ids=["no_ai", "ai"])
@pytest.mark.parametrize(
    "qiskit_transpile_options",
    [None, {"seed_transpiler": 0}],
    ids=["no opt", "one option"],
)
def test_rand_circ_backend_routing(optimization_level, ai, qiskit_transpile_options):
    backend_name = "ibm_brisbane"
    random_circ = random_circuit(5, depth=3, seed=42)

    cloud_transpiler_service = TranspilerService(
        backend_name=backend_name,
        ai=ai,
        optimization_level=optimization_level,
        qiskit_transpile_options=qiskit_transpile_options,
    )
    transpiled_circuit = cloud_transpiler_service.run(random_circ)

    assert isinstance(transpiled_circuit, QuantumCircuit)


@pytest.mark.parametrize(
    "optimization_level", [1, 2, 3], ids=["opt_level_1", "opt_level_2", "opt_level_3"]
)
@pytest.mark.parametrize("ai", [False, True], ids=["no_ai", "ai"])
@pytest.mark.parametrize(
    "qiskit_transpile_options",
    [None, {"seed_transpiler": 0}],
    ids=["no opt", "one option"],
)
def test_qv_backend_routing(optimization_level, ai, qiskit_transpile_options):
    backend_name = "ibm_brisbane"
    qv_circ = QuantumVolume(27, depth=3, seed=42).decompose(reps=3)

    cloud_transpiler_service = TranspilerService(
        backend_name=backend_name,
        ai=ai,
        optimization_level=optimization_level,
        qiskit_transpile_options=qiskit_transpile_options,
    )
    transpiled_circuit = cloud_transpiler_service.run(qv_circ)

    assert isinstance(transpiled_circuit, QuantumCircuit)


@pytest.mark.parametrize(
    "coupling_map",
    [
        [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],
        [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],
    ],
)
@pytest.mark.parametrize("optimization_level", [1, 2, 3])
@pytest.mark.parametrize("ai", [False, True], ids=["no_ai", "ai"])
@pytest.mark.parametrize("qiskit_transpile_options", [None, {"seed_transpiler": 0}])
def test_rand_circ_cmap_routing(
    coupling_map, optimization_level, ai, qiskit_transpile_options
):
    random_circ = random_circuit(5, depth=3, seed=42).decompose(reps=3)

    cloud_transpiler_service = TranspilerService(
        coupling_map=coupling_map,
        ai=ai,
        optimization_level=optimization_level,
        qiskit_transpile_options=qiskit_transpile_options,
    )
    transpiled_circuit = cloud_transpiler_service.run(random_circ)

    assert isinstance(transpiled_circuit, QuantumCircuit)


def test_qv_circ_several_circuits_routing():
    qv_circ = QuantumVolume(5, depth=3, seed=42).decompose(reps=3)

    cloud_transpiler_service = TranspilerService(
        backend_name="ibm_brisbane",
        ai=True,
        optimization_level=1,
    )
    transpiled_circuit = cloud_transpiler_service.run([qv_circ] * 2)
    for circ in transpiled_circuit:
        assert isinstance(circ, QuantumCircuit)

    transpiled_circuit = cloud_transpiler_service.run([qasm2.dumps(qv_circ)] * 2)
    for circ in transpiled_circuit:
        assert isinstance(circ, QuantumCircuit)

    transpiled_circuit = cloud_transpiler_service.run([qasm2.dumps(qv_circ), qv_circ])
    for circ in transpiled_circuit:
        assert isinstance(circ, QuantumCircuit)


def test_qv_circ_wrong_input_routing():
    qv_circ = QuantumVolume(5, depth=3, seed=42).decompose(reps=3)

    cloud_transpiler_service = TranspilerService(
        backend_name="ibm_brisbane",
        ai=True,
        optimization_level=1,
    )

    circ_dict = {"a": qv_circ}
    with pytest.raises(TypeError):
        cloud_transpiler_service.run(circ_dict)
