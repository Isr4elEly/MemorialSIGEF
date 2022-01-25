import pandas as pd

# Tabela 01 SIGEF - Vértices da parcela
df1 = pd.read_html('./vertices.html', encoding='utf-8')[0]

# Tabela 02 do SIGEF - Limites
df2 = pd.read_html('./limites.html', encoding='utf-8')[0]

# Juntando as tabelas

df = df1.join(df2)
df.rename(columns= {'Código':'codigo', 'Longitude':'long', 'Sigma Long. (m)': 'sigma_long', 'Latitude': 'lat', 'Sigma Lat. (m)': 'sigma_lat', 'Altitude (m)': 'alt', 'Sigma Altitude (m)':'sigma_alt', 'Método Posicionamento':'metodo','Do Vértice':'vert_ini','Ao Vértice':'vert_fim', 'Tipo':'tipo', 'Lado':'lado', 'Azimute':'az','Comprimento (m)':'dist', 'Confrontante':'conf'}, inplace=True)

# Determinação do pontos de partida e dados princiais
# variáveis do memorial
# Proprietario 
nome = 'JOSÉ APARECIDO SANTOS'
cpf  = '690.402.735-53'

# Imóvel
imovel = 'FAZENDA BARRO VERMELHO'
ccir = '000.019.168.386-2'
matricula = '3211'
CNS = '(01.017-3) Urandi - BA'
municipio = 'Urandi'
perimetro = '5.086,36 m'
area = '76,8515 ha'

# Técnico
Tecnico= 'EDIVALDO CARMO DE MEDEIROS'
fomacao = 'Técnico de Grau Médio em Agrimensura'
codigo = 'G1H'
conselho = '92412718172/MT'
art = '327453 - BA'

# Sistemas de Coordenadas
src = 'SIRGAS 2000'
mc ='-39°'


with open('./latex/cabecalho.tex', 'w', encoding='utf-8') as f:
    f.write(f'''
\\begin{{center}}
\LARGE {{MEMORIAL DESCRITIVO}}
\end{{center}}
\\begin{{tabular}}{{ll}}
\emph{{Imóvel: {imovel}}} & \emph{{Comarca: {CNS}}} \\\ 
\\emph{{Proprietário: {nome}}}&\\\ 
\emph{{UF: Ba}}& \emph{{Município: {municipio}}}\\\ 
\emph{{Código INCRA: {ccir}}}\hspace{{3cm}}	 & \emph{{Matrícula: {matricula}}}\\\ 
\emph{{Área ($ha$): {area}}} & \emph{{Perímetro ($m$): {perimetro}}}\\\ 
\end{{tabular}}''')


# Montando o memorial descritivo

with open('./latex/memorial.tex', 'a', encoding='utf-8' ) as f:
    
    for i in df.itertuples():
        if i.Index==0:
            f.write(f'''Inicia-se a descrição deste perímetro no vértice {i.codigo}, com Latitude {i.lat} N e Longitude {i.long} S; deste, segue confrontando com {str(i.conf).upper()}, com azimute geodésico de {i.az} e distância de {str(i.dist/100).replace('.',',')}m''')
        else:
            f.write(f''' até o vértice {i.codigo}, com Latitude {i.lat} N e Longitude {i.long} S; deste, segue confrontando com {i.conf}, com azimute geodésico de {i.az} e distância de 
{str(i.dist/100).replace('.',',')}m ''')
    f.write(f''' até o vértice {df.loc[0,'codigo']} encerrando esta descrição. Todas as coordenadas aqui descritas estão georrefereciadas ao Sistema Geodésico Brasileiro, e encontram-se representadas no sistema {src}, referenciadas ao Meridiano Central {mc}. Todos os azimutes e distâncias, área e perímetro foram calculados no Sistema Geodésico Local.''')

with open('./latex/main.tex', 'w', encoding='utf-8') as f:
    f.write('''\documentclass[10.8pt, a4paper]{article}
\input{config}%pacotes e configurações

\\begin{document}
\input{cabecalho}
\\vspace{1cm}
   % corpo do memorial

\input{memorial.tex}

\\vspace{1cm}
\\begin{flushright}
   \emph{Urandi-BA, xx de xxxx de 20xx}
\end{flushright}
\\vspace{0.5cm}
\input{assinatura}
\end{document}     ''')