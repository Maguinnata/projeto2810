import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Análise DRX x OPTC',
                   page_icon= ':bar_chart:',
                   layout= 'wide',
                   )

stats_indiv_optc = pd.read_excel('Stats Individual OPTC.xlsx')
stats_t_ct_optc = pd.read_excel('Stats Time CT OPTC.xlsx')
stats_t_tr_optc = pd.read_excel('Stats Time TR OPTC.xlsx')
stats_eco_optc = pd.read_excel('Stats ECO OPTC.xlsx')

stats_ct = stats_t_ct_optc.groupby(['Mapas', 'Bomb']).sum().round(2)
stats_tr = stats_t_tr_optc.groupby(['Mapas', 'Bomb']).sum().round(2)




st.title('Optic')

tab1, tab2, tab3 = st.tabs(['▶️ Análise','▶️ Stats Time','▶️ Stats Individual'])

with tab1:
    st.title('Lado de Ataque')
    st.markdown('##')
    st.write('Com uma quantidade de rounds menor nesse half, a OPTC só teve 4 armados, os quais os 3 foram desastrosos e com muitas falhas, '
             'não é atoa que só conseguiram ganhar 1 round, devido a um clutch do Brimstone numa situação 1x2. '
             'Além disso os rounds ECO não houveram impactos na economia inimiga pois não conseguiam tirar uma quantidade significativa de armas.')
    st.markdown('##')
    st.markdown('##')

    st.subheader('Posicionamento da OPTC antes do plant')
    st.write('A ideia aqui é mostrar por onde a OPTC mais joga no mapa.'
             'Aqui podemos ter ideia de como o setup da ataque da Optic é predominantemente feito pela região inferior do mapa.')
    st.image('imagens/OPTC atk geral.png')

    st.markdown('----')
    st.markdown('##')

    st.title('-Pistol')
    st.markdown('##')

    st.image('imagens/OPTC atk 1 P.png')
    st.video('videos/OPTC11.mp4')
    st.write('Possível fake com o Kay/o na parte superior chamando rotação e conseguindo vantagem numérica. '
             'Enquanto isso, os outros 4 players conseguem o domínio do Bomb de forma tranquila e tem a vantagem de posicionamento.')

    st.markdown('##')

    st.video('videos/OPTC12.mp4')
    st.write('Decisão de stackar em torno da parte superior do bomb B devido ao contato inicial e pensamento de que o retake será feito por ali. '
             'Entretanto não contavam que a DRX já havia passado e que todos os players stackaram em uma região sem visão direta para a spike, '
             'por pouco a prensa da DRX não da certo e a OPTC perderia o round.')
    st.markdown('----')

    st.title('-ECO')
    st.markdown('##')

    st.write('Não houveram rounds com estratégias ou impactos relevantes.')

    st.markdown('----')

    st.title('-Anti-ECO')
    st.markdown('##')

    st.image('imagens/OPTC atk 2 AE.png')
    st.video('videos/OPTC13.mp4')
    st.write('Anti-eco padrão jogando em bloco para entrar no Bomb A, '
             'de inicio utiliza utilitárias para ganhar/limpar espaço,'
             ' tirando qualquer jogador adversário que possa estar avançado.')

    st.markdown('##')

    st.video('videos/OPTC14.mp4')
    st.write('Post Plant voltado para a garagem, depois do primeiro contato que o Breach teve')

    st.markdown('----')

    st.title('-Armados')
    st.markdown('##')

    st.subheader('1º Padrão')
    st.image('imagens/OPTC atk 3 AR.png')
    st.video('videos/OPTC15.mp4')
    st.write('Jogando 4-1 pelo Bomb B, apesar da first kill vir por parte do Chamber da OPTC, '
             'contato na parte superior é desastroso, tendo em vista que o objetivo era pegar a ultimate do Brimstone, '
             'entretanto ao mesmo tempo o Breach vai para a posição de Ultimate. '
             'Assim o time fica posicionado de maneira totalmente isolada e '
             'possível de brecha para o time adversário usar utilitárias e conseguir duelos 1x1.')
    st.markdown('##')
    st.markdown('##')

    st.subheader('2º Padrão')
    st.image('imagens/OPTC atk 4 AR.png')
    st.video('videos/OPTC16.mp4')
    st.write('Neon abrindo sem nenhuma utilitária e ninguém para fazer trade e só depois que ele morre vem o stun do Breach, '
             'claramente um erro de comunicação; ')

    st.markdown('##')

    st.video('videos/OPTC17.mp4')
    st.write('Em seguida tentam entrar no bomb com duas ulimates fortes, '
             'mas estão em desvantagem e sem a Neon, '
             'para isolar espaço com a parede e acelerar o entry.')

    st.markdown('----')
    st.markdown('----')

    st.title('Lado de Defesa')
    st.markdown('##')
    st.write('No início do jogo apostaram em muitos stacks, e que até certo ponto foi bom, como por exemplo conseguiram ganhar o eco no 2º round, '
             'e chegaram a ter um placar de 4-2. Porém depois disso, os rounds ficaram fáceis de ler e a DRX conseguiu trabalhar muito bem em cima das falhas da OPTC,'
             ' até mesmo ganhando rounds em desvantagem.')
    st.markdown('##')
    st.markdown('##')

    st.subheader('Posicionamento da OPTC antes do plant')
    st.write('A ideia aqui é mostrar por onde a OPTC mais joga no mapa.'
             'Aqui podemos ter ideia de como o setup da defesa da Optic tem uma maior predominância em torno do Bomb B, '
             'deixando muitas vezes o Chamber cuidando do Bomb A. Outro ponto importante é a presença do Breach em ambos os Bombs.')
    st.image('imagens/OPTC def geral.png')

    st.markdown('----')
    st.markdown('##')

    st.title('-Pistol')
    st.markdown('##')

    st.image('imagens/OPTC def 1 P.png')
    st.video('videos/OPTC1.mp4')
    st.write('Stack Bomb B deixando apenas o Chamber cuidando de ambas entradas do Bomb A.'
             'O retake é feito em maioria pelas costas do time adversário, '
             'usando as utilitárias do Breach para ganhar espaço na garagem,'
             ' esse é um domínio importante pois tem como objetivo dificultar a resposta dos jogadores adversários que estão dentro do Bomb,'
             ' caso o domínio seja efetivado com vantagem. Apesar de ser um retake bem pensado, '
             'a resposta do time adversário de adiantar alguns confrontos e se reposicionar foi muito bem feito.')
    st.markdown('----')


    st.title('-ECO')
    st.markdown('##')

    st.image('imagens/OPTC def 2 E.png')
    st.video('videos/OPTC2.mp4')
    st.write('Stack em 4 agora no Bomb A, provavelmente pode ter sido uma leitura pensando no pistol ou até mesmo um anti-tático. '
             'Apesar de armas inferiores a OPTC consegue jogar muito bem em volta de utilitários, diminuindo a desvantagem, '
             'e consegue vantagem de maneira rápida e significativa.')
    st.markdown('----')

    st.title('-Anti-ECO')
    st.markdown('##')

    st.image('imagens/OPTC def 3 AE.png')
    st.video('videos/OPTC3.mp4')
    st.write('Sabendo que a DRX está jogando para orbes, devido a situação de desvantagem e da Neon adversária faltar apenas 2 orbes para sua ultimate,'
             ' novamente de início a OPTC opta por stack em um dos Bombs,possivelmente visando uma batida na parte superior do mapa para contestar uma das orbes, '
             'entretanto depois do primeiro contato em torno do Bomb A, eles formam um 2-3, e mantém buscando informação de maneira mais safe possível, '
             'principalmente no Bomb de menor quantidade. Quando conseguem a info em um dos Bombs a rotação é instantânea, '
             'pois já conseguiram muita informação do time adversário. ')
    st.markdown('##')
    st.markdown('##')

    st.title('-Armados')
    st.markdown('##')

    st.subheader('1º Padrão')
    st.image('imagens/OPTC def 4 AR.png')
    st.video('videos/OPTC4.mp4')
    st.write('Apesar do fake adversário forçar muitas utilitárias e conseguir abate, '
             'a OPTC ainda consegue sair com vantagem devido ao Chamber estar ancorado no outro Bomb,'
             ' resultando em uma maior facilidade do retake. '
             'Além disso tem o uso de ultimates por parte do Breach e Kay/o ajudando a conseguir dominar importantes espaços para o retake.')

    st.markdown('##')

    st.video('videos/OPTC5.mp4')
    st.write('Entretanto, mesmo numa situação de 3x1 por parte da OPTC, eles acabam pecando e escolhendo por duelos individuais,'
             ' sem trades e uma comunicação conjunta. O que faz que o Brimstone adversário consiga ganhar a situação de clutch, '
             'devido ao tempo que conseguiu comprar.')
    st.markdown('##')
    st.markdown('##')

    st.subheader('2º Padrão')
    st.image('imagens/OPTC def 5 AR.png')
    st.video('videos/OPTC6.mp4')
    st.write('Uso de utilitários na parte superior do Bomb B, e depois rápida rotação para o Bomb A, fazendo 2-3.')

    st.markdown('##')

    st.video('videos/OPTC7.mp4')
    st.write('Importante notar como o Brimstone e o Breach chegam somando já com utilitários na entrada da garagem,'
             ' isso faz com que a parte de baixo do time adversário, '
             'tenha que esperar e consequentemente não acompanhar a entrada pela parte de cima do Bomb.')

    st.markdown('##')

    st.video('videos/OPTC8.mp4')
    st.write('Apesar da boa rotação e resposta a OPTC acaba perdendo em uma situação '
             'de 5x3 devido a alguns duelos que a troca foi falha.')

    st.markdown('##')
    st.markdown('##')

    st.subheader('3º Padrão')
    st.image('imagens/OPTC def 6 AR.png')
    st.video('videos/OPTC9.mp4')
    st.video('videos/OPTC10.mp4')
    st.write('3-2 e sendo agressivo logo de início depois de perder 5 rounds consecutivos jogando sem agressividade. '
             'Conseguem vantagem numérica e tem bons ultimates para jogar retake, '
             'provável motivo para não redominar o espaço do Bomb A após a batida, na parte superior')

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
    st.table(stats_eco_optc.style.format(precision=0))
    st.markdown('##')

    st.subheader('5x4 & 4x5')
    st.image('imagens/OPTC extra 1.png')

with tab3:
    st.write('Aqui temos os stats individuais do time da OPTC. Como só está sendo analisado um único mapa,'
                 ' não tem como gerar média e quartis desses stats, então o gráfico acaba sendo apenas uma forma melhor de visualizar e comparar.')
    st.markdown('----')

    st.table(stats_indiv_optc.style.format(precision=2))

    st.sidebar.header('Filtros')

    var1 = st.sidebar.multiselect(
        'Selecione uma Variável (Stats Individual)',
        options=stats_indiv_optc.columns.unique()
    )

    stats_var1 = stats_indiv_optc.query(
        'ACS == @var1'
    )

    g_stats_indiv = px.bar(
        stats_indiv_optc.round(2),
        x='Players',
        y=var1,
        barmode='group',
        text_auto=True,
        color_discrete_sequence=['#0d0887', 'orangered', 'lightslategray'],
        width=800,
        height=500,
        template='plotly_white'
    )

    g_stats_indiv.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=(dict(showgrid=False))
    )
    g_stats_indiv.update_layout(font=dict(size=15))

    st.plotly_chart(g_stats_indiv)




