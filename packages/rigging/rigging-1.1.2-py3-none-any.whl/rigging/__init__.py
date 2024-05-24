from rigging.chat import Chat, PendingChat
from rigging.completion import Completion, PendingCompletion
from rigging.data import chats_to_df, df_to_chats
from rigging.generator import GenerateParams, Generator, chat, complete, get_generator, register_generator
from rigging.message import Message, MessageDict, Messages
from rigging.model import Model, attr, element, make_primitive, wrapped
from rigging.tool import Tool

__version__ = "1.1.1"

__all__ = [
    "get_generator",
    "Message",
    "MessageDict",
    "Messages",
    "Tool",
    "Model",
    "attr",
    "element",
    "wrapped",
    "Chat",
    "PendingChat",
    "Generator",
    "GenerateParams",
    "chat",
    "complete",
    "Completion",
    "PendingCompletion",
    "register_generator",
    "chats_to_df",
    "df_to_chats",
    "make_primitive",
]

from loguru import logger

logger.disable("rigging")
