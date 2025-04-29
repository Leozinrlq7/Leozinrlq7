from flet import*
from conexao import*
from encapsulamento.login1 import*


def main (page:Page):
    page.window_center()
    page.window.width= 1200
    page.window.height= 650
    page.bgcolor= "#FFFFFF"
    page.window.maximizable = False
    page.window.resizable = False
    page.padding = 10


    txt= TextField(label="Digite o nome")
    tx= TextField(label="Digite a turma")
    b = FilledButton(text="Salvar", on_click=lambda e:create(e))
    te = Text("", size=50)

    def create(e):
        nome = txt.value
        turma = tx.value
        txt.value=""

        if nome and turma:
            conn, status = conectardb()
            if conn:
                result = concreate(conn,nome, turma)
                te.value=result
                te.value= "Nome inserido"
                conn.close()
            else:
                te.value=status
        else:
            te.value= "Por favor, insira seu nome"

        page.update()





    page.add(txt, tx,b, te)
app(target = main)