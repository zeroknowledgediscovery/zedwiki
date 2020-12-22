# Work with pgfplot color bar

## Get inverted colormap jet (or any colormap you may define)
In the following example, we want to have the original jet color bar, and an inverted jet color bar. 
We note that, all predefined colormap has a definition by a list of RGB 3-tuples, 
and hence if we can find the defining list, we can manually invert it.

According to [pgfplot manual](https://mirrors.concertpass.com/tex-archive/graphics/pgf/contrib/pgfplots/doc/pgfplots.pdf#page=194) (page 197), the jet colormap is equivalent to the RGB 3-tuples list
```
rgb255(0cm)=(0,0,128) 
rgb255(1cm)=(0,0,255)
rgb255(3cm)=(0,255,255) 
rgb255(5cm)=(255,255,0) 
rgb255(7cm)=(255,0,0) 
rgb255(8cm)=(128,0,0)
```
```
% colorbar_inverted.tex
\documentclass{standalone}
\usepackage{pgfplots}
\usetikzlibrary{positioning}

\begin{document}
\begin{tikzpicture}
    \pgfplotsset{
        CB/.style={
            % Since we only want the color bar,
            % we want to set the dimension of the axis to be 0.
            % However, if we don't hide axis and 
            % apply the width and height only to the axis (scale only axis),
            % latex will complain that the width and height being too small.
            hide axis,
            scale only axis,
            width=0pt,
            height=0pt,
            colorbar horizontal, 
            point meta min=0,
            point meta max=1.,
        },
        CBstyle/.style={
            width=5cm,
            height=.5cm,
            at={(0,1.2)},
            anchor=north west,
            xlabel style={yshift=.1cm},	
        }
    }
    \node (B1) at (0, 0) {
        \begin{tikzpicture}
            \begin{axis}[
                CB,
                colormap={}{
                    rgb255(0cm)=(0,0,128); 
                    rgb255(1cm)=(0,0,255); 
                    rgb255(3cm)=(0,255,255); 
                    rgb255(5cm)=(255,255,0); 
                    rgb255(7cm)=(255,0,0); 
                    rgb255(8cm)=(128,0,0);
                },
                colorbar style={
                    CBstyle,
                    xlabel={original jet},
                },
            ]
                \addplot[draw=none] coordinates {(0, 0)};
            \end{axis}
        \end{tikzpicture}
    };
    \node[below=0cm of B1] (B2) {
        \begin{tikzpicture}
            \begin{axis}[
                CB,
                colormap={}{
                    rgb255(0cm)=(128,0,0);
                    rgb255(1cm)=(255,0,0); 
                    rgb255(3cm)=(255,255,0); 
                    rgb255(5cm)=(0,255,255); 
                    rgb255(7cm)=(0,0,255); 
                    rgb255(8cm)=(0,0,128); 
                },
                colorbar style={
                    CBstyle,
                    xlabel={reverted jet},
                },
            ]
                \addplot[draw=none] coordinates {(0, 0)};
            \end{axis}
        \end{tikzpicture}
    };
\end{tikzpicture}
\end{document}
```
The result will be ![reverted color bar](/uploads/colorbar_reverted.png)

## One color bar with two set of scales
This is needed for the snapshot figure in the `nncomput_` project. 
For four of datasets (Weather and the Crimes), we have two types of events, 
and we used jet and inverted jet as the colormap for the density plots of the two types.
Since we have limited space, we only want to put one color bars, 
and hence the color bar has to have two scales. 

In this solution, we make a `groupplot` of two axis. 
We set the dimension of the axis to be \\\(0\\\) so that we only have colorbars.
We position the first color bar under its axis and the second one, above. 
And we position the two color bar so that they are touching each other. 
We remove the color bars original frames and, by the end, we plot a frame surrounding both bars.
```
\documentclass[tikz]{standalone}
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\usepgfplotslibrary{groupplots}

\begin{document}

\begin{tikzpicture}
	\def\WIDTH{5cm}
	\def\HEIGHT{3mm}
	\def\ys{3mm}
	\begin{groupplot}[
		% set the axis width and height to zero
		% because we only need the color bar
		width=0pt, 
		height=0pt,
		group style = {
			group size=1 by 2,
			vertical sep=2cm,
		},
	]
		\nextgroupplot[
			hide axis,
			scale only axis,
			colorbar horizontal,
			% specify the minimal value represented by the color bar
			point meta min=20,
			% specify the maximal value represented by the color bar
			point meta max=80, 
			colorbar style = {
				% name the colorbar for positioning
				name=cb1,
				width=\WIDTH,
				height=\HEIGHT,
				at={(rel axis cs: 0, 0)},
				anchor=north west,
				% remove frame around colorbar
				axis line style={draw=none}, 
				% the POSITIONS of the ticks
				xtick={20, 40, 60, 80}, 
				% the labels at the positions defined by the xtick parameters
				xticklabels={20, 40, 60, 80}, 
			}
		]
			% dummy plot since we only want the color bar
			\addplot[draw=none] coordinates {(0, 0)};
      
		\nextgroupplot[
			hide axis,
			scale only axis,
			colorbar horizontal,
			point meta min=.2,
			point meta max=1.,
			colorbar style = {
				name=cb2,
				width=\WIDTH,
				height=\HEIGHT,
				anchor=south west,
				at=(cb1.north west),
				% Move it around so that the two color bars are touching 
				yshift=\ys,
				axis line style={draw=none},
				% give a different color to the tick labels (optional)
				xticklabel style={blue},
				% put the the tick labels on top
				xticklabel pos=upper,
				xtick={.2, .4, .6, .8, 1},
				xticklabels={1, .8, .6, .4, .2},
			}
		]
			\addplot[draw=none] coordinates {(0, 0)};
	\end{groupplot}
	% draw a box around the two colorbars as a frame
	\draw (cb1.south west) rectangle (cb2.north east);
\end{tikzpicture}
\end{document}

```
This will be the result: ![one color bar two scales](/uploads/one_color_bar_two_scales.png)

**Please find the files that has the snapshots with colorbar for the `nncomput_` project [here](https://github.com/zeroknowledgediscovery/pub_nncomput_/tree/master/tex/Figures). 
The files are `snapshot_colorbar.tex` and `color.tex`**


# Automatic inversion of predefined colormap
For later reference, here is a solution that inverts a predefined colormap from stackoverflow.
```
\documentclass{standalone}
\usepackage{pgfplots}
\usepgfplotslibrary{colormaps}

\begin{document}
\pgfplotsset{colormap/jet}
  \begin{tikzpicture}
    \begin{axis}[colorbar]
      \addplot[mesh, thick, samples=200] {x^2};
    \end{axis}
  \end{tikzpicture}

  \begin{tikzpicture}
    \begin{axis}[
      colorbar,
        colormap={reverse jet}{
            indices of colormap={
                \pgfplotscolormaplastindexof{jet},...,0 of jet
        }
      },
    ]
      \addplot[mesh, thick, samples=200] {x^2};
    \end{axis}
  \end{tikzpicture}
\end{document}
```

# Get the colors strings for LaTex from python `Matplotlib`
Because we usually work with python and LaTex with the plot generated by python `matplotlib` and colorbar generated by LaTex, I post here the python code generating the color strings which we can copy and paste to LaTex:
```
import pylab as plt
import matplotlib.cm as cm
import matplotlib as mpl

# ============================ Paramters ============================
vmin, vmax, step_size = -100, 100, 20
positions = np.arange(-100, 100 + step_size, step_size)
norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax)
cmap = cm.Spectral_r

# ==== Print the strings for laTex and have a look at the colors ====
fig, ax = plt.subplots(1, 1)
for i, pos in enumerate(positions):
    rgba_color_byte = cmap(norm(pos), bytes=True) 
    rgb_str = ','.join(map(str, rgba_color_byte[:-1]))
    print(f'rgb255({i}cm)=({rgb_str});')    
    
    ax.plot(pos, pos, 'o', markersize=20, color=cmap(norm(pos))) 

plt.show()
```
The output is:
```
rgb255(0cm)=(94,79,162);
rgb255(1cm)=(50,134,188);
rgb255(2cm)=(102,194,165);
rgb255(3cm)=(169,220,164);
rgb255(4cm)=(230,245,152);
rgb255(5cm)=(254,254,189);
rgb255(6cm)=(254,224,139);
rgb255(7cm)=(252,172,96);
rgb255(8cm)=(244,109,67);
rgb255(9cm)=(211,60,78);
rgb255(10cm)=(158,1,66);
```

[[/uploads/GFS_AIRS.png|height=400px,alt=GFS AIRS Request submission page]]