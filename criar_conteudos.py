import os

estrutura = {
    "matematica": {
        "basico": [
            "adicao",
            "subtracao",
            "multiplicacao",
            "divisao",
            "fracoes",
            "numeros_inteiros",
            "potenciacao",
            "radiciacao"
        ],
        "intermediario": [
            "equacoes_1_grau",
            "equacoes_2_grau",
            "produtos_notaveis",
            "fatoracao",
            "sistemas_lineares",
            "inequacoes"
        ],
        "avancado": [
            "funcoes",
            "logaritmos",
            "progressao_aritmetica",
            "progressao_geometrica",
            "trigonometria",
            "matrizes",
            "determinantes"
        ]
    },
    "fisica": {
        "basico": [
            "cinematica",
            "movimento_uniforme",
            "movimento_uniformemente_variado",
            "leis_de_newton",
            "trabalho_e_energia"
        ],
        "intermediario": [
            "quantidade_de_movimento",
            "impulso",
            "hidrostatica",
            "termodinamica"
        ],
        "avancado": [
            "ondas",
            "optica",
            "eletrodinamica",
            "fisica_moderna"
        ]
    }
}

BASE_DIR = "conteudos"

def criar_estrutura():
    for materia, niveis in estrutura.items():
        for nivel, topicos in niveis.items():
            pasta = os.path.join(BASE_DIR, materia, nivel)
            os.makedirs(pasta, exist_ok=True)

            for topico in topicos:
                caminho = os.path.join(pasta, f"{topico}.txt")
                if not os.path.exists(caminho):
                    with open(caminho, "w", encoding="utf-8") as f:
                        f.write(
                            f"{topico.replace('_', ' ').title()}\n\n"
                            "📘 Teoria:\n\n"
                            "✏️ Exemplos:\n\n"
                            "📝 Exercícios:\n"
                        )

if __name__ == "__main__":
    criar_estrutura()
    print("Estrutura de conteúdos criada com sucesso!")
