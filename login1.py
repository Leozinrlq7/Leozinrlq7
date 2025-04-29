from flet import*
from encapsulamento.index import*

def main(page: Page):
    page.window.center()
    page.window.width = '800'
    page.window.height = '500'
    page.padding= 0
    page.window.maximizable = False
    page.window.resizable = False
    page.window_title_bar_hidden = True


    def index(e):
    
     
     
        
        page.update()
    #Logica de transição de página
    def um(e):
        telalogin.visible=True
        telacadastro.visible=False

        page.update()

    def dois(e):
        telacadastro.visible=True
        telalogin.visible=False
        page.update()

    #Objetos tela de login

    tlogin=Text("Login", size=30, weight="Bold",)


    tacresent=Text("Ou faça login no seu email", size=12)


    tacresent2=CupertinoButton(text="Esqueci minha senha",color=colors.BLACK)


    textoemail=TextField(label= "E-mail", border_radius=15,autofocus=True, border_color="Black",cursor_color=colors.BLACK,label_style=TextStyle(color=colors.BLACK), )


    textosenha=TextField(label= "Senha", border_radius=15, border_color="Black",cursor_color=colors.BLACK,label_style=TextStyle(color=colors.BLACK),password=True,can_reveal_password=True )


    botaoentrar=FilledButton(text="Entrar", on_click=index,style=ButtonStyle(bgcolor="white", color=colors.BLACK))


    botaologin=FilledButton(text="Entrar",style=ButtonStyle(bgcolor=colors.BLACK))


    iconegoogle=Image(src="iconegoogle.png",width=20,height=20,
                        fit=ImageFit.COVER)


    iconefacebook=Image(src="facebook.png",width=25, height=25,
                        fit=ImageFit.COVER
    )


    iconegithub=Image(src="github.png",width=25, height=25,
                        fit=ImageFit.COVER
    )


    iconelikedin=Image(src="linkedin.png",width=25, height=25,
        fit=ImageFit.COVER
    )


    textoolaamigo=Text("Olá, amigo!", size=30, weight="Bold",color=colors.WHITE, bgcolor="Black")

   
    textoregistreconta=Text("Registre-se com seus dados pessoais \n para usar todos os recursos do site", size=12,color=colors.WHITE)






    #Objetos tela de cadastro
    botaocadastro=FilledButton(text="Entrar", on_click=um,style=ButtonStyle(bgcolor="white", color=colors.BLACK))


    createaccount=Text("Criar uma conta", size=30, weight="Bold",)


    oudigite=Text("Ou use seu e-mail para registro", size=12)


    txtvazio1=TextField(label= "Nome", width=250,height=40,border_radius=10,autofocus=True, border_color="Black",cursor_color=colors.BLACK,label_style=TextStyle(color=colors.BLACK), )
  

    txtvazio2=TextField(label= "E-mail", width=250,height=40,border_radius=10,autofocus=True, border_color="Black",cursor_color=colors.BLACK,label_style=TextStyle(color=colors.BLACK), )


    textosenhalogin=TextField(label= "Senha",width=250, height=40,border_radius=10, border_color="Black",cursor_color=colors.BLACK,label_style=TextStyle(color=colors.BLACK),password=True,can_reveal_password=True )

    botaoentrarblack=FilledButton(text="Entrar", on_click=dois,style=ButtonStyle(bgcolor="black", color=colors.WHITE))

    encapsulamentodetxtvazio=Column([txtvazio1,txtvazio2,textosenhalogin,botaoentrarblack],alignment=MainAxisAlignment.CENTER,horizontal_alignment=CrossAxisAlignment.CENTER,
        spacing=15)


    botaoentrar=FilledButton(text="Entrar", on_click=dois,style=ButtonStyle(bgcolor="white", color=colors.BLACK))



    textowelcome=Text("Bem vindo de volta!", size=30, weight="Bold",color=colors.WHITE, bgcolor="Black")


    textorecursoscompletos=Text("       Insira seus dados pessoais \n para usar todos os recursos do site", size=12,color=colors.WHITE)







    encapsulamentodeicones=Row([iconegoogle,iconefacebook, iconegithub,iconelikedin],alignment=MainAxisAlignment.CENTER,
        spacing=20)
    encapsulamentode1=Column([textoolaamigo, textoregistreconta, botaoentrar],alignment=MainAxisAlignment.CENTER,horizontal_alignment=CrossAxisAlignment.CENTER,
        spacing=20)
    
    encapsulamentode2=Column([textowelcome, textorecursoscompletos, botaocadastro],alignment=MainAxisAlignment.START,horizontal_alignment=CrossAxisAlignment.CENTER,
        spacing=20)
    #Container de construção
    telalogin=Row([

            Container(width=395, height=495,padding=50,content=


                      Column([tlogin,encapsulamentodeicones,tacresent,textoemail, textosenha,tacresent2,botaologin

                              ],alignment=MainAxisAlignment.CENTER, horizontal_alignment=CrossAxisAlignment.CENTER)
                      ),

            Container(width=395, height=495, bgcolor="black", border_radius=border_radius.only(top_left=170, bottom_left=170),
                      content=Column([encapsulamentode1

                              ],alignment=MainAxisAlignment.CENTER, horizontal_alignment=CrossAxisAlignment.CENTER)
                      )

    ])

    telacadastro=Row([

               Container(width=395, height=495, bgcolor="black",padding=50,border_radius=border_radius.only(top_right=170, bottom_right=170),

                      content=Column([encapsulamentode2

                              ],alignment=MainAxisAlignment.CENTER, horizontal_alignment=CrossAxisAlignment.CENTER)
                      ),

            Container(width=395, height=495 , padding=60,content=


                      Column([createaccount,encapsulamentodeicones,oudigite,encapsulamentodetxtvazio

                              ],alignment=MainAxisAlignment.START, horizontal_alignment=CrossAxisAlignment.CENTER)



                      )
     

    ])

    sair=FilledButton(text="Entrar", on_click=dois,style=ButtonStyle(bgcolor="white", color=colors.BLACK))


    page.add(telalogin,telacadastro)

app(main)