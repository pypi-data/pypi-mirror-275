import streamlit as st

from streamlit_pandera.validate_file import run_validate_file


def main():
    standards = {
        "store_schema": "https://raw.githubusercontent.com/resilientinfrastructure/standards/main/panderas_schema.yml"
    }
    validated_df = run_validate_file(standards=standards)
    # DO SOMETHING ELSE WITH VALIDATED_DF


if __name__ == "__main__":
    main()
