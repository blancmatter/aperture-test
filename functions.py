from astropy.io import fits
import astropy.visualization as viz
import matplotlib.pyplot as plt
from photutils import DAOStarFinder
from astropy.stats import mad_std
import numpy as np
import settings

import logging as log


def show_image(filename):
    """
    Purpose - take a fits image, detect sources and plot the data.
    Input - filename
    """

    log.debug("Loading image data")
    img_data = fits.getdata(filename)

    bkg_sigma = mad_std(img_data)

    daofind = DAOStarFinder(fwhm=3, threshold=settings.THRESHOLD*bkg_sigma)
    sources = daofind(img_data)
    log.info("Found {} sources".format(len(sources)))

    fig, ax = plt.subplots()

    positions = np.transpose((sources['xcentroid'], sources['ycentroid']))
    for position in positions:
        circle = plt.Circle(
            position,
            30,
            color=settings.COLOR,
            lw=settings.LINE_WIDTH,
            fill=False
        )
        ax.add_artist(circle)

    viz.imshow_norm(
        img_data,
        origin='lower',
        interval=viz.ZScaleInterval(),
        cmap='gray'
    )
    plt.draw()
    plt.colorbar()
    plt.show()
    return