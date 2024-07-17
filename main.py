import streamlit as st
import requests

coverage_options = {
    "Normal": (["Fighting", "Psychic", "Dark"],"WhiteSmoke"),
    "Water": (["Ice", "Steel", "Psychic"],"DodgerBlue"),
    "Poison": (["Bug", "Grass", "Electric"],"MediumOrchid"),
    "Psychic": (["Fairy", "Ghost", "Water"],"HotPink"),
    "Fighting": (["Electric", "Ice", "Fire"],"Brown"),
    "Flying": (["Steel", "Dragon", "Fighting"],"LightSkyBlue"),
    "Grass": (["Ground", "Poison", "Rock"],"ForestGreen"),
    "Ground": (["Rock", "Grass", "Dark"],"Sienna"),
    "Bug": (["Dark", "Poison", "Ground"],"YellowGreen"),
    "Rock": (["Ground", "Fire", "Electric"],"DarkKhaki"),
    "Dark": (["Rock", "Electric", "Poison"],"DimGray"),
    "Fairy": (["Psychic", "Water", "Grass"],"Magenta"),
    "Steel": (["Ice", "Ground", "Ghost"],"DarkGray"),
    "Ghost": (["Poison", "Flying", "Bug"],"RebeccaPurple"),
    "Ice": (["Water", "Fairy", "Steel"],"DeepSkyBlue"),
    "Dragon": (["Fire", "Grass", "Psychic"],"DarkBlue"),
    "Electric": (["Fairy", "Grass", "Dragon"],"Gold"),
    "Fire": (["Dragon", "Electric", "Fighting"],"OrangeRed")
}

pokemon=st.text_input("Pokemon Name", placeholder="Enter a Pokemon's name")
try:
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon.lower().rstrip().lstrip()
    data = requests.get(url).json()
    name = data['name'].title()
    image_url = data['sprites']['front_default']
    types_string=":gray[Types:] "
    coverages = []
    coverage_string=":gray[Coverage Options:] "
    for type_data in data["types"]:
        type = type_data["type"]["name"].capitalize()
        types_string+=f'<span style="color:{coverage_options[type][1]}">{type}</span>'+', '
        for coverage in coverage_options[type][0]:
            if coverage not in coverages:
                coverages.append(coverage)
                coverage_string+=f'<span style="color:{coverage_options[coverage][1]}">{coverage}</span>'+', '
    base_stats = {}
    for stat in data["stats"]:
        base_stats[stat["stat"]["name"]] = stat["base_stat"]
    col1, col2 = st.columns(2)
    with col1:
        st.write(f':gray[{name} Info]')
        st.markdown(types_string[0:-2:], unsafe_allow_html=True)
        for stat in ["hp","attack","defense","special-attack","special-defense","speed"]:
            st.write(f":gray[{stat.title()}:] :red[{base_stats[stat]}]")
        st.write(coverage_string[0:-2:], unsafe_allow_html=True)
    with col2:
        st.image(image_url, width=100)  
except:
    if pokemon!="":
        st.write(':gray[Invalid Pokemon Name]')
    else:
        st.write(":gray[Guidelines for use:]")
        st.write(":gray[-Both uppercase and lowercase work]")
        st.write(":gray[-Ensure no spaces between words. Try to replace them with '-']")
        st.write(":gray[-Search groudon-primal instead of primal groudon, etc.]")
