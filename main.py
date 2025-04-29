from flet import*
from encapsulamento.login1 import Login
from encapsulamento.index import Sistema


def main(page: Page):

    def route_change(route):
        page.views.clear()

        if page.route == "/":
            page.views.append(Login(page))
        elif page.route == "/index":
            page.views.append(Sistema(page))
        page.update()


    page.on_route_change = route_change
    page.go(page.route)
app(target=main)