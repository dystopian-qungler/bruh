import curses
def main(stdscr):
    curses.curs_set(0)
    stdscr.timeout(100)
    curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_YELLOW,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(4,curses.COLOR_CYAN,curses.COLOR_BLACK)
    curses.init_pair(5,curses.COLOR_BLUE,curses.COLOR_BLACK)
    curses.init_pair(6,curses.COLOR_MAGENTA,curses.COLOR_BLACK)
    sh,sw = stdscr.getmaxyx()
    colour = 1
    btn_press = -1
    text = ["#####  #####  #    # #    # ","#    # #    # #    # #    # ","#####  #    # #    # ###### ","#    # #####  #    # #    # ","#    # #   #  #    # #    # ","#####  #    #  ####  #    # "]
    while(btn_press==-1): #loop ends when any keyboard input is detected
        for line in text:
            stdscr.addstr(sh//2-3+text.index(line),sw//2-14,line,curses.color_pair(colour))
        colour += 1
        if(colour==7): colour = 1 #loops back
        btn_press = stdscr.getch()
curses.wrapper(main)
