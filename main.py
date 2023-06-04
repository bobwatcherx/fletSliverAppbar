from flet import *


def main(page:Page):
    page.window_width= 300
    page.window_height = 600
    page.padding = 0
    page.spacing = 0

    # AND NOW I WILL CREATE FLOATING ACTION BUTTON
    page.floating_action_button = FloatingActionButton(
        icon="add",bgcolor="yellow",
        shape=CircleBorder(),

        # SET OFFSET IF YOU SCROLL AFTER 315
        offset = transform.Offset(0,0),
        animate_offset=animation.Animation(400,"easeIn")


        )



    # AND NOW I CREATE NAVBAR SHOW IF YOU SCROLL
    # after 315
    navbarscroll = Card(
        elevation=30,
        # HIDE IF not under 315
        visible=False,
        content=Container(
        bgcolor="yellow",
        padding=15,
        content= Row([
            Text("my Sliver ",size=25,weight="bold"),
            Icon(name="home",size=25)

            ],alignment="spaceBetween")
        )
        )

    def showscroll(e:OnScrollEvent):
        # YOU CAN CHECK e.pixes in you terminal
        # this based on e.pixels if large then my sliver smal
        print(e)
        if e.pixels > 0 :
            scroll_factor = min(1,e.pixels / 100)
            new_size = 60 - (scroll_factor * 35)

            # AND SET my sliver text to new_size
            myappbar.content.size = new_size


            # AND DETECT IF YOU WANT VALUE 315
            # then run style
            # 315 is optional  you can change if you like
            if e.pixels >= 315:
                print(myappbar.content.size)
                navbarscroll.visible = True
                page.floating_action_button.offset = transform.Offset(0,3)
            else:
                navbarscroll.visible = False
                page.floating_action_button.offset = transform.Offset(0,0)

        page.update()


    page.overlay.append(navbarscroll)

    myappbar = Container(
        width=page.window_width,
        height=350,
        padding=5,
        bgcolor="yellow",
        # AND I SET TEXT my sliver to left bottom
        alignment=alignment.bottom_left,
        content=Text("my sliver",
            size=60,weight="bold"
            )
        )

    mylist = Container(
        border_radius=30,
        width=page.window_width,
        bgcolor="white",
        padding=10,
        content=Column()
        )

    # NOW CREATE RANDOM NUMBER FOR mylist
    for x in range(1,40):
        mylist.content.controls.append(
            Text(f"data - {x}",size=25)
            )


    page.add(
        # NOW I BUILD SCROLL DETECTION IN COLUMN
        Container(
            width=page.window_width,
            height=page.window_height,
            content=Column([
                myappbar,
                # AND NOW FOR SCROLL
                # i will create fake data loop
                mylist


                ],scroll="always",
                on_scroll=showscroll
                )
            )

        )

flet.app(target=main)
