from __future__ import annotations

from langchain.agents import AgentType, initialize_agent
from langchain.memory import ConversationBufferMemory

from src.middleware import (
    UserContext,
    apply_guardrails,
    build_system_prompt,
    choose_model,
    human_in_the_loop_confirm,
)
from src.tools import get_tools, read_saved_notes


def maybe_handle_sensitive_action(user_input: str) -> None:
    lowered = user_input.lower()
    if "save note" in lowered or "enregistre" in lowered or "supprime" in lowered:
        allowed = human_in_the_loop_confirm(
            "Cette action peut modifier des données locales. Voulez-vous continuer ?"
        )
        if not allowed:
            raise ValueError("Action annulée par l'utilisateur.")


def main():
    print("=" * 70)
    print("Agent LangChain - TP AI Agents")
    print("Tapez 'exit' pour quitter, 'notes' pour afficher les notes.")
    print("=" * 70)

    context = UserContext()

    memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
    input_key="input",
    output_key="output",
    )

    while True:
        user_input = input("\nVous > ").strip()

        if user_input.lower() in {"exit", "quit"}:
            print("Au revoir.")
            break

        if user_input.lower() == "notes":
            print(read_saved_notes(""))
            continue

        if not user_input:
            continue

        try:
            apply_guardrails(user_input)
            maybe_handle_sensitive_action(user_input)

            llm = choose_model(user_input)
            tools = get_tools()

            agent = initialize_agent(
                tools=tools,
                llm=llm,
                agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
                memory=memory,
                verbose=True,
                handle_parsing_errors=True,
                agent_kwargs={
                    "system_message": build_system_prompt(user_input),
                },
            )

            full_input = (
                f"Contexte utilisateur: nom={context.username}, cours={context.course}.\n"
                f"Question: {user_input}"
            )

            response = agent.invoke({"input": full_input})
            print(f"\nAgent > {response['output']}")

        except Exception as e:
            print(f"\nErreur > {e}")