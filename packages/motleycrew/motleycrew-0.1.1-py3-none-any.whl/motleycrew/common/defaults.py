from motleycrew.common import LLMFamily
from motleycrew.common import GraphStoreType


class Defaults:
    DEFAULT_LLM_FAMILY = LLMFamily.OPENAI
    DEFAULT_LLM_NAME = "gpt-4-turbo"
    DEFAULT_LLM_TEMPERATURE = 0.0
    LLM_MAP = {}

    DEFAULT_GRAPH_STORE_TYPE = GraphStoreType.KUZU

    MODULE_INSTALL_COMMANDS = {
        "crewai": "pip install crewai",
        "llama_index": "pip install llama-index",
        "autogen": "pip install autogen",
    }
