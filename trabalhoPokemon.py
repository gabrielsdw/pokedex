import tkinter as tk
from tkinter import ttk
import requests
import urllib.request
from PIL import Image, ImageTk
from io import BytesIO


def mostraInfo():
    # Request para pegar a info do Pokemon
    nome = cmbOpcoes.get()
    pokemon = request("https://pokemon.danielpimentel.com.br/v1/pokemon/nome/" + nome)

    # Chamando os Labels na tela/inserindo as informações
    lblNome_Pokemon["text"] = pokemon["nome"].title()
    lblInfo["text"] = "Informações"
    lblEstatisticas["text"] = "Estatísticas"
    lblPeso["text"] = "Peso: {} Kg".format(pokemon["peso"]/1000, "Kg")
    lblAltura["text"] = "Altura: {} m".format(pokemon["altura"]/100, "m")
    lblTipo["text"] = "Tipo: "
    lblGeracao["text"] = "Geração: {}".format(pokemon["geracao"])
    lblHP["text"] = "HP: {}".format(pokemon["hp"])
    lblATK["text"] = "ATK: {}".format(pokemon["atk"])
    lblDEF["text"] = "DEF: {}".format(pokemon["def"])
    lblSpatk["text"] = "SPATK: {}".format(pokemon["spatk"])
    lblSpdef["text"] = "SPDEF: {}".format(pokemon["spdef"])
    lblSpeed["text"] = "Speed: {}".format(pokemon["speed"])
    lblNumero["text"] = "Número: {}".format(pokemon["numero"])
    lblEvolucoes["text"] = "Evoluções: {}".format(pokemon["evolucoes"])

    # Chamando e configurando as informações do frame
    frmFoto["borderwidth"] = 4
    frmFoto["relief"] = "solid"
    frmFoto["width"] = 212
    frmFoto["height"] = 241

    # Carregando Foto externa do Pokemon
    carregaFotoExterna(pokemon["img"])

    try:
        # Tentando pegar os tipos do Pokemon caso for composto
        # Pegando os tipos do Pokemon e inserindo no link
        tipo1, tipo2 = pokemon["tipo"].split(",")
        endTipo = "fotosTipos/"+tipo1+".png"
        endTipo2 = "fotosTipos/"+tipo2+".png"

        # Exibindo as fotos dos dois Tipos
        foto = tk.PhotoImage(file=endTipo)
        foto2 = tk.PhotoImage(file=endTipo2)
        lblFotoTipo.configure(image=foto)
        lblFotoTipo.image = foto
        lblFotoTipo2.configure(image=foto2)
        lblFotoTipo2.image = foto2
    except(ValueError):
        # Caso a tentativa acima não ter
        # sucesso pelo motivo do pokemon ter apenas um tipo
        tipo1 = pokemon["tipo"]
        endTipo = "fotosTipos/" + tipo1 + ".png"
        foto = tk.PhotoImage(file=endTipo)
        lblFotoTipo.configure(image=foto)
        lblFotoTipo.image = foto
        # Deixando a imagem do tipo 2 vazia
        lblFotoTipo2.configure(image=None)
        lblFotoTipo2.image = None
    finally:
        # Redirecionando o botão de pesquisa
        # após a exibição da foto do Pokemon
        btnPesquisar.place(x=265, y=420)


def carregaFotoExterna(endereco):
    # Baixando a imagem na internet
    u = urllib.request.urlopen(endereco)
    img_online = u.read()
    u.close()

    # Transformando a imagem online numa imagem local
    img_local = Image.open(BytesIO(img_online))
    img_local = img_local.resize((200, 229))  # Redimensionando
    img_local = ImageTk.PhotoImage(img_local)

    # Colocando a foto no Label
    lblFoto.configure(image=img_local)
    lblFoto.image = img_local
    lblFoto["background"] = "Light Gray"


# Pegando os nomes de todos os Pokemons e os inserindo em uma lista
def carregaNomes(lista: list):
    resp = request("https://pokemon.danielpimentel.com.br/v1/pokemon/lista")
    i = 0
    while i < len(resp):
        lista.append(resp[i]["nome"])
        i += 1
    return lista


def request(url: str):
    return requests.get(url).json()["pokemon"]


# Criando a lista com o nome de todos os pokemons
lista_Pokemons = list()
carregaNomes(lista_Pokemons)


# Configurações de Tela
janela = tk.Tk()
janela.title("Pokedéx")
janela["bg"] = "Red"
janela.geometry("580x500")


# Criando o Combobox e informando os Pokemons
cmbOpcoes = ttk.Combobox(janela)
cmbOpcoes.grid(column=1, row=0, padx=10, pady=10)
cmbOpcoes["values"] = lista_Pokemons


# Frames
frmFoto = tk.Frame(janela, borderwidth=0, relief="solid")
frmFoto.place(x=15, y=130)


# Labels Textos
lblPokemon = tk.Label(
    janela,
    text="Selecione um Pokemon:",
    bg="Red",
    font="Matiz, 12"
)
lblPokemon.grid(column=0, row=0, padx=10, pady=10)


lblNome_Pokemon = tk.Label(
    janela,
    text="",
    bg="Red",
    height=2,
    width=20,
    font=("Matiz", 18, "bold")
)
lblNome_Pokemon.place(x=-35, y=58)


lblInfo = tk.Label(
    janela,
    text="",
    bg="Red",
    height=3,
    width=20,
    font=("Matiz", 15, "bold")
)
lblInfo.place(x=345, y=48)


lblPeso = tk.Label(
    janela,
    text="",
    bg="Red",
    font=("Matiz", 11)
)
lblPeso.place(x=410, y=108)


lblAltura = tk.Label(
    janela,
    text="",
    bg="Red",
    font=("Matiz", 11)
)
lblAltura.place(x=410, y=128)


lblTipo = tk.Label(
    janela,
    text="",
    bg="Red",
    font=("Matiz", 11)
)
lblTipo.place(x=410, y=148)


lblGeracao = tk.Label(
    janela,
    text="",
    bg="Red",
    font=("Matiz", 11)
)
lblGeracao.place(x=410, y=168)


lblNumero = tk.Label(
    janela,
    text="",
    bg="Red",
    font=("Matiz", 11)
)
lblNumero.place(x=410, y=188)


lblEstatisticas = tk.Label(
    janela,
    text="",
    bg="Red",
    height=1,
    width=20,
    font=("Matiz", 15, "bold")
)
lblEstatisticas.place(x=345, y=208)


lblHP = tk.Label(
    janela,
    text="",
    bg="Red",
    font=("Matiz", 11)
)
lblHP.place(x=410, y=238)


lblATK = tk.Label(
    janela,
    text="",
    bg="Red",
    font=("Matiz", 11)
)
lblATK.place(x=410, y=258)


lblDEF = tk.Label(
    janela,
    text="",
    bg="Red",
    font=("Matiz", 11)
)
lblDEF.place(x=410, y=278)


lblSpatk = tk.Label(
    janela,
    text="",
    bg="Red",
    font=("Matiz", 11)
)
lblSpatk.place(x=410, y=298)


lblSpdef = tk.Label(
    janela,
    text="",
    bg="Red",
    font=("Matiz", 11)
)
lblSpdef.place(x=410, y=318)


lblSpeed = tk.Label(
    janela,
    text="",
    bg="Red",
    font=("Matiz", 11)
)
lblSpeed.place(x=410, y=338)


lblEvolucoes = tk.Label(
    janela,
    text="",
    bg="Red",
    font=("Matiz", 11, "bold")
)
lblEvolucoes.place(x=15, y=380)


# Labels Fotos
lblFoto = tk.Label(frmFoto, bg="Red")
lblFoto.place(x=0, y=0)

foto = tk.PhotoImage(file="fotosTipos/bug.png")
lblFotoTipo = tk.Label(janela, bg="Red")
lblFotoTipo.place(x=450, y=148)

foto2 = tk.PhotoImage(file="fotosTipos/grass.png")
lblFotoTipo2 = tk.Label(janela, background="Red")
lblFotoTipo2.place(x=480, y=148)

Emblema = Image.open("fotosTipos/e.png")
resized = Emblema.resize((100, 100))
fotoEmblema = ImageTk.PhotoImage(resized)
lblEmblema = tk.Label(janela, image=fotoEmblema, background="Red")
lblEmblema.place(x=480, y=400)


# Botões
btnPesquisar = tk.Button(
    janela,
    command=mostraInfo,
    text="Pesquisar",
    background="Black",
    foreground="Light Gray",
    font=("Matiz", 8)
)
btnPesquisar.grid(column=1, row=7, padx=10, pady=10)


janela.mainloop()