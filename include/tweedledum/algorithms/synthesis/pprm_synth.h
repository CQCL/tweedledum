/*------------------------------------------------------------------------------
| Part of tweedledum.  This file is distributed under the MIT License.
| See accompanying file /LICENSE for details.
*-----------------------------------------------------------------------------*/
#pragma once

#include "../../ir/Circuit.h"
#include "../../ir/GateLib.h"
#include "../../ir/Operand.h"

#include <cassert>
#include <kitty/kitty.hpp>
#include <vector>

namespace tweedledum {

using TruthTable = kitty::dynamic_truth_table;

inline void pprm_synth(Circuit& circuit, std::vector<Operand> const& qubits,
    TruthTable const& function)
{
	uint32_t const num_controls = function.num_vars();
	assert(qubits.size() >= (num_controls + 1u));

	Operand const target = qubits.back();
	std::vector<Operand> controls;
	controls.reserve(num_controls);
	for (auto const& cube : kitty::esop_from_pprm(function)) {
		auto bits = cube._bits;
		for (uint32_t v = 0u; bits; bits >>= 1, ++v) {
			if ((bits & 1) == 0u) {
				continue;
			}
			controls.push_back(qubits.at(v));
		}
		circuit.create_instruction(GateLib::X{}, controls, target);
		controls.clear();
	}
}

inline Circuit pprm_synth(TruthTable const& function)
{
	// TODO: method to generate a name;
	Circuit circuit("my_circuit");
	// Create the necessary qubits
	std::vector<Operand> operands;
	operands.reserve(function.num_vars());
	for (uint32_t i = 0u; i < function.num_vars() + 1; ++i) {
		operands.emplace_back(circuit.create_qubit());
	}
	pprm_synth(circuit, operands, function);
	return circuit;
}

} // namespace tweedledum