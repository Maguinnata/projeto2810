import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Análise DRX x OPTC',
                   page_icon= ':bar_chart:',
                   layout= 'wide',
                   )



st.title('Análise DRX x OPTC - Fracture')
st.markdown('----')
st.write('Essa é uma análise da partida DRX x OPTC no mapa da Fracture, que foi jogado no Valorant Champions de 2022. '
         'A ideia é analisar o jogo pelo ponto de vista de ambas as equipes, '
         'falando sobre os padrões e setups dos times em rounds Pistol; ECO; Anti-ECO e Armados, '
         'além disso conta com stats da partida comparando ambas equipes.')
st.markdown('##')
st.subheader('Feito por: Maguinnata :)')

