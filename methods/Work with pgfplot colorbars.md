# Under construction

# Get inverted jet
It is not the most succinct solution to invert a color map, but may a more versatile one:
In the following example, we want to have the original jet color bar, and an inverted jet color bar. 
We note that, all predefined colormap has a definition by a list of RGB 3-tuples, and hence if we can find the defining list, we can manually invert it.

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
\documentclass{standalone}
\usepackage{pgfplots}
\usetikzlibrary{positioning}

\begin{document}
\begin{tikzpicture}
	\pgfplotsset{
		CB/.style={
			hide axis,
			scale only axis,
			width=0pt,
			height=0pt,
			colorbar horizontal, 
			point meta min=0,
			point meta max=1.,
			colorbar style={
				name=cb1,
				width=5cm,
				height=.5cm,
				at={(0,1.2)},
				anchor=north west,
				xlabel={original jet},
				xlabel style={yshift=.1cm},
			},
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
		]
		\addplot[draw=none] coordinates {(0, 0)};
		\end{axis}
		\end{tikzpicture}
	};
\end{tikzpicture}
\end{document}
```

