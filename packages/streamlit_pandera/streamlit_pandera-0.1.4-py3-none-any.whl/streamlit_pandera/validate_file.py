import logging
from tempfile import NamedTemporaryFile

import pandas as pd
import pandera as pa
import requests
import streamlit as st
import validators
import yaml
from io_file_validator.validator import ValidatorDataframe

logger = logging.getLogger(__name__)

if "panderas_url" not in st.session_state:
    st.session_state["panderas_url"] = "Unassigned"


def assign_panderas_url(panderas_url):
    if validators.url(panderas_url):
        st.success("Valid URL! Proceed.")
        st.session_state["panderas_url"] = panderas_url
    else:
        st.session_state["panderas_url"] = "Unassigned"
        st.error("Panderas URL not valid!")


def set_panderas_url_from_selectbox(standards):
    names = [name for name in standards]
    name = st.selectbox(
        label="File standard (as defined in standards section)",
        options=(names),
    )
    # Add a button to confirm selection
    if st.button("Confirm"):
        # Check if a selection has been made
        if name:
            # Perform actions based on the selected name
            st.write("Selected name:", name)
        else:
            # Display an error message if no selection is made
            st.error("Please select a name.")
        standard_url = standards[name]
        st.success(f"Selected {name}, we will validate file against {standard_url}")
        assign_panderas_url(panderas_url=standard_url)
        return name


def run_validate_file(
    validator: ValidatorDataframe = ValidatorDataframe(url=None, file_format="csv"), standards: dict = {}
):
    """
    standards is a key value pair of name and url
    e.g.: 'inclinometr': 'https://path/to/panderas/url"""
    st.set_page_config(
        page_title="Data Validator Home",
        page_icon="📊",
    )

    st.write("# Data Validation Tool Using Pandera Yaml Schemas! 📊")

    name = set_panderas_url_from_selectbox(standards=standards)

    if "panderas_url" in st.session_state:

        if st.session_state["panderas_url"] is not None:

            uploaded_file = st.file_uploader("Choose a file")
            if uploaded_file is not None:
                dataframe = validator.run_validation(uploaded_file=uploaded_file)
                st.success("Validated dataframe!")
                st.dataframe(dataframe)
                st.balloons()
                return uploaded_file
