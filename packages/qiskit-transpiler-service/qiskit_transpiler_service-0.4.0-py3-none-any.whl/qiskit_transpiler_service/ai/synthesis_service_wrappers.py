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

import logging
import os
from typing import Union

import requests
from qiskit import QuantumCircuit
from qiskit.circuit.library import LinearFunction
from qiskit.quantum_info import Clifford

from .service_wrapper import AIService

logging.basicConfig()
logging.getLogger(__name__).setLevel(logging.INFO)


class CliffordAIService(AIService):
    """A helper class that covers some basic funcionality from the Clifford AI Synthesis service"""

    def __init__(self, url: str = None, token: str = None):
        # If it does not recive URL or token, the function tries to find your Qiskit
        # token from the QISKIT_IBM_TOKEN env var
        # If it couldn't find it, it will try to get it from your ~/.qiskit/qiskit-ibm.json file
        # If it couldn't find it, it fails

        if url is None:
            url = os.environ.get(
                "CLIFFORDAI_URL",
                "https://cloud-transpiler.quantum.ibm.com/clifford/",
            )

        super().__init__(url, token)

    def transpile(
        self,
        circuits: list[Union[QuantumCircuit, Clifford]],
        backend: str,
        qargs: list[list[int]],
    ):
        transpile_resps = self.request_and_wait(
            endpoint="transpile",
            body={
                "clifford_dict": [Clifford(circuit).to_dict() for circuit in circuits],
                "qargs": qargs,
            },
            params={"backend": backend},
        )

        results = []
        for transpile_resp in transpile_resps:
            if transpile_resp.get("success") and transpile_resp.get("qasm") is not None:
                results.append(QuantumCircuit.from_qasm_str(transpile_resp.get("qasm")))
            else:
                results.append(None)
        return results


class LinearFunctionAIService(AIService):
    """A helper class that covers some basic funcionality from the Linear Function AI Synthesis service"""

    def __init__(self, url: str = None, token: str = None):
        if url is None:
            url = os.environ.get(
                "LINEARFUNCTIONAI_URL",
                "https://cloud-transpiler.quantum.ibm.com/linear_functions/",
            )
        super().__init__(url, token)

    def transpile(
        self,
        circuits: list[Union[QuantumCircuit, LinearFunction]],
        backend: str,
        qargs: list[list[int]],
    ):
        transpile_resps = self.request_and_wait(
            endpoint="transpile",
            body={
                "clifford_dict": [Clifford(circuit).to_dict() for circuit in circuits],
                "qargs": qargs,
            },
            params={"backend": backend},
        )

        results = []
        for transpile_resp in transpile_resps:
            if transpile_resp.get("success") and transpile_resp.get("qasm") is not None:
                results.append(QuantumCircuit.from_qasm_str(transpile_resp.get("qasm")))
            else:
                results.append(None)
        return results


class PermutationAIService(AIService):
    """A helper class that covers some basic funcionality from the Permutation AI Synthesis service"""

    def __init__(self, url: str = None, token: str = None):
        if url is None:
            url = os.environ.get(
                "PERMUTATIONAI_URL",
                "https://cloud-transpiler.quantum.ibm.com/permutations/",
            )

        super().__init__(url, token)

    def transpile(
        self,
        patterns: list[list[int]],
        backend: str,
        qargs: list[list[int]],
    ):
        transpile_resps = self.request_and_wait(
            endpoint="transpile",
            body={"permutation": patterns, "qargs": qargs},
            params={"backend": backend},
        )

        results = []
        for transpile_resp in transpile_resps:
            if transpile_resp.get("success") and transpile_resp.get("qasm") is not None:
                results.append(QuantumCircuit.from_qasm_str(transpile_resp.get("qasm")))
            else:
                results.append(None)
        return results
