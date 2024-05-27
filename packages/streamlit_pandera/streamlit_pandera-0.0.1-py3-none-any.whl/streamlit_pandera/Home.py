import streamlit as st

from streamlit_pandera.io_file_validator import run_validate_file


def main():
    standards = {
        "store_schema": ("https://raw.githubusercontent.com/resilientinfrastructure/standards/main/panderas_schema.yml")
    }
    st.set_page_config(
        page_title="Data Validator Home",
        page_icon="📊",
    )

    run_validate_file(standards=standards)
    # TODO: DO SOMETHING ELSE WITH VALIDATED_DF


if __name__ == "__main__":
    main()
