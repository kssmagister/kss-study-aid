from langchain.prompts import PromptTemplate

prompt_template_questions = """
Sie sind Experte für die Erstellung von Übungsfragen auf der Grundlage von Studienmaterial.
Ihr Ziel ist es, einen Studenten auf seine Prüfung vorzubereiten. Sie tun dies, indem Sie Fragen zum unten stehenden Text stellen:

------------
{text}
------------

Erstellen Sie Fragen, die die Schüler auf ihre Prüfung vorbereiten. Achten Sie darauf, dass keine wichtigen Informationen verloren gehen.

QUESTIONS:
"""
PROMPT_QUESTIONS = PromptTemplate(template=prompt_template_questions, input_variables=["text"])

refine_template_questions = ("""
Sie sind Experte für die Erstellung von Übungsfragen auf der Grundlage von Studienmaterial.
Ihr Ziel ist es, einem Studenten bei der Vorbereitung auf eine Prüfung zu helfen.
Wir haben einige Übungsfragen zu einem gewissen Grad erhalten: {existing_answer}.
Wir haben die Möglichkeit, die bestehenden Fragen zu verfeinern oder neue Fragen hinzuzufügen.
(nur wenn nötig) mit etwas mehr Kontext unten.
------------
{text}
------------

Verfeinern Sie angesichts des neuen Kontexts die ursprünglichen Fragen auf Deutsch.
Wenn der Kontext nicht hilfreich ist, stellen Sie bitte die Originalfragen.
QUESTIONS:
"""
)
REFINE_PROMPT_QUESTIONS = PromptTemplate(
    input_variables=["existing_answer", "text"],
    template=refine_template_questions,
)