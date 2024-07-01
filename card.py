import flet as ft


def main(page:ft.Page):

#Alinhando os items
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_min_width = 500
    page.bgcolor = ft.colors.BLACK

    image = ft.Container(
        expand=4,
        border_radius=ft.border_radius.vertical(top=20),
        clip_behavior=ft.ClipBehavior.NONE,
        gradient=ft.LinearGradient(
            begin=ft.alignment.bottom_left,
            end=ft.alignment.top_right,
            colors=[ft.colors.BROWN,ft.colors.SURFACE]
        ),
        content=ft.Image(
            src= './bar1.png',
            scale=ft.Scale(scale=1.3)
        )
    )
    info = ft.Container(
        expand=2,
        padding=ft.padding.all(30),
        alignment=ft.alignment.center,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(value='LEVEL 4',color= ft.colors.ORANGE),
                ft.Text(
                    value='Barbaro',
                    weight=ft.FontWeight.BOLD,
                    size=30,
                    color=ft.colors.BLACK,
                ),
                ft.Text(value='A aparência do Bárbaro é a um homem com uma expressão irritada pronto para lutas. ',
                color=ft.colors.GREY,
                text_align=ft.TextAlign.CENTER)

                    
                
            ]
        )
    )
    skills = ft.Container(
        expand=1,
        padding=ft.padding.symmetric(horizontal=20),
        bgcolor=ft.colors.ORANGE,
        border_radius=ft.border_radius.vertical(bottom=20),
        content=ft.Row(
            controls=[
                ft.Column(
                    expand=1,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,             
                    controls=[
                        ft.Text(value='20',
                                color=ft.colors.WHITE,
                                weight=ft.FontWeight.BOLD,
                                size=25,),
                        ft.Text(value='DEFESA',
                                color=ft.colors.WHITE,
                                size='14', 
                    )]),
                    ft.VerticalDivider(opacity=0.5),
                    ft.Column(
                    expand=1,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,             
                    controls=[
                        ft.Text(value='15',
                                color=ft.colors.WHITE,
                                weight=ft.FontWeight.BOLD,
                                size=25,),
                        ft.Text(value='VELOCIDADE',
                                color=ft.colors.WHITE,
                                size='14' 
                    )]),
                    ft.VerticalDivider(opacity=0.5),
                    ft.Column(
                    expand=1,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,             
                    controls=[
                        ft.Text(value='170',
                                color=ft.colors.WHITE,
                                weight=ft.FontWeight.BOLD,
                                size=25,),
                        ft.Text(value='DANO',
                                color=ft.colors.WHITE,
                                size='14' 
                    )]),
            ]
        )
    )

    layout = ft.Container(
        clip_behavior=ft.ClipBehavior.NONE,
        height=600,
        width = 400,
        shadow=ft.BoxShadow(blur_radius=100,color=ft.colors.BROWN),
        border_radius=ft.border_radius.all(30),
        bgcolor=ft.colors.WHITE,
        content=ft.Column(
            spacing=0,
            controls=[
                image,
                info,
                skills,

            ]
        )




    )

    page.add(layout)
    #page.update() PAGE.ADD já contem o page.update()




if __name__ == '__main__':
    ft.app(target=main)

