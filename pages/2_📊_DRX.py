import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Análise DRX x OPTC',
                   page_icon= ':bar_chart:',
                   #layout= 'wide',
                   )


stats_indiv_drx = pd.read_excel('Stats Individual DRX.xlsx')
stats_t_ct_drx = pd.read_excel('Stats Time CT DRX.xlsx')
stats_t_tr_drx = pd.read_excel('Stats Time TR DRX.xlsx')
stats_eco_drx = pd.read_excel('Stats ECO DRX.xlsx')

stats_ct = stats_t_ct_drx.groupby(['Mapas','Bomb']).sum().round(2)
stats_tr = stats_t_tr_drx.groupby(['Mapas','Bomb']).sum().round(2)


st.title('DRX')

tab1, tab2, tab3 = st.tabs(['▶️ Análise','▶️ Stats Time','▶️ Stats Individual'])

with tab1:
    st.title('Lado de Ataque')
    st.markdown('##')
    st.write('Mesmo começando perdendo, a DRX conseguiu jogar com mais de um jeito com a composição. '
             'Seja jogando em bloco e usando todo o poder de utilitárias para entrar no Bomb ou jogando '
             'um pouco mais lento e buscando informação e contato antes de fazer a explosão. '
             'Importante notar que por terem ultimates muito fortes eles tentam usar em rounds seguidos, '
             'com o intuito de criar uma bola de neve independente da economia adversária,'
             ' esse fator vem das ults do Breach e Fade, que são as principais ferramentar para uma boa explosão.')
    st.markdown('##')
    st.markdown('##')

    st.subheader('Posicionamento da DRX antes do plant')
    st.write('A ideia aqui é mostrar por onde a DRX mais joga no mapa. '
             'Nesse caso podemos ver uma predominancia pelo Bomb B e a parte da garagem para entradas no Bomb A. '
             'Outro ponto importante é que o Chamber geralmente aparece de maneira mais isolada ao restante do grupo, '
             'antes da spike ser plantada.')
    st.image('imagens/DRX atk geral.png')
    st.markdown('----')
    st.markdown('##')

    st.title('-Pistol')
    st.markdown('##')

    st.image('imagens/DRX atk 1 P.png')
    st.write('Setup DRX Pistol ATK')
    st.markdown('##')

    st.video('videos/DRX1.mp4')
    st.write('Avanço rápido em 5 da DRX, pela garagem, utilizando uma das propostas da composição. '
            'A utilização de utilitários é feita na intenção de tirar os adversários de posição e isolar o espaço do Bomb,'
            'que por consequência dificulta o tempo de resposta do time da OPTC.')
    st.markdown('##')

    st.image('imagens/DRX atk 2 P.png')
    st.write('O posicionamento do post plant é feito de forma muito bem,'
            ' pois são posições que vao conseguir, rapidamente, '
            ' a informação de onde os adversários vem.')
    st.markdown('----')

    st.title('-ECO')
    st.markdown('##')

    st.image('imagens/DRX atk 4 E.png')
    st.image('imagens/DRX extra 1.png')
    st.write('Round mais lento jogando em torno dos espaços da orbe, '
             'pois só faltam 2 orbes p/ ult da Neon que pode ser a condição de vitória da DRX no round eco. '
             'Porém não conseguem executar devido ao avanço da OPTC após o contato no bomb B ')

    st.markdown('##')
    st.video('videos/DRX2.mp4')

    st.markdown('----')

    st.title('-Anti-ECO')
    st.markdown('##')

    st.image('imagens/DRX atk 12 AE.png')
    st.write('Exec rápida no segundo tempo do round no Bomb B sendo feita pela parte superior do mapa '
             'usando a ultimate da Fade. Mesmo caindo num stack de 4 player com stinger eles conseguem ter êxito,'
             'o que só mostra a força dessa ult com a entrada rápida da Neon e o poder da vantagem de armas.')
    st.video('videos/DRX3.mp4')


    st.markdown('----')

    st.title('-Armados')
    st.markdown('##')

    st.subheader('1º Padrão')
    st.image('imagens/DRX atk 5 AR.png')
    st.video('videos/DRX4.mp4')
    st.write('2-3 usando fake com a Neon e utilitárias do Breach para entrar no bomb B conseguindo vantagem '
             'numérica e forçando muitas utilitárias dos 3 jogadores restantes da OPTC (o que é muito valioso pois dificulta o retake no bomb A). '
             'Entretanto, mesmo com uma boa tática alguns erros de posicionamento acontecem e '
             'também por não terem jogados juntos no post plant, acaba resultando em uma situação de desvantagem.'
             )
    st.markdown('##')
    st.markdown('##')

    st.subheader('2º Padrão')
    st.video('videos/DRX5.mp4')
    st.write('Mesmo com desvantagem e alguns erros no post-plant o Brimstone consegue jogar uma situação de 1x3 muito bem, '
             'separando os inimigos com sua ultimate e também comprando tempo.')
    st.markdown('##')
    st.markdown('##')

    st.subheader('3º Padrão')
    st.image('imagens/DRX atk 9 AR.png')
    st.video('videos/DRX6.mp4')
    st.write('Variação da execução no Bomb B, dessa vez agora vindo da região superior e mantendo apenas 1 player por baixo. '
             'E mesmo com a OPTC jogando de fora do Bomb, para fazer retake, a DRX consegue vencer o round.')
    st.markdown('##')

    st.video('videos/DRX7.mp4')
    st.write('Entrada foi boa e conseguiu muito espaços, importante notar também que o post plant foi bem executado pelo Brimstone, '
             'devido a ter jogado de fora do Bomb usando seus recursos para ganhar tempo. ')
    st.markdown('##')
    st.markdown('##')

    st.image('imagens/DRX atk 8 AR.png')
    st.video('videos/DRX8.mp4')
    st.write('3-2 rápido no bomb A, porém a parte de cima (Neon e Chamber) entram mt cedo, pois a parte de baixo ainda está limpando garagem, '
             'e mesmo que estivessem mais próximos para entrar no Bomb junto a parte superior, '
             'não conseguiriam devido as utilitárias da OPTC impedindo a passagem. '
             'Mesmo com a entrada desconexa no bomb a DRX consegue ganhar o round, decidindo jogar mais lento e esperando algum erro da OPTC.')

    st.markdown('----')
    st.markdown('----')

    st.title('Lado de Defesa')
    st.markdown('##')
    st.write('Diferente da OPTC, jogaram mais em torno de um setup 3-2, e buscando informação em alguma parte do mapa. '
             'Algumas vezes o Breach conseguia espaço mais avançado para o Chamber,principalmente em torno da garagem, '
             'o intuito é que aquela região sempre tenha que ser limpa pelo time adversário, forçando uso de utilitárias. '
             'Importante fator, é que similar ao ataque a DRX conseguiu muitas vezes abrir mão dos bombs e jogar retake em torno de ultimates fortes, '
             'como Fade, Breach e Brimstone.')
    st.markdown('##')
    st.markdown('##')

    st.subheader('Posicionamento da DRX antes do plant')
    st.write('A ideia aqui é mostrar por onde a DRX mais joga no mapa.'
             'Aqui podemos ter ideia de como é o setup da defesa, como por exemplo, tendo o Breach mais vezes para o Bomb A e '
             'a preferência do Chamber pelo Bomb B.')
    st.image('imagens/DRX def geral.png')

    st.markdown('----')
    st.markdown('##')


    st.title('-Pistol')
    st.markdown('##')

    st.image('imagens/DRX def 1 P.png')
    st.video('videos/DRX9.mp4')
    st.write('Batida na parte de cima do mapa, tendo como ideia o chamber cuidar da parte de baixo do mapa de ambos os Bombs '
             '(a trap só pode ser evitada com alguma habilidade, ou seja forçando utilitárias e gerando informação). '
             'Com esse avanço, fica claramente definido que o Bomb B será jogado para retake.')
    st.markdown('----')


    st.title('-ECO')
    st.markdown('##')

    st.image('imagens/DRX def 2 E.png')
    st.video('videos/DRX10.mp4')
    st.write('Tentativa de stack no Bomb B mas a OPTC executa pro outro bomb. Fazendo com que o Bomb A seja retake, '
             'porém com dificuldade devido a desvantagem de armamentos e utilitários.')
    st.markdown('----')

    st.title('-Anti-ECO')
    st.markdown('##')

    st.subheader('1º Padrão')
    st.image('imagens/DRX def 5 AE.png')
    st.video('videos/DRX11.mp4')
    st.write('Nesse round pode ter rolado um pedido de smoke por parte da Neon, '
             'que por vantagem de arma tomou a decisão de redominar a garagem sozinha com os lobos da Fade.')
    st.markdown('##')
    st.markdown('##')

    st.subheader('2º Padrão')
    st.image('imagens/DRX def 7 AE.png')
    st.video('videos/DRX12.mp4')
    st.write('Jogaram 3-2 que no meio de round se transformou num Retake A com apenas o chamber jogando da Base. '
             'Essa decisão pode ter sido tomada devido a ter a vantagem de armamento e ter a ult do Breach disponível.'
             '')
    st.markdown('----')

    st.title('-Armados')
    st.markdown('##')

    st.subheader('1º Padrão')
    st.image('imagens/DRX def 4 AR.png')
    st.write('Padrão 3-2 pode ser por preferência de preferir jogar retake no Bomb A, '
             'deixando o Breach para dar espaço pro Chamber e sendo a rotação pro Bomb B. ')
    st.video('videos/DRX13.mp4')
    st.write('Boa abertura do Brimstone, que aproveitou lobo da Fade, '
             'também tinha a informação do click na orbe, então seria um a menos com mira no momento de abrir ')
    st.markdown('##')
    st.markdown('##')

    st.subheader('2º Padrão')
    st.image('imagens/DRX def 6 AR.png')
    st.video('videos/DRX14.mp4')
    st.write('Variação do setup, invertendo o Bomb do Chamber e tendo o suporte do Brimstone.'
             'Uso da trap para ter segurança da parte superior do Bomb B e jogando pela parte inferior. '
             'O Brimstone ficou como reação ao pick do Chamber para uso da ultimate. '
             'Conseguindo comprar mais tempo ainda para os 3 players do outro bomb conseguirem rotacionar')
    st.markdown('##')
    st.markdown('##')

    st.subheader('3º Padrão')
    st.image('imagens/DRX def 8 AR.png')
    st.video('videos/DRX15.mp4')
    st.write('Utilitárias para atrasar a OPTC de lutar pela orbe, '
             'tendo em vista que só faltava uma orbe para o Breach e Kay/o inimigos, '
             'conseguindo assim vantagem numérica logo cedo no round.')


with tab2:

    st.write('O intuito é analisar quanto plants e retakes foram feitos pelo time, '
             'tendo em conta a situação no momento em que a spike foi plantada (Vantagem, Desvantagem e Igualdade). '
             'Além disso, contabilizar os rounds ECO e verificar quantas armas foram tiradas do time adversário e também '
             'ver o aproveitamento de rounds 5x4 e 4x5, para saber como os times jogam em situação de vantagem e desvantagem, respectivamente.')
    st.markdown('----')

    st.subheader('Retakes')
    st.table(stats_ct.style.format(precision=0))
    st.markdown('##')

    st.subheader('Plants')
    st.table(stats_tr.style.format(precision=0))
    st.markdown('##')

    st.subheader('ECO')
    st.table(stats_eco_drx.style.format(precision=0))
    st.markdown('##')

    st.subheader('5x4 & 4x5')
    st.image('imagens/DRX extra 2.png')

with tab3:
    st.write('Aqui temos os stats individuais do time da DRX. Como só está sendo analisado um único mapa,'
             ' não tem como gerar média e quartis desses stats, então o gráfico acaba sendo apenas uma forma melhor de visualizar e comparar.'
             '')
    st.markdown('----')

    st.table(stats_indiv_drx.style.format(precision=2))

    st.sidebar.header('Filtros')

    var1 = st.sidebar.multiselect(
        'Selecione uma Variável (Stats Individual)',
        options= stats_indiv_drx.columns.unique()
    )

    stats_var1 = stats_indiv_drx.query(
        'ACS == @var1'
    )

    g_stats_indiv = px.bar(
        stats_indiv_drx.round(2),
        x= 'Players',
        y= var1,
        barmode= 'group',
        text_auto= True,
        color_discrete_sequence= ['#0d0887','orangered','lightslategray'],
        width= 800,
        height= 500,
        template= 'plotly_white'
    )

    g_stats_indiv.update_layout(
        plot_bgcolor= 'rgba(0,0,0,0)',
        xaxis= (dict(showgrid=False))
    )
    g_stats_indiv.update_layout(font= dict(size=15))

    st.plotly_chart(g_stats_indiv)
