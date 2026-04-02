from __future__ import annotations

from langchain.tools import Tool
from langchain_experimental.tools import PythonREPLTool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.tools.tavily_search import TavilySearchResults

from src.config import NOTES_FILE, settings


def calculator(expression: str) -> str:
    try:
        allowed_builtins = {"abs": abs, "round": round, "min": min, "max": max}
        result = eval(expression, {"__builtins__": allowed_builtins}, {})
        return str(result)
    except Exception as e:
        return f"Erreur calcul : {e}"


def read_saved_notes(_: str = "") -> str:
    try:
        if not NOTES_FILE.exists():
            return "Aucune note enregistrée."
        content = NOTES_FILE.read_text(encoding="utf-8").strip()
        return content if content else "Aucune note enregistrée."
    except Exception as e:
        return f"Erreur lecture notes : {e}"


def save_note(text: str) -> str:
    try:
        NOTES_FILE.parent.mkdir(parents=True, exist_ok=True)
        with NOTES_FILE.open("a", encoding="utf-8") as f:
            f.write(text.strip() + "\n")
        return "Note enregistrée avec succès."
    except Exception as e:
        return f"Erreur sauvegarde note : {e}"


def clear_notes(_: str = "") -> str:
    try:
        NOTES_FILE.write_text("", encoding="utf-8")
        return "Toutes les notes ont été supprimées."
    except Exception as e:
        return f"Erreur suppression notes : {e}"


def get_tools():
    tools = [
        Tool(
            name="Calculator",
            func=calculator,
            description="Utilise cet outil pour faire des calculs mathématiques.",
        ),
        Tool(
            name="ReadNotes",
            func=read_saved_notes,
            description="Lit les notes sauvegardées localement.",
        ),
        Tool(
            name="SaveNote",
            func=save_note,
            description="Enregistre une note locale.",
        ),
        Tool(
            name="ClearNotes",
            func=clear_notes,
            description="Supprime toutes les notes locales.",
        ),
        DuckDuckGoSearchRun(),
        PythonREPLTool(),
    ]

    if getattr(settings, "tavily_api_key", ""):
        try:
            tools.append(TavilySearchResults(max_results=3))
        except Exception:
            pass

    return tools