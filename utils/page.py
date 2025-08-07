import streamlit as st
from typing import Callable, Optional, Dict


def page_group(param: str):
    key = f"{__name__}_page_group_{param}"

    if key not in st.session_state:
        st.session_state[key] = PageGroup(param)

    return st.session_state[key]


class PageGroup:
    def __init__(self, param: str):
        self._param: str = param
        self._default: Optional[str] = None
        self._pages: Dict[str, Callable] = {}

    @property
    def selected(self) -> str:
        params = st.query_params
        return params[self._param][0] if self._param in params else self._default

    def item(self, label: str, callback: Callable, default: bool = False) -> None:
        page = self._normalize_label(label)
        self._pages[page] = callback
        if default and not self._default:
            self._default = page

    def show(self, name: Optional[str] = None) -> None:
        # Accept explicit page name or fall back to selected/default
        page_key = self._normalize_label(name) if name else self.selected
        callback = self._pages.get(page_key)

        if callback:
            callback()
        else:
            st.title("🤷 404 Not Found")

    def _normalize_label(self, label: str) -> str:
        return "".join(char.lower() for char in label if char.isascii()).strip().replace(" ", "-")
