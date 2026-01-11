"""Cœur de calcul énergétique basé sur la nouvelle méthodologie.

Le module convertit des tailles de contenus en tokens, puis estime l'énergie
et les émissions par profil (translation, completion, chatbot) à partir des
hypothèses de puissance et de PUE fournies dans la configuration.
"""

from __future__ import annotations

import dataclasses
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import yaml


@dataclasses.dataclass
class ProfileConfig:
	name: str
	topic_size_chars: float
	prompt_size_chars: float
	avg_topics: float
	avg_prompts: float
	output_tokens_constant: Optional[float]
	output_tokens_factor: Optional[float]
	throughput_tokens_per_sec: float
	gpu_power_w: float
	cpu_power_w: float
	gpu_util: float
	cpu_util: float
	pue: float
	utilization_rate: float
	carbon_intensity_g_per_kwh: float

	@property
	def base_power_w(self) -> float:
		return (self.gpu_power_w * self.gpu_util) + (self.cpu_power_w * self.cpu_util)

	def estimate_tokens(self, char_per_token: float) -> Tuple[float, float]:
		topic_tokens = (self.topic_size_chars * self.avg_topics) / char_per_token
		prompt_tokens = (self.prompt_size_chars * self.avg_prompts) / char_per_token
		input_tokens = topic_tokens + prompt_tokens

		if self.output_tokens_constant is not None:
			output_tokens = self.output_tokens_constant
		elif self.output_tokens_factor is not None:
			output_tokens = self.output_tokens_factor * topic_tokens
		else:
			output_tokens = 0.0
		return input_tokens, output_tokens


class EnergyCalculator:
	def __init__(
		self,
		config_path: Path | str = Path("config/config.yaml"),
		model_config_path: Path | str = Path("config/config_model.yaml"),
	) -> None:
		self.config = self._load_yaml(config_path)
		self.model_config = self._load_yaml(model_config_path)
		self.char_per_token = float(self.model_config.get("char_per_token", 4.0))
		self.data_path = Path(self.config.get("data_path", "data/2025-FluidTopics-daily-analytics.yaml"))
		self.profiles = self._build_profiles(self.model_config.get("profiles", {}))

	@staticmethod
	def _load_yaml(path: Path | str) -> Dict:
		with Path(path).open("r", encoding="utf-8") as fh:
			return yaml.safe_load(fh) or {}

	def _build_profiles(self, raw: Dict[str, Dict]) -> Dict[str, ProfileConfig]:
		profiles: Dict[str, ProfileConfig] = {}
		for name, cfg in raw.items():
			profiles[name] = ProfileConfig(
				name=name,
				topic_size_chars=float(cfg.get("topic_size_chars", 0.0)),
				prompt_size_chars=float(cfg.get("prompt_size_chars", 0.0)),
				avg_topics=float(cfg.get("avg_topics", 1.0)),
				avg_prompts=float(cfg.get("avg_prompts", 0.0)),
				output_tokens_constant=cfg.get("output_tokens_constant"),
				output_tokens_factor=cfg.get("output_tokens_factor"),
				throughput_tokens_per_sec=float(cfg.get("throughput_tokens_per_sec", 1.0)),
				gpu_power_w=float(cfg.get("gpu_power_w", 0.0)),
				cpu_power_w=float(cfg.get("cpu_power_w", 0.0)),
				gpu_util=float(cfg.get("gpu_util", 0.0)),
				cpu_util=float(cfg.get("cpu_util", 0.0)),
				pue=float(cfg.get("pue", 1.0)),
				utilization_rate=float(cfg.get("utilization_rate", 1.0)),
				carbon_intensity_g_per_kwh=float(cfg.get("carbon_intensity_g_per_kwh", 0.0)),
			)
		return profiles

	def _load_usage(self) -> Dict[str, List[Dict[str, str]]]:
		data = self._load_yaml(self.data_path)
		genai = data.get("genai", {})
		return {
			"chatbot": genai.get("chatbots", []),
			"completion": genai.get("completions", []),
			"translation": genai.get("translations", []),
		}

	@staticmethod
	def _energy_from_profile(
		profile: ProfileConfig, input_tokens: float, output_tokens: float
	) -> Tuple[float, float]:
		throughput = profile.throughput_tokens_per_sec
		if throughput <= 0:
			raise ValueError(f"Throughput must be positive for profile {profile.name}")

		#t_prefill_s = (input_tokens ** 2) / throughput
		n_ref = 2048  # Référence pour la complexité quadratique
		t_prefill_s = (input_tokens**2) / (throughput * n_ref)
		t_decode_s = output_tokens / throughput
		t_compute_h = (t_prefill_s + t_decode_s) / 3600

		energy_wh = profile.base_power_w * t_compute_h * profile.pue * profile.utilization_rate
		energy_kwh = energy_wh / 1000
		co2_kg = energy_kwh * (profile.carbon_intensity_g_per_kwh / 1000)
		return energy_kwh, co2_kg

	def compute(self) -> Dict[str, Dict[str, float]]:
		"""Calcule énergie, CO2 et volumes de tokens par profil et au total."""

		usage = self._load_usage()
		result: Dict[str, Dict[str, float]] = {
			"profiles": {},
			"total": {"requests": 0, "energy_kwh": 0.0, "co2_kg": 0.0, "input_tokens": 0.0, "output_tokens": 0.0},
		}

		for profile_name, records in usage.items():
			if profile_name not in self.profiles:
				continue

			profile_cfg = self.profiles[profile_name]
			input_tokens_per_call, output_tokens_per_call = profile_cfg.estimate_tokens(self.char_per_token)
			energy_per_req_kwh, co2_per_req_kg = self._energy_from_profile(
				profile_cfg, input_tokens_per_call, output_tokens_per_call
			)

			total_requests = sum(int(day.get("count", 0)) for day in records)
			energy_kwh = energy_per_req_kwh * total_requests
			co2_kg = co2_per_req_kg * total_requests
			input_tokens_total = input_tokens_per_call * total_requests
			output_tokens_total = output_tokens_per_call * total_requests

			result["profiles"][profile_name] = {
				"requests": total_requests,
				"input_tokens_per_call": input_tokens_per_call,
				"output_tokens_per_call": output_tokens_per_call,
				"input_tokens_total": input_tokens_total,
				"output_tokens_total": output_tokens_total,
				"energy_kwh": energy_kwh,
				"co2_kg": co2_kg,
			}

			result["total"]["requests"] += total_requests
			result["total"]["energy_kwh"] += energy_kwh
			result["total"]["co2_kg"] += co2_kg
			result["total"]["input_tokens"] += input_tokens_total
			result["total"]["output_tokens"] += output_tokens_total

		result["char_per_token"] = self.char_per_token
		return result


def load_default_calculator() -> EnergyCalculator:
	return EnergyCalculator()


__all__ = ["EnergyCalculator", "load_default_calculator", "ProfileConfig"]
