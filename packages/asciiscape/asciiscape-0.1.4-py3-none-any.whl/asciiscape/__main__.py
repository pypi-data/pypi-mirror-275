from rich.console import Console
from asciiscape import imgUtils as iu
from asciiscape import console
from console import printAscii, renderOptions, renderTitle

console = Console()
resizedImageArray=None

def main():
    renderTitle()
    originalImagePath=console.input("[red]PATH[/red]: ")
    originalImage=iu.loadImage(originalImagePath)
    
    if type(originalImage)==bool:
        console.print("Invalid [dark_blue]IMAGE[/dark_blue] or [red]PATH[/red]!")
        return -1
    color, charset, isDither, threshold=renderOptions()
    resizedImageArray=iu.resizeImage(originalImage, console, charset)
    
    printAscii(resizedImageArray, color, charset, isDither, threshold)
main()