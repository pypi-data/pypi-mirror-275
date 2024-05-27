import numpy as np
import matplotlib.pyplot as plt
import matplotlib.offsetbox as offsetbox

from . import linelist as ll

class Spectrum():
    """
    class for a spectrum object.
    The filename (incl extension name) of the file having four cols
    first col: wavelengths, 2nd col: flux, 3rd col: err, 4th col: continuum
    """

    imp_lines = (
        'HI_1215', 'HI_1025', 'DI_1215', 'DI_1025',
        'HeI_584', 'HeI_537', 'HeII_303', 'HeII_256',
        'CI_1656', 'CI_1560', 'CII_1334', 'CII_1036',
        'CIII_977', 'CIV_1548', 'CIV_1550',
        'NI_1200a', 'NI_1200b', 'NII_1083', 'NII_915',
        'NIII_684', 'NIII_685', 'NIII_763', 'NIII_989',
        'NIV_765', 'NV_1238', 'NV_1242',
        'OI_1302', 'OI_988', 'OI_971', 'OII_834',
        'OII_833', 'OII_832', 'OIII_832', 'OIII_702',
        'OIV_553', 'OIV_554', 'OIV_608', 'OIV_787',
        'OV_629', 'OVI_1031', 'OVI_1037', 'OVII_21', 'OVII_18',
        'NeIV_543', 'NeIV_542', 'NeIV_541', 'NeV_568',
        'NeVI_558', 'NeVIII_780', 'NeVIII_770',
        'NaI_5897', 'NaI_5891',
        'MgI_2026', 'MgI_2852', 'MgII_2803', 'MgII_2796',
        'SiI_1845', 'SiI_1693', 'SiI_1631', 'SiI_1562',
        'SiII_1808', 'SiII_1526', 'SiII_1304', 'SiII_1260',
        'SiII_1193', 'SiII_1190', 'SiII_1020', 'SiII_989',
        'SiIII_1206', 'SiIV_1402', 'SiIV_1393',
    )

    def __init__(self, filename, ):
        self.filename = filename
        f = open(self.filename)
        wvlength = []
        flux = []
        cont = []    # continuum

        for line in f.readlines():
            line = line.split()
            wvlength.append(float(line[0].lstrip().rstrip()))
            flux.append(float(line[1].lstrip().rstrip()))
            cont.append(float(line[3].lstrip().rstrip()))
        
        f.close()

        self.wvlength = np.asarray(wvlength)
        self.flux = np.asarray(flux)
        self.cont = np.asarray(cont)
        cont_mean = np.mean(self.cont)
        self.ylim = (0, 4*cont_mean)

        # Keep track of added lines and annotations
        self.added_lines = []
        self.added_annotations = []
        
        # Store the clicked coordinates
        self.clicked_coords = None
        self.cid = None

        # Storing the transition value of getz
        self.transition = None
    
    def fplot(self):
        """
        Method to plot flux vs wavelength
        """
        plt.ion()
        plt.figure(figsize=(20,6))
        plt.ylim(self.ylim[0], self.ylim[1])
        plt.plot(self.wvlength, self.flux, 'k', lw=0.6)
        plt.show()

    def nfplot(self):
        """
        Method to plot normalized flux vs wavelength
        """
        plt.ion()
        plt.figure(figsize=(20,6))
        plt.ylim(-0.25, max(self.flux/self.cont)*0.01)
        plt.plot(self.wvlength, self.flux/self.cont, 'k', lw=0.6)
        # Adjust the subplot to decrease padding
        plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.1)

        plt.show()

    def marklines(self, z=0):
        """
        Method to mark transition lines at certain wavelengths
        """
        plt.ion()

        for line in self.imp_lines:
            line_wvlength = ll.wl[line]
            if z: line_wvlength = (1+z)*line_wvlength
            if min(self.wvlength) <= line_wvlength <= max(self.wvlength):
                lineobj = plt.axvline(line_wvlength, color='purple', linestyle='dotted')
                self.added_lines.append(lineobj)
                # plt.text(line_wvlength, 0.95, line, rotation=90, va='top', ha='center', color='purple')
                # plt.annotate(line, xy=(line_wvlength, 0.95), xycoords='data',
                #          xytext=(0, 5), textcoords='offset points',
                #          rotation=90, va='bottom', ha='center', color='purple')

                # Create a fixed annotation box for the label
                # Refer: https://matplotlib.org/stable/gallery/text_labels_and_annotations/demo_annotation_box.html
                label_box = offsetbox.TextArea(f'{line}', textprops={'color': 'purple', 'rotation': 90, 'va': 'bottom', 'ha': 'right'})
                ab = offsetbox.AnnotationBbox(label_box, (line_wvlength, 0.75), xycoords=('data', 'axes fraction'), frameon=False)
                plt.gca().add_artist(ab)
                self.added_annotations.append(ab)

    # def unmark(self):
    #     """
    #     Method to remove marked transition lines and labels
    #     """
    #     plt.ion()

    #     # ax = plt.gca()  # Get the current Axes object

    #     # # Find all lines and text annotations in the Axes
    #     # lines = ax.lines
    #     # annotations = ax.texts

    #     # # Remove each line and annotation added by marklines method
    #     # for line in lines:
    #     #     if line.get_color() == 'purple' and line.get_linestyle() == 'dotted':
    #     #         ax.lines.remove(line)
    #     # for annotation in annotations:
    #     #     if annotation.get_color() == 'purple':
    #     #         ax.texts.remove(annotation)

    #     # plt.draw()  # Redraw the plot to reflect the changes
    #     plt.clf()  # Clear the current figure

    #     # Plot the original spectrum without marked lines and labels
    #     self.nfplot()

    #     plt.draw()  # Redraw the plot

    # def unmark(self):
    #     """
    #     Method to remove marked transition lines and labels
    #     """
    #     plt.ion()

    #     ax = plt.gca()  # Get the current Axes object

    #     # Find all lines and text annotations in the Axes
    #     lines = list(ax.lines)  # Convert to a regular list
    #     annotations = list(ax.texts)  # Convert to a regular list

    #     # Remove each line and annotation added by marklines method
    #     for line in lines:
    #         if line.get_color() == 'purple' and line.get_linestyle() == 'dotted':
    #             line.remove()
    #     for annotation in annotations:
    #         if annotation.get_color() == 'gray':
    #             annotation.remove()

    #     plt.draw()  # Redraw the plot to reflect the changes

    # def unmarklines(self):
    #     """
    #     Method to remove marked transition lines and labels
    #     """
    #     plt.ion()

    #     ax = plt.gca()  # Get the current Axes object

    #     # Iterate through the lines and annotations and set their visibility to False
    #     for line in ax.lines:
    #         if line.get_color() == 'purple' and line.get_linestyle() == 'dotted':
    #             line.set_visible(False)
    #     for annotation in ax.texts:
    #         if annotation.get_color() == 'purple':
    #             annotation.set_visible(False)

    #     plt.draw()  # Redraw the plot to reflect the changes

    def unmark(self):
            """
            Method to remove marked transition lines and labels
            """
            plt.ion()

            # Remove added lines and annotations
            for line in self.added_lines:
                line.remove()
            for annotation in self.added_annotations:
                annotation.remove()

            # Clear the added lines and annotations lists
            self.added_lines = []
            self.added_annotations = []

            plt.draw()  # Redraw the plot to reflect the changes

    def getz(self, transition):
        """
        Prints the redshift of transition line by mouseclick event
        """
        print('Click to find z')
        plt.ion()

        ax = plt.gca()  # Get the current Axes object

        # Find the transition wavelength
        line_wavelength = ll.wl[transition]
        self.transition = transition

        # Connect the onclick event
        self.cid = plt.gcf().canvas.mpl_connect('button_press_event', self._onclick)
        plt.draw()

    def _onclick(self, event):
        """
        Callback function for mouse click event
        """
        # print('onclick called')
        if event.inaxes:
            self.clicked_coords = (event.xdata, event.ydata)
            plt.gcf().canvas.mpl_disconnect(self.cid)  # Disconnect the onclick event
            # plt.close()  # Close the plot
            # print('onclick finished')
            self.print_clicked_coords()

    def print_clicked_coords(self):
        """
        Method to print clicked coordinates (for testing)
        """
        # print("Clicked Coordinates:", self.clicked_coords)
        # print(type(self.clicked_coords))
        # clicked_coords is a tuple with x and y value
        z = (self.clicked_coords[0]/ll.wl[self.transition]) - 1.0
        print(z)
