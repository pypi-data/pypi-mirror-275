import streamlit as st

from streamlit_pandera.validate_file import run_validate_file


def main():
    validated_df = run_validate_file()
    # DO SOMETHING ELSE WITH VALIDATED_DF


if __name__ == "__main__":
    main()
