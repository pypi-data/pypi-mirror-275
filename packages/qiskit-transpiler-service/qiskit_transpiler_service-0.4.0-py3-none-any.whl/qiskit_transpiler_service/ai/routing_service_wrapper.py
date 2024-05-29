import logging
import os

from qiskit import QuantumCircuit, qasm2, qasm3
from qiskit.qasm2 import QASM2ExportError

from .service_wrapper import AIService

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class AIRoutingService(AIService):
    """A helper class that covers some basic funcionality from the AIRouting plugin"""

    def __init__(self, url: str = None, token: str = None):
        if url is None:
            url = os.environ.get(
                "ROUTINGAI_URL",
                "https://cloud-transpiler.quantum.ibm.com/routing/",
            ).rstrip("/")

        super().__init__(url, token)

    def routing(
        self,
        circuit: QuantumCircuit,
        coupling_map,
        optimization_level: int = 1,
        check_result: bool = False,
        layout_mode: str = "OPTIMIZE",
    ):
        is_qasm3 = False
        try:
            qasm = qasm2.dumps(circuit)
        except QASM2ExportError:
            qasm = qasm3.dumps(circuit)
            is_qasm3 = True

        json_args = {"qasm": qasm.replace("\n", " "), "coupling_map": coupling_map}

        params = {
            "check_result": check_result,
            "layout_mode": layout_mode,
            "optimization_level": optimization_level,
        }

        routing_resp = self.request_and_wait(
            endpoint="routing", body=json_args, params=params
        )

        if routing_resp.get("success"):
            routed_circuit = (
                qasm3.loads(routing_resp["qasm"])
                if is_qasm3
                else QuantumCircuit.from_qasm_str(routing_resp["qasm"])
            )
            return (
                routed_circuit,
                routing_resp["layout"]["initial"],
                routing_resp["layout"]["final"],
            )
