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
Municipio = 'Urandi-BA'
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

# Ponto de partida

p0 = df.loc[0,'codigo']
lat0= df.loc[0,'lat']
long0 = df.loc[0,'long']
conf0 = df.loc[0,'conf']
az0 = df.loc[0,'az']
dist0 = df.loc[0,'dist']

cabecalho = f''' MEMORIAL DESCRITIVO

Imóvel: {imovel}							Comarca: {CNS}
Proprietário: {nome} C.P.F. nº {cpf}
Município/UF: {'Urandi-BA'}
Código INCRA: {ccir}					Matrícula: {matricula}
Área (ha): {area}					Perímetro: {perimetro}'''

inicio = f'''Inicia-se a descrição deste perímetro no vértice {p0}, 
com Latitude {lat0} N e Longitude {long0} S, '''

# variáveis temporárias
pn = 0
pn1 = 0
lat_n = 0
long_n = 0
conf_n = 0
azim = 0
dist_n = 0


# Acessando as informações do memorial



with open('./memorial.tex', 'a', encoding='utf-8' ) as f:
    f.write(inicio)
    for i in df.itertuples():
        f.write(f'''deste, segue confrontando com {i.conf}, com azimute geodésico de {i.az} e distância de 
{str(i.dist/100).replace('.',',')}m até o vértice {i.vert_fim} de Latitude {i.lat} N e Logitude {i.long} S;\n''')
    f.write(f''' encerrando esta descrição. Todas as coordenadas aqui descritas estão georrefereciadas ao Sistema 
Geodésico Brasileiro, e encontram-se representadas no sistema {src}, referenciadas ao Meridiano Central {mc}.
 Todos os azimutes e distâncias, área e perímetro foram calculados no Sistema Geodésico Local.''')