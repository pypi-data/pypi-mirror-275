from motleycrew.common import Defaults
from motleycrew.common import LLMFamily, LLMFramework
from motleycrew.common.exceptions import LLMFamilyNotSupported, LLMFrameworkNotSupported
from motleycrew.common.utils import ensure_module_is_installed


def langchain_openai_llm(
    llm_name: str = Defaults.DEFAULT_LLM_NAME,
    llm_temperature: float = Defaults.DEFAULT_LLM_TEMPERATURE,
    **kwargs,
):
    from langchain_openai import ChatOpenAI

    return ChatOpenAI(model=llm_name, temperature=llm_temperature, **kwargs)


def llama_index_openai_llm(
    llm_name: str = Defaults.DEFAULT_LLM_NAME,
    llm_temperature: float = Defaults.DEFAULT_LLM_TEMPERATURE,
    **kwargs,
):
    ensure_module_is_installed("llama_index")
    from llama_index.llms.openai import OpenAI

    return OpenAI(model=llm_name, temperature=llm_temperature, **kwargs)


Defaults.LLM_MAP = {
    (LLMFramework.LANGCHAIN, LLMFamily.OPENAI): langchain_openai_llm,
    (LLMFramework.LLAMA_INDEX, LLMFamily.OPENAI): llama_index_openai_llm,
}


def init_llm(
    llm_framework: str,
    llm_family: str = Defaults.DEFAULT_LLM_FAMILY,
    llm_name: str = Defaults.DEFAULT_LLM_NAME,
    llm_temperature: float = Defaults.DEFAULT_LLM_TEMPERATURE,
    **kwargs,
):

    func = Defaults.LLM_MAP.get((llm_framework, llm_family), None)
    if func is not None:
        return func(llm_name=llm_name, llm_temperature=llm_temperature, **kwargs)

    raise LLMFamilyNotSupported(llm_framework=llm_framework, llm_family=llm_family)
