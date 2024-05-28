from rich.console import Console
import imgUtils as iu
from console import rendetTitle, renderOptions, printAscii

console = Console()
resizedImageArray=None

def main():
    rendetTitle()
    originalImagePath=console.input("[red]PATH[/red]: ")
    originalImage=iu.loadImage(originalImagePath)
    
    if type(originalImage)==bool:
        console.print("Invalid [dark_blue]IMAGE[/dark_blue] or [red]PATH[/red]!")
        return -1
    color, charset, isDither, threshold=renderOptions()
    resizedImageArray=iu.resizeImage(originalImage, console, charset)
    
    printAscii(resizedImageArray, color, charset, isDither, threshold)
main()