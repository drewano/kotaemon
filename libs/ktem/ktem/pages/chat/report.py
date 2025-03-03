from typing import Optional

import gradio as gr
from ktem.app import BasePage
from ktem.db.models import IssueReport, engine
from sqlmodel import Session


class ReportIssue(BasePage):
    def __init__(self, app):
        self._app = app
        self.on_building_ui()

    def on_building_ui(self):
        with gr.Accordion(label="Commentaires", open=False, elem_id="report-accordion"):
            self.correctness = gr.Radio(
                choices=[
                    ("La réponse est correcte", "correct"),
                    ("La réponse est incorrecte", "incorrect"),
                ],
                label="Correction :",
            )
            self.issues = gr.CheckboxGroup(
                choices=[
                    ("La réponse est offensante", "offensive"),
                    ("Les preuves sont incorrectes", "wrong-evidence"),
                ],
                label="Autre problème :",
            )
            self.more_detail = gr.Textbox(
                placeholder=(
                    "Plus de détails (par exemple, à quel point est-ce faux, quelle est la "
                    "bonne réponse, etc...)"
                ),
                container=False,
                lines=3,
            )
            gr.Markdown(
                "Ceci enverra la conversation actuelle et vos paramètres utilisateur pour "
                "aider à l'enquête."
            )
            self.report_btn = gr.Button("Signaler")

    def report(
        self,
        correctness: str,
        issues: list[str],
        more_detail: str,
        conv_id: str,
        chat_history: list,
        settings: dict,
        user_id: Optional[int],
        info_panel: str,
        chat_state: dict,
        *selecteds,
    ):
        selecteds_ = {}
        for index in self._app.index_manager.indices:
            if index.selector is not None:
                if isinstance(index.selector, int):
                    selecteds_[str(index.id)] = selecteds[index.selector]
                elif isinstance(index.selector, tuple):
                    selecteds_[str(index.id)] = [selecteds[_] for _ in index.selector]
                else:
                    print(f"Unknown selector type: {index.selector}")

        with Session(engine) as session:
            issue = IssueReport(
                issues={
                    "correctness": correctness,
                    "issues": issues,
                    "more_detail": more_detail,
                },
                chat={
                    "conv_id": conv_id,
                    "chat_history": chat_history,
                    "info_panel": info_panel,
                    "chat_state": chat_state,
                    "selecteds": selecteds_,
                },
                settings=settings,
                user=user_id,
            )
            session.add(issue)
            session.commit()
        gr.Info("Merci pour vos commentaires")