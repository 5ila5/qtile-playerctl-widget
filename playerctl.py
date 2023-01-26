"""
Widget requirements: pyxdg.
"""
import re
import subprocess
import cairocffi

from libqtile.log_utils import logger
import math
import cairo
import os
from libqtile import images
from xdg.IconTheme import getIconPath

from libqtile import bar
from libqtile.widget import base



#__all__ = [
#    'playerctl',
#]

class Playerctl(base._TextBox):
    orientations = base.ORIENTATION_HORIZONTAL
    defaults = [
        ("list_type", 0, "0 all Applications, 1 Blacklist,2 Whitelist"),
        ("list",[],"White Blacklist dependent on list_type. playerctl player name \"all\" Black/Whitelists the general Controll"),
        ("update_interval", 0.5, "Update time in seconds."),
        ("icon_color", "FFFFFF", "Color of Play Pause Next... Icons"),
        ("show_next", True, "Show next Track button"),
        ("show_prev", True, "Show previous Track button"),
        ("controll_multiple",True, "shows Icon with the currently selected player if False Controlls always all Player at once"),
        ("icon_width", (20,30), "Width of Play/Pause(1) and Next/Pref(2) Buttons"),
        ("distance", 10, "distance Betwen Icons distance multiplier*icon_width Play/Pause"),
        ("icon_order", (1,2,3), "Order of Icons (1,2,3) represents prev -> Pl/pause -> next"),
        ("top_margin", 3, "Distance between top of the Bar Icon"),
        ("bottom_margin", 3, "Distance between bottom of the Bar Icon"),
        ("player_icons",{},"path to icons format {\"player_name\": \"source to icon\"}"),
        ("app_player_icons",{"spotifyd":"spotify"},"Replaces Icon of first_app with the second Default: replaces Spotifyd(not found) icon with spotify Icon (if installed)"),
        
        ("default_icon","~/Pictures/not_found.png","Default icon if no icon for the given Application found"),

        ("showVolume",True,"show Playervolume like the Volume Widget"), #pactl list short clients |||| pactl list short sink-inputs
    ]

    def __init__(self, **config):



        #base._TextBox.__init__(self, '', **config)
        super().__init__(**config)

        self.add_defaults(Playerctl.defaults)
        self.surfaces = {}
        self.player=[]
        self.status=False
        self.selected=0
        self.click_area=[[0,0],[0,0],[0,0]]
        self.show_player_icon = False


        self.icon_height=0
        self.default_icon=os.path.expanduser(self.default_icon)

        
        
        


        
        
    def calculate_length(self):

        self.icon_height =self.bar.height-self.top_margin-self.bottom_margin
        add_icons =0
        if self.show_prev and self.show_next:
            add_icons =2
        elif self.show_prev or self.show_next:
            add_icons =1
        
        width = self.icon_width[0] + add_icons * (self.icon_width[1] +self.distance)
        width +=  (self.icon_height +self.distance) if self.show_player_icon else 0
        if self.player==[]:
            width=0
        icon_order=self.icon_order
        icon_width=list(self.icon_width)
        #icon_width=self.icon_width

        icon_width[0]+=self.distance
        icon_width[1]+=self.distance

        click_area = click_area=[[0,0],[0,0],[0,0]]

        if self.show_prev:
            if icon_order[0] == 1:
                click_area[0][1] = icon_width[1]
            
            elif icon_order[1] ==1:
                if icon_order[0] == 3:
                    if self.show_next:
                        click_area[0][0] = icon_width[1]
                        click_area[0][1] = icon_width[1]*2
                    else:
                        click_area[0][1] = icon_width[1]
                    
                elif icon_order[0] == 2:
                    click_area[0][0] = icon_width[0]
                    click_area[0][1] = icon_width[1]+icon_width[0]

            elif icon_order[2] ==1:
                click_area[0][1]=width
                if self.show_next or self.show_next:
                    click_area[0][0]+=icon_width[1]
                    if self.show_next and self.show_next:
                        click_area[0][0]+=icon_width[1]


        if icon_order[0] ==2:
            click_area[1][1] = icon_width[0]
        elif icon_order[1] ==2:
            click_area[1][1] = icon_width[0]

            if (icon_order[0]==1 and self.show_prev) or (icon_order[0]==3 and self.show_next):
                click_area[1][1] += icon_width[1]
                click_area[1][0] = icon_width[0]


        elif icon_order[2] == 2:
            click_area[1][1] = icon_width[0]
            if self.show_next or self.show_next:
                click_area[1][0]+=icon_width[1]
                click_area[1][1]+=icon_width[1]

                if self.show_next and self.show_next:
                    click_area[1][0]+=icon_width[1]
                    click_area[1][1]+=icon_width[1]

        
        if self.show_next:
            if icon_order[0] == 3:
                if self.show_next:
                    click_area[2][1] = icon_width[1]
            elif icon_order[1] ==3:
                click_area[2][1] = icon_width[1]
                if icon_order[0] == 1:
                    if self.show_prev:
                        click_area[2][1]+= icon_width[1]
                        click_area[2][0]+= icon_width[1]

                elif icon_order[0] == 2:
                    click_area[2][0] = icon_width[0]
                    click_area[2][1] = icon_width[1]+icon_width[0]

            elif icon_order[2] ==3:
                click_area[2][1]=width
                click_area[2][0] = icon_width[0]
                if self.show_prev:
                    click_area[2][0]+=icon_width[1]

        if self.show_player_icon:
            for i in range(3):
                for k in range(2):
                    click_area[i][k]+=self.icon_height+self.distance
        
        self.click_area = click_area

        return int(width)


    def _configure(self, qtile, bar):
        #base._Widget._configure(self, qtile, bar)
        super()._configure(qtile, bar)

         


        """self.textlayout = self.drawer.textlayout(
                     "Text",
                     "fffff",       # Font colour
                     "sans",        # Font family
                     12,            # Font size
                     None,          # Font shadow
                     markup=False,  # Pango markup (False by default)
                     wrap=True      # Wrap long lines (True by default)
                     )"""

    def timer_setup(self):
        self.timeout_add(self.update_interval, self.update)

    def lookup_icon(self,name,search_name=""):
        #logger.warning("name:"+str(name)+" SearchName: "+str(search_name))
        if search_name=="": search_name=name
        self.player_icons[name] = None
        self.player_icons[name] = getIconPath(search_name)
        if self.player_icons[name] is None:
            self.player_icons[name] = self.default_icon


    def update_player_icons(self):
        #logger.warning(str(self.app_player_icons))
        #not_found_folder = find_img("not_found")
        if (not self.default_icon) or (not os.path.isfile(self.default_icon)):
            self.default_icon = None
        
        for name in self.player:
            search_name=name
            if name in self.app_player_icons:
                search_name = self.app_player_icons[name]
            self.lookup_icon(name,search_name=search_name)
            if self.player_icons[name] == self.default_icon:
                self.lookup_icon(name,search_name=search_name.split(".")[0])


        for img_name, iconfile in self.player_icons.items():
            if iconfile:
                try:
                    img = cairocffi.ImageSurface.create_from_png(iconfile)
                except cairocffi.Error:
                    #logger.exception('Error loading icon for application "%s" (%s)', img_name, iconfile)
                    return
                
                input_width = img.get_width()
                input_height = img.get_height()

                sp = input_height / (self.icon_height)
                width = int(input_width / sp)

                imgpat = cairocffi.SurfacePattern(img)
                scaler = cairocffi.Matrix()
                scaler.scale(sp, sp)
                scaler.translate(0, -self.top_margin)
                imgpat.set_matrix(scaler)

                imgpat.set_filter(cairocffi.FILTER_BEST)
                self.surfaces[img_name] = imgpat
                #self.icons_widths[img_name] = width

    

    def getLenth(self):
        return self._length
        

    def button_press(self, x, y, button):

        if button in range(1,3):
            if self.click_area[0][0]<=x and x<self.click_area[0][1]:
                self.prev_track()
            if self.click_area[1][0]<=x and x<self.click_area[1][1]:
                self.play_pause_toggle()
            if self.click_area[2][0]<=x and x<self.click_area[2][1]:
                self.next_track()
        elif button==4 and self.controll_multiple:
            self.selected = (self.selected +1) if self.selected< len(self.player)-1 else 0
        elif button==5 and self.controll_multiple:
            self.selected = (self.selected -1) if self.selected> 0 else len(self.player) -1
        if self.selected<0: self.selected=0


        self.update(button=True)
        self.draw()



    def update(self,button=False):
        status= self.get_status()
        if status != self.status:
            self.status=status
            self._update_drawer()
            self.draw()
            self.bar.draw()
        if not button:
            self.timeout_add(self.update_interval, self.update)

    def to_rads(self, degrees):
        return degrees * math.pi / 180.0


    def _update_drawer(self):
        self.drawer.clear(self.background or self.bar.background)
        '''if not self.status:
            self.text='▶'
        elif self.status:
            self.text = '='
        if self.player == []:
            self.text = "no Player"
        '''
    def get_player(self):
        command = self.create_command('player')
        callOut = self.call_process(command)
        if callOut == ""or callOut == "No players found":
            self.selected=0
            self.player=[]
            return -1

        player = ["all"]
        player.extend(list(filter(None, (callOut.split("\n")))))
        
        if self.list_type==1:
            for blacklisted in self.list:
                if blacklisted in player:
                    player.remove(blacklisted)
        elif self.list_type==2:
            new_player=[]#["all"]
            for whitelisted in self.list:
                if whitelisted in self.list:
                    new_player.append(whitelisted)
            player = new_player


        if player != self.player:
            self.player = player
            if self.controll_multiple:
                self.update_player_icons()
            self.bar.draw()

        if self.selected > len(player):
            self.selected=0


    def get_status(self):
        if self.get_player()==-1:
            return -1
        command = self.create_command('status')
        
        try:
            callOut = self.call_process(command)
        except Exception as e:
            return -1


        if "playing" in callOut.lower():
            return True 
        else:
            return False



    def create_command(self, command_type, controll=""):
        command = ["playerctl"]

        if command_type == 'player':

            command.append("-l")

        elif command_type == 'status':
            command.append("status")
            if self.player[self.selected]=="all":
                command.extend(["-a",])
            else:
                command.extend(["-p", self.player[self.selected]])
        elif command_type == "ctl":
            command.append( controll)
            if self.player[self.selected]=="all":
                command.append("-a")
            else:
                command.extend(["-p",self.player[self.selected]])
        return command



    def draw_play_pause(self,startx):
        self.drawer.ctx.new_sub_path()

        if self.status: #Draw PAUSE
            self.drawer.ctx.rectangle(startx,self.top_margin,self.icon_width[0]/3 ,self.icon_height)
            self.drawer.ctx.rectangle(startx+(self.icon_width[0]/3)*2,self.top_margin,self.icon_width[0]/3 ,self.icon_height)
        else: #DRAW PLAY
            self.drawer.ctx.move_to(startx,self.top_margin)
            self.drawer.ctx.line_to(startx+self.icon_width[0],self.icon_height/2+self.top_margin)
            self.drawer.ctx.line_to(startx,self.icon_height+self.top_margin)
        self.drawer.ctx.fill()

    def draw_next(self,startx):
        one_arrow_width = self.icon_width[1]/2
        self.drawer.ctx.new_sub_path()
        self.drawer.ctx.move_to(startx,self.top_margin)
        self.drawer.ctx.line_to(startx+one_arrow_width,self.icon_height/2+self.top_margin)
        self.drawer.ctx.line_to(startx,self.icon_height+self.top_margin)
        startx+=one_arrow_width
        self.drawer.ctx.move_to(startx,self.top_margin)
        self.drawer.ctx.line_to(startx+one_arrow_width,self.icon_height/2+self.top_margin)
        self.drawer.ctx.line_to(startx,self.icon_height+self.top_margin)
        self.drawer.ctx.fill()
        
    def draw_prev(self,startx):
        self.drawer.ctx.new_sub_path()
        one_arrow_width = self.icon_width[1]/2

        self.drawer.ctx.move_to(startx+one_arrow_width,self.top_margin)
        self.drawer.ctx.line_to(startx,self.icon_height/2+self.top_margin)
        self.drawer.ctx.line_to(startx+one_arrow_width,self.icon_height+self.top_margin)
        startx+=one_arrow_width
        self.drawer.ctx.move_to(startx+one_arrow_width,self.top_margin)
        self.drawer.ctx.line_to(startx,self.icon_height/2+self.top_margin)
        self.drawer.ctx.line_to(startx+one_arrow_width,self.icon_height+self.top_margin)
        self.drawer.ctx.fill()

        
    def draw(self):
        self.drawer.clear(self.background or self.bar.background)
        if self.player==[]:
            return -1
        self.drawer.ctx.set_fill_rule(cairo.FILL_RULE_EVEN_ODD)          
        #self.drawer.set_source_rgb("666666")



        startx=0
        self.show_player_icon=False
        if self.controll_multiple:
            if self.player[self.selected] in self.surfaces:
                img = self.surfaces[self.player[self.selected]] 
                self.drawer.ctx.new_sub_path()

                self.drawer.ctx.set_source(img)
                self.drawer.ctx.paint()
                #self.drawer.ctx.clip_preserve()
                startx+=self.icon_height+self.distance
                self.show_player_icon=True


        self.drawer.set_source_rgb(self.icon_color)

        for i in self.icon_order:
        
            if i==1 and self.show_prev:
                self.draw_prev(startx)
                startx+=int(self.icon_width[1]+self.distance)

            if i==2:
                self.draw_play_pause(startx)
                startx+=int(self.icon_width[0]+self.distance)


            if i==3 and self.show_next:
                self.draw_next(startx)
                startx+=int(self.icon_width[1]+self.distance)









        self.drawer.draw(offsetx=self.offsetx, width=self.width)

        




    def play_pause_toggle(self):
        if self.player==[]:
            return -1

        cmd =self.create_command('ctl',controll="pause" if self.status else "play")
        #self.status = not self.status

        self.call_process(cmd)


    def prev_track(self):
        cmd =self.create_command('ctl',controll="previous")
        self.call_process(cmd)

    def next_track(self):
        cmd =self.create_command('ctl',controll="next")
        self.call_process(cmd)
