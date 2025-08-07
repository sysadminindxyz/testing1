import streamlit as st
from typing import Callable, Optional


def page_group(param):
    key = f"{__name__}_page_group_{param}"

    if key not in st.session_state:
        st.session_state[key] = PageGroup(param)

    return st.session_state[key]


class PageGroup:

    def __init__(self, param):
        self._param = param  # Name of query param (e.g., 'page')
        self._default = None  # Default page if no query param is set
        self._selected = None  # Callback for the selected page
        self._backup = None  # To handle selection toggling

        # Fix some rollback issues when multiple pages are selected in the same run.
        self._backup: Optional[str] = None

    @property
    def selected(self) -> bool:
        params = st.query_params
        return params[self._param][0] if self._param in params else self._default

    def item(self, label: str, callback: Callable, default=False) -> None:
        # self._backup = None   ###NO LONGER NEEDED FOR LINKS (NOT CHECKBOXES)
        # key = f"{__name__}_{self._param}_{label}" ###NO LONGER NEEDED FOR LINKS (NOT CHECKBOXES)

        page = self._normalize_label(label)

        if default:
            self._default = page

        selected = (page == self.selected)

        if selected:
            self._selected = callback

        label_display = f"**{label}**" if selected else label
        if st.button(label_display, key=label):
            st.query_params[self._param] = page

    def show(self) -> None:
        if self._selected is not None:
            self._selected()
        else:
            st.title("🤷 404 Not Found")

    def _on_change(self, page: str) -> None:
        params = st.query_params

        if self._backup is None:
            if self._param in params:
                self._backup = params[self._param][0]
            params[self._param] = [page]
        else:
            params[self._param] = [self._backup]

        st.query_params = {k: v[0] for k, v in params.items()}  # ✅ Update using new API

    def _normalize_label(self, label: str) -> str:
        return "".join(char.lower() for char in label if char.isascii()).strip().replace(" ", "-")
