# The GPLv3 License (GPLv3)

# Copyright © 2024 aitelegrambot authors.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
This module defines the TelegramBot class.
"""

from telegram import Update, Message
from telegram.ext import ContextTypes
from ollama import Client
import aitelegrambot.constants as constants
import re
import time
from dataclasses import dataclass


@dataclass
class OllamaState:
    """
    Arguments
    ==========
    ollama_client: The Ollama client to use for sending messages.
    model: The model to use for inference.
    message_chunk_size: The number of words to be send at a time.
    """

    client: Client
    model: str
    message_chunk_size: int


@dataclass
class CommandHandlers:
    """
    Base class for handling commands.

    Arguments
    ==========
    ollama_state: The Ollama State with Ollama client and model name.
    """

    ollama_state: OllamaState

    def get_content(self, raw_query) -> str:
        """
        Remove the command from query.

        Arguments:
        ==========
        raw_query: the raw query from telegram.
        """
        return re.split(" ", raw_query, 1)[0]


class NormalCommandHandlers(CommandHandlers):
    """
    Class for handling normal commands.
    """

    async def start(
        self,
        update: Update,
        context: ContextTypes.DEFAULT_TYPE,
    ):
        """
        Informs the user about its version.

        Arguments:
        ==========
        update: The update to be processed.
        context: The context for the message.
        """
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=constants.WELCOME_MESSAGE,
            parse_mode="Markdown",
        )

    async def help(
        self,
        update: Update,
        context: ContextTypes.DEFAULT_TYPE,
    ):
        """
        Informs the user about its commands.

        Arguments:
        ==========
        update: The update to be processed.
        context: The context for the message.
        """
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=constants.HELP_MESSAGE,
            parse_mode="Markdown",
        )

    async def basic_inference(
        self,
        update: Update,
        context: ContextTypes.DEFAULT_TYPE,
    ):
        """
        Performs inference on the given update.

        Arguments:
        ==========
        update: The update to be processed.
        context: The context for the inference.
        """
        query: str = self.get_content(update.message.text)

        if query == "":
            await update.message.reply_text(
                text=constants.MISTAKEN_CLICK,
                parse_mode="Markdown"
            )
            return

        message: Message = await update.message.reply_text(
            text="wait...", parse_mode="Markdown"
        )
        await message.edit_text(
            text=self.ollama_state.client.chat(
                model=self.ollama_state.model,
                messages=[
                    {
                        "role": "user",
                        "content": query,
                    },
                ],
            )["message"]["content"],
            parse_mode="Markdown",
        )

    async def stream_inference(
        self,
        update: Update,
        context: ContextTypes.DEFAULT_TYPE,
    ):
        """
        Performs inference on the given update.

        Arguments:
        ==========
        update: The update to be processed.
        context: The context for the inference.
        """
        prev_msg_size: int = 0
        query: str = self.get_content(update.message.text)

        if query == "":
            await update.message.reply_text(
                text=constants.MISTAKEN_CLICK,
                parse_mode="Markdown"
            )
            return

        message: Message = await update.message.reply_text(
            text="wait...", parse_mode="Markdown"
        )
        message_stream: list[str] = []
        for message_chunk in self.ollama_state.client.chat(
            model=self.ollama_state.model,
            messages=[
                {
                    "role": "user",
                    "content": query,
                },
            ],
            stream=True,
        ):
            message_stream.append(message_chunk["message"]["content"])
            cur_msg_size = len(message_stream)

            # avoid BadRequest
            if cur_msg_size == prev_msg_size:
                continue

            is_message_rounded: bool = (
                cur_msg_size % self.ollama_state.message_chunk_size == 0
            )

            is_last_chunk: bool = (
                message_chunk["done"]
            )

            if is_message_rounded or is_last_chunk:
                prev_msg_size = cur_msg_size
                await message.edit_text(
                    text="".join(message_stream), parse_mode="Markdown"
                )
                time.sleep(2)


class AdministrationCommandHandlers(CommandHandlers):
    """
    Class for administrating Ollama by the Bot administrators.
    """

    def __init__(self, ollama_state: OllamaState, administrator_user_ids: list[int]):
        """
        Arguments:
        ==========
        ollama_state: The Ollama State with Ollama client and model name.
        administrator_user_ids: Telegram user ids of the administrators.
        """
        super().__init__(ollama_state)
        self.administrator_user_ids: list[int] = administrator_user_ids

    def is_admin(self, update: Update):
        """
        Check if the current user is an administrator.

        Arguments:
        ==========
        update: The update to be processed.
        """
        return (update.message.from_user.id in self.administrator_user_ids)

    async def list_models(
        self,
        update: Update,
        context: ContextTypes.DEFAULT_TYPE,
    ):
        """
        List the available models in Ollama.

        Arguments:
        ==========
        update: The update to be processed.
        context: The context for the inference.
        """
        if not self.is_admin(update):
            await update.message.reply_text("You are not an Admin!")
            return None

        model_list: list[str] = [
            model["name"] for model in self.ollama_state.client.list()["models"]
        ]

        if len(model_list) == 0:
            await update.message.reply_text(
                "No models available. Pull some using the `/pull_model` command.",
                parse_mode="Markdown"
            )
            return None

        def get_model_text(model_name: str) -> str:
            current_model_indication: str = (
                "*(current_model)*"
                if model_name == self.ollama_state.model
                else ""
            )
            return f"- {current_model_indication}\
            [{model_name}](https://ollama.com/library/{model_name})\n\
            `/change_model {model_name}`"

        models_text = "\n".join(map(get_model_text, model_list))

        await update.message.reply_text(models_text, parse_mode="Markdown")

    async def change_model(
        self,
        update: Update,
        context: ContextTypes.DEFAULT_TYPE,
    ):
        """
        Change the model used by Ollama.

        Arguments:
        ==========
        update: The update to be processed.
        context: The context for the inference.
        """
        if not self.is_admin(update):
            await update.message.reply_text("You are not an Admin!")
            return None
        model: str = self.get_content(update.message.text)
        self.ollama_state.model = model
        await update.message.reply_text(
            f"Alright! changing to *{model}*.", parse_mode="Markdown"
        )

    async def pull_model(
        self,
        update: Update,
        context: ContextTypes.DEFAULT_TYPE,
    ):
        """
        Pull the model used by Ollama.

        Arguments:
        ==========
        update: The update to be processed.
        context: The context for the inference.
        """
        if not self.is_admin(update):
            await update.message.reply_text("You are not an Admin!")
            return None
        model: str = self.get_content(update.message.text)
        if len(model) == 0:
            await update.message.reply_text(
                "We don't have any models!\nTry pulling them."
            )
            return None
        await update.message.reply_text(f"Pulling {model}!")
        self.ollama_state.client.pull(model)
        await update.message.reply_text(f"Done pulling {model}!")

    async def remove_model(
        self,
        update: Update,
        context: ContextTypes.DEFAULT_TYPE,
    ):
        """
        Delete the model used by Ollama.

        Arguments:
        ==========
        update: The update to be processed.
        context: The context for the inference.
        """
        if not self.is_admin(update):
            await update.message.reply_text("You are not an Admin!")
            return None
        model: str = self.get_content(update.message.text)
        await update.message.reply_text(f"Deleting {model}!")
        self.ollama_state.client.delete(model)
        await update.message.reply_text(f"Done deleting {model}!")
