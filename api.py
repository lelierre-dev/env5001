"""Point d'entrée CLI pour lancer les calculs."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from interface import format_summary
from traitement import EnergyCalculator


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description="Calcule l'énergie/CO2 des profils IA")
	parser.add_argument("--config", default="config/config.yaml", help="Chemin du fichier de configuration basique")
	parser.add_argument(
		"--model-config", default="config/config_model.yaml", help="Chemin du fichier de paramètres modèles"
	)
	parser.add_argument("--json", action="store_true", help="Retourne le résultat en JSON brut")
	return parser.parse_args()


def main() -> None:
	args = parse_args()
	calculator = EnergyCalculator(config_path=Path(args.config), model_config_path=Path(args.model_config))
	result = calculator.compute()

	if args.json:
		print(json.dumps(result, indent=2))
	else:
		print(format_summary(result))


if __name__ == "__main__":
	main()


