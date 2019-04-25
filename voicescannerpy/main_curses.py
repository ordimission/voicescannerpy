from core.command.ReadImageCommand import ReadImageCommand
from core.command.SayTextCommand import SayTextCommand
from core.command.SayTextPyttsxCommand import SayTextPyttsxCommand
from core.command.ScanImageCommand import ScanImageCommand
import curses
stdscr = curses.initscr()
#curses.cbreak()
curses.noecho()
#curses.keypad(True)

goon = 1
paragraphs = ""
index = 0
image_path = "/tmp/image_test.jpg"
scanner = "brother"
engine = "picotts"

while goon:
    key = stdscr.getch()
    if key == curses.KEY_EXIT or key == curses.KEY_BREAK:
        print("Quit")
        goon = 0
    if key == curses.KEY_ENTER:
        SayTextCommand({"text": "Lecture en cours", "engine": engine}).execute()
        ScanImageCommand({"path": image_path, "scanner": scanner, "mode": "color"}).execute()
        paragraphs = ReadImageCommand({"path": image_path, "lang": "fr_FR"}).execute()
        SayTextCommand({"text": str(len(paragraphs)) + " paragraphes", "engine": engine}).execute()
        print("Scan " + str(len(paragraphs))+ " paragraphes")
    if key == curses.KEY_SPACE:
        SayTextCommand({"text": "position " + str(index+1) + " sur " + str(len(paragraphs)), "engine": engine}).execute()
        print("Space " + "position " + str(index+1) + " sur " + str(len(paragraphs)))
    if key == curses.KEY_LEFT:
        if index > 0:
            index = index - 1
        SayTextCommand(
            {"text": paragraphs[index], "engine": engine}).execute()
        print("Left " + paragraphs[index])
    if key == curses.KEY_RIGHT:
        if index < len(paragraphs) - 1:
            index = index + 1
        SayTextCommand({"text": paragraphs[index], "engine": engine}).execute()
        print("Right " + paragraphs[index])
    if key == curses.KEY_DOWN:
        SayTextCommand({"text": paragraphs[index], "engine": engine}).execute()
        print("Down " + paragraphs[index])
    if key == curses.KEY_FIRST or key == curses.KEY_PPAGE or key == curses.KEY_PREVIOUS:
        index = 0
        SayTextCommand({"text": paragraphs[index], "engine": engine}).execute()
        print("First " + paragraphs[index])
    if key == curses.KEY_LAST or key == curses.KEY_NPAGE or key == curses.KEY_NEXT:
        index = len(paragraphs) - 1
        SayTextCommand({"text": paragraphs[index], "engine": engine}).execute()
        print("Last " + paragraphs[index])
