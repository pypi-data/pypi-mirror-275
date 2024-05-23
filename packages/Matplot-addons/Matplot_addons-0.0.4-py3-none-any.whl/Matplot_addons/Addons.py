import os
import matplotlib.pyplot as plt



def save(folder, file, extension = None):
    # This functions save the plots in 'plots' folder.
    # This function it's designed for be used in a loop where several plots are maden.
    # Inptus:
    #       - Folder: Path of the main folder
    #       - file: Name of the file of the plot to be set
    #       - extension: Extension of the picture file. It must have the dot (".")
    path = os.path.join(folder, 'plots')

    if not os.path.exists(path):
        create_folder(path = path)
        
    if extension is not None:
        file = file + extension
        
    plt.savefig(os.path.join(path,file))
    
    plt.close()


def create_folder(path):
    # This function creates the folder if it does not exist
    # Inptus:
    #       - path: path of the folder to be created
    try:
        os.mkdir(path)
        print(f"{path} created.")
    except FileExistsError:
        print(f"{path} exist.")
        
        

# Tests
if __name__ == '__main__':
    
    x = [1, 2, 3]
    y = [4, 5, 6]
    folder_path = r'C:\Users\sergio.deavila\Desktop\Pruebas'
    fig, ax = plt.subplots()
    ax.plot(x,y)
    save(folder = folder_path, file = 'test', extension= '.png')
    plt.show()
    