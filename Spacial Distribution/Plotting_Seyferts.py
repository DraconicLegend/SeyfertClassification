import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def main():
    df = pd.read_csv("Seyfert.csv")
    df = df.fillna(0)

    long_Sy1 = []
    lat_Sy1 = []
    long_Sy2 = []
    lat_Sy2 = []

    for k, row in df.iterrows():
            ra      = float(row['ra'])
            dec     = float(row['dec'])
            OType   = str(row['OType'])

            if OType == 'Sy1':
                long_Sy1.append(ra)
                lat_Sy1.append(dec)
            elif OType == 'Sy2':
                long_Sy2.append(ra)
                lat_Sy2.append(dec)



    plt.figure (figsize = (16, 8.4))
    plt.subplot (projection = "aitoff")
    plt.title ("Seyfert Galaxies")
    plt.plot (long_Sy1, lat_Sy1, 'o', markersize = 0.5, alpha = 0.4, color = 'r', label='Sy1')
    plt.plot (long_Sy2, lat_Sy2, 'o', markersize = 0.5, alpha = 0.4, color = 'b', label='Sy2')
    plt.grid (True)
    plt.show()

if __name__ == "__main__":
    main()
