import streamlit as st

from views import pages



list_of_pages = [
    "Overview",
    "Demographics",
    "Clustering",
    "Who are not Saving for Old Age?",
    "Conclusion",
    "Recommendation",
    "Pandas.RAKS"
]

st.sidebar.title(':scroll: Main Pages')
selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == "Overview":
    pages.Overview()

elif selection == "Demographics":
    pages.demog()

elif selection == "Clustering":
    pages.clustering()

elif selection == "Who are not Saving for Old Age?":
    pages.wansoa()
    
elif selection == "Conclusion":
    pages.conclusion()

elif selection == "Recommendation":
    pages.recommendation()

elif selection == "Pandas.RAKS":
    pages.the_team()
