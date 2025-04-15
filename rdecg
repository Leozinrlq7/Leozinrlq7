import flet as ft

def main (page:ft.Page):
    page.window_center()
    page.window.width= 1200
    page.window.height= 650
    page.bgcolor= "#FFFFFF"
    page.window.maximizable = False
    page.window.resizable = False
    page.padding = 0
    page.window_title_bar_hidden = True
   
    r1 =  ft.Container (width=200, height=650, bgcolor='#000000', padding = 20,
                        content= ft.Column([
                            ft.Row([
                            ft.IconButton(ft.icons.HOME, icon_color="#FFFFFF", icon_size=30, on_click=lambda e:ini(e)),
                            ft.Text("Inicio", color= "#FFFFFF"),
                        ]),
                            
                            ft.Row([
                            ft.IconButton(ft.icons.PEOPLE, icon_color="#FFFFFF", icon_size=30, on_click=lambda e:funcaoalunos(e)),
                            ft.Text("Alunos", color= "#FFFFFF")
                        ]),
                            ft.Row([
                            ft.IconButton(ft.icons.FAMILY_RESTROOM, icon_color="#FFFFFF", icon_size=30),
                            ft.Text("Responsáveis", color= "#FFFFFF")
                        ]),
                            ft.Row([
                            ft.IconButton(ft.icons.ATTACH_MONEY, icon_color="#FFFFFF", icon_size=30),
                            ft.Text("Financeiro", color= "#FFFFFF")
                        ]),
                            ft.Row([
                            ft.IconButton(ft.icons.SCHOOL, icon_color="#FFFFFF", icon_size=30),
                            ft.Text("Turma", color= "#FFFFFF")
                        ]),
                            ft.Row([
                            ft.IconButton(ft.icons.MENU_BOOK, icon_color="#FFFFFF", icon_size=30),
                            ft.Text("Disciplinas", color= "#FFFFFF")
                        ]),

                            ft.Container(height=190),

                            ft.Divider(color="#ffffff"),


                            ft.Row([
                            ft.IconButton(ft.icons.EXIT_TO_APP_SHARP, icon_color="#FFFFFF", icon_size=30, on_click=lambda e:sair(e)),
                            ft.Text("Sair", color= "#FFFFFF")
                        ])
                        ])
                        )
    
    inicio = ft.Container(width=965, height=620,  padding = 20,
                       
                        content= ft.Row([
                            ft.Container (width=200, height=200, bgcolor='#000000', padding = 20, border_radius=10),
                            ft.Container (width=200, height=200, bgcolor='#000000', padding = 20, border_radius=10),
                            ft.Container (width=200, height=200, bgcolor='#000000', padding = 20, border_radius=10),
                            ft.Container (width=200, height=200, bgcolor='#000000', padding = 20, border_radius=10)


                        ], alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.START)
                        )
    

    alunos = ft.Container(width=965, height=620,  padding = 20,
                       
                        content= ft.DataTable(columns=[
                            ft.DataColumn(ft.Text("Nome",color='#000000')),
                            ft.DataColumn(ft.Text("Matrícula",color='#000000')),
                            ft.DataColumn(ft.Text("Turma",color='#000000')),
                            ft.DataColumn(ft.Text("Ações",color='#000000')),    
                        ]))
                
    

    responsaveis = ft.Container(width=965, height=620, bgcolor='#000000', padding = 20,
                       
                        content= ft.Text("Sair", color="#FFFFFF", size = 15 )
                        )
    

    financeiro = ft.Container(width=965, height=620, bgcolor='#000000', padding = 20,
                       
                        content= ft.Text("Sair", color="#FFFFFF", size = 15 )
                        )
    

    turma = ft.Container(width=965, height=620, bgcolor='#000000', padding = 20,
                       
                        content= ft.Text("Sair", color="#FFFFFF", size = 15 )
                        )
    

    disciplina = ft.Container(width=965, height=620, bgcolor='#000000', padding = 20,
                       
                        content= ft.Text("Sair", color="#FFFFFF", size = 15 )
                        )
    



    def funcaoalunos(e: ft.ControlEvent):
        page.remove(r1)
        page.add(ft.Row([r1, alunos]))

    def ini(e: ft.ControlEvent):
        page.remove(r1)
        page.add(ft.Row([r1, inicio]))
    

    def sair(e):
        page.window_close()

        page.update()



    page.add(r1)
ft.app(target = main)
