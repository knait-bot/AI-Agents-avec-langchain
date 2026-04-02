from __future__ import annotations

import re
from dataclasses import dataclass

from langchain_openai import ChatOpenAI

from src.config import settings


BLOCKED_PATTERNS = [
    r"ignore all previous instructions",
    r"system prompt",
    r"reveal.*api key",
    r"show.*secret",
]


def apply_guardrails(user_input: str) -> None:
    lowered = user_input.lower()
    for pattern in BLOCKED_PATTERNS:
        if re.search(pattern, lowered):
            raise ValueError(
                "La requête a été bloquée par les guardrails du projet."
            )


def choose_model(user_input: str) -> ChatOpenAI:
    # Dynamic model
    text = user_input.strip()
    chosen = settings.openai_model_simple if len(text) < 120 else settings.openai_model
    return ChatOpenAI(
        model=chosen,
        temperature=settings.temperature,
        api_key=settings.openai_api_key,
    )


def build_system_prompt(user_input: str) -> str:
    # Dynamic prompt
    lowered = user_input.lower()

    if any(word in lowered for word in ["calcule", "calcul", "math", "+", "-", "*", "/"]):
        task_hint = "Tu privilégies les outils de calcul quand c'est utile."
    elif any(word in lowered for word in ["cherche", "recherche", "web", "internet"]):
        task_hint = "Tu privilégies les outils de recherche web quand c'est utile."
    elif any(word in lowered for word in ["note", "mémoire", "souviens", "remember"]):
        task_hint = "Tu fais attention à la mémoire et aux notes enregistrées."
    else:
        task_hint = "Tu réponds clairement et brièvement, puis détailles si nécessaire."

    return (
        "Tu es un assistant pédagogique pour un TP LangChain. "
        "Sois utile, clair et structuré. "
        f"{task_hint} "
        "Quand un outil est nécessaire, utilise-le. "
        "Si un outil échoue, explique simplement l'erreur et continue si possible."
    )


@dataclass
class UserContext:
    username: str = "Student"
    course: str = "AI Agents avec LangChain"


def human_in_the_loop_confirm(question: str) -> bool:
    answer = input(f"{question} [y/N]: ").strip().lower()
    return answer in {"y", "yes", "o", "oui"}
