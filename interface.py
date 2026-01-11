"""Formatage des résultats pour affichage console ou API."""

from __future__ import annotations

from typing import Dict


def format_summary(result: Dict) -> str:
	lines = []
	profiles = result.get("profiles", {})
	total = result.get("total", {})

	lines.append("Profil       |   req |   in_tok_tot |  out_tok_tot |    kWh |   CO2 kg")
	lines.append("-" * 78)

	for name, data in profiles.items():
		lines.append(
			f"{name.capitalize():<12} | {data['requests']:>6} | {data['input_tokens_total']:>12.0f} | {data['output_tokens_total']:>12.0f} | {data['energy_kwh']:.4f} | {data['co2_kg']:.4f}"
		)

	lines.append("-" * 78)
	lines.append(
		f"Total        | {total.get('requests', 0):>6} | {total.get('input_tokens', 0):>12.0f} | {total.get('output_tokens', 0):>12.0f} | {total.get('energy_kwh', 0):.4f} | {total.get('co2_kg', 0):.4f}"
	)

	char_per_token = result.get("char_per_token")
	if char_per_token is not None:
		lines.append(f"Hypothèse char/token : {char_per_token}")

	return "\n".join(lines)


__all__ = ["format_summary"]
