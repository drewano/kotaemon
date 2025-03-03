import gradio as gr
from ktem.app import BasePage
from theflow.settings import settings as flowsettings

KH_DEMO_MODE = getattr(flowsettings, "KH_DEMO_MODE", False)

if not KH_DEMO_MODE:
    PLACEHOLDER_TEXT = (
        "Ceci est le début d'une nouvelle conversation.\n"
        "Commencez par télécharger un fichier ou une URL web. "
        "Visitez l'onglet Fichiers pour plus d'options (ex: GraphRAG)."
    )
else:
    PLACEHOLDER_TEXT = (
        "Bienvenue dans la démo de Kotaemon. "
        "Commencez par parcourir les conversations préchargées pour vous familiariser.\n"
        "Consultez la section Conseils pour plus d'astuces."
    )


class ChatPanel(BasePage):
    def __init__(self, app):
        self._app = app
        self.on_building_ui()

    def on_building_ui(self):
        self.chatbot = gr.Chatbot(
            label=self._app.app_name,
            placeholder=PLACEHOLDER_TEXT,
            show_label=False,
            elem_id="main-chat-bot",
            show_copy_button=True,
            likeable=True,
            bubble_full_width=False,
        )
        with gr.Row():
            self.text_input = gr.MultimodalTextbox(
                interactive=True,
                scale=20,
                file_count="multiple",
                placeholder=(
                    "Tapez un message, recherchez sur le @web, ou taguez un fichier avec @nomfichier"
                ),
                container=False,
                show_label=False,
                elem_id="chat-input",
            )

    def submit_msg(self, chat_input, chat_history):
        """Submit a message to the chatbot"""
        return "", chat_history + [(chat_input, None)]
