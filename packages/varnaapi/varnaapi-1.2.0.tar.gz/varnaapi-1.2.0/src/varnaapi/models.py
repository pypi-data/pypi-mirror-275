import re
import os
import abc
from string import ascii_lowercase, ascii_uppercase
from colour import Color
import subprocess
from math import ceil
from tempfile import NamedTemporaryFile
from deprecated import deprecated
from functools import reduce

from IPython.display import display
from svgpathtools import svg2paths
from drawsvg.jupyter import JupyterSvgImage


from varnaapi.param import _VarnaConfig, BasesStyle, _Title, _Highlight, _Annotation, _BPStyle, _ChemProb, _ColorMap
import varnaapi.settings


PARENTHESES_SYSTEMS = [
    ("(", ")"),
    ("[", "]"),
    ("<", ">"),
    ("{", "}")
] + [(c1, c2) for c1, c2 in zip(ascii_uppercase, ascii_lowercase)]
PARENTHESES_OPENING = [c1 for c1, c2 in PARENTHESES_SYSTEMS]
PARENTHESES_CLOSING = {c2: c1 for c1, c2 in PARENTHESES_SYSTEMS}


@deprecated("Class has been renamed 'Structure'")
def VARNA(*args, **kwargs):
    return Structure(*args, **kwargs)



def assert_valid_interval(length, *args):
    if not varnaapi.settings.CONFIG['hackmode']:
        for i in args:
            if i < 1 or i > length:
                raise Exception("{} out of range".format(args))

def check_structure(ss):
    pass


def _bp_to_struct(bps):
    """Base pair list to structure"""
    n = max([j for i, j in bps]) + 1
    ss = [-1 for i in range(n)]
    for i, j in bps:
        ss[i], ss[j] = j, i
    return ss

def _parse_vienna(ss):
    """
    Parse secondary structure in dot-bracket notation
    """
    stacks = {c:[] for c in PARENTHESES_OPENING}
    res = [-1 for i in range(len(ss))]
    for i,c in enumerate(ss):
        if c in PARENTHESES_OPENING:
            stacks[c].append(i)
        elif c in PARENTHESES_CLOSING:
            ii = stacks[PARENTHESES_CLOSING[c]].pop()
            res[ii],res[i] = i,ii
    return res


def _match_ext(dbn, positions):
    """Return minimal bases in exterior loop identified by given positions
    """
    res = [0] * (len(dbn)+1)
    count = 0
    current = 0
    for ind, c in enumerate(dbn):
        if c == '(':
            if count == 0:
                current = ind+1
            count += 1
            res[ind+1] = current
        elif c == ')':
            count -= 1
            res[ind+1] = current
            if count == 0:
                current = 0
        else:
            res[ind+1] = current
    return list(set(res[t] for x in positions for t in (x if isinstance(x, tuple) else (x,)) if res[t]!=0))


def _border_of_path(path):
    """Return max x and y of a svgpathtools path
    """
    _, x, _, y = path.bbox()
    return x, y


def _border_of_svg(name):
    """Return border of given svg filename
    """
    paths, _ = svg2paths(name)
    return reduce(lambda u, v: (max(u[0], v[0]), max(u[1], v[1])), map(_border_of_path, paths), (0, 0))


class BasicDraw(_VarnaConfig):
    def __init__(self):
        super().__init__()

        self.structure = ""
        self.aux_BPs = []
        self.highlight_regions = []
        self._title = None
        self.bases_styles = {}
        self.annotations = []
        self.chem_prob = []
        self.length = 0
        self.colormap = None
        self.to_flip = []
        self.smart_flip = False
        self._check_interval = True

    def add_aux_BP(self, i:int, j:int, edge5:str='wc', edge3:str='wc', stericity:str='cis', color='blue', thickness:float=1, **kwargs):
        """Add an additional base pair `(i,j)`, possibly defining and using custom style

        Args:
            i: 5' position of base pair
            j: 3' position of base pair
            edge5: Edge 5' used for interaction in non-canonical base-pairs, as defined by the Leontis/Westhof classification of base-pairs. Admissible values are __wc__ (Watson/Crick edge), __h__ (Hoogsteen edge) and __s__ (Sugar edge).
            edge3: Edge 3' used for interaction in non-canonical base-pairs. Admissible values are __wc__, __h__ and __s__.
            stericity: Orientation of the strands. Admissible values are __cis__ and __trans__
            color (color): Base-pair color
            thickness: Base-pair thickness
        """
        if self._check_interval:
            assert_valid_interval(self.length, i, j)

        self.aux_BPs.append((i, j, _BPStyle(edge5=edge5, edge3=edge3, stericity=stericity, color=color, thickness=thickness, **kwargs)))

    def add_highlight_region(self, i:int, j:int, radius:float=16, fill="#BCFFDD", outline="#6ED86E", **kwargs):
        """Highlights a region by drawing a polygon of predefined radius,
        fill color and outline color around it.
        A region consists in an interval from base `i` to base `j`.

        Args:
            i: 5'-end of the highlight
            j: 3'-end of the highlight
            radius: Thickness of the highlight
            fill (color): The color used to fill the highlight
            outline (color): The color used to draw the line around the highlight
        """
        if self._check_interval:
            assert_valid_interval(self.length, i, j)

        self.highlight_regions.append((i, j, _Highlight(radius, fill, outline, **kwargs)))

    def set_title(self, title:str, color='#000000', size:int=19, **kwargs):
        """Set title displayed at the bottom of the panel with color and font size
        """
        self._title = _Title(title, color, size, **kwargs)

    def add_bases_style(self, style:BasesStyle, bases:list):
        """Apply a [BasesStyle][varnaapi.param.BasesStyle] to a list of positions.
        If a position is assigned to more than one styles,
        one of them will be randomly used.

        Args:
            style: Style to apply
            bases: List of 0-indexed positions

        Examples:
            >>> v = varnaapi.Structure()
            >>> style1 = varnaapi.param.BasesStyle(fill="#FF0000")
            >>> style2 = varnaapi.param.BasesStyle(fill="#FFFF00" outline="#00FF00")
            >>> v.add_bases_style(style1, [1,2,4])
            >>> v.add_bases_style(setye1, [10,11,12])
            >>> v.add_bases_style(style2, [4,5,6,7])

        """
        if not isinstance(style, BasesStyle):
            raise Exception("style should be BasesStyle object")
        if len(bases) > 0:
            self.bases_styles[style] = self.bases_styles.get(style, set()).union({i for i in bases})

    def add_annotation(self, annotation:_Annotation):
        """Add an annotation.
        Argument should be a valid [Annotation](/style#annotation) object

        Examples:
            >>> v = varnaapi.Structure()
            >>> a = varnaapi.param.LoopAnnotation("L1", 6, color="#FF00FF")
            >>> v.add_annotation(a)
        """
        # Assert is annotation
        if not isinstance(annotation, _Annotation):
            raise Exception("Should be a valid annotation object")
        self.annotations.append(annotation)

    def add_chem_prob(self, base:int, glyph:str='arrow', dir:str='in', intensity:float=1, color='#0000B2', **kwargs):
        """Add chemical probing annotation on two adjacent bases.

        Args:
            base: index of the first base of adjacent bases
            glyph: Shape of the annotation chosen from ['arrow', 'dot', 'pin', 'triangle']
            dir: Direction of the annotation chosen from ['in', 'out']
            intensity: Annotation intensity, _i.e._ thickness
            color (color): Color used to draw the annotation
        """
        if self._check_interval:
            assert_valid_interval(self.length, base)
        self.chem_prob.append((int(base), _ChemProb(glyph=glyph, dir=dir, intensity=intensity, color=color, **kwargs)))

    def add_colormap(self, values, vMin:float=None, vMax:float=None, caption:str="", style="energy", **kwargs):
        """Add color map on bases.

        Args:
            values (float list): list of values in float for each base. `0`s are added at the end of the list if the list length is shorter than the number of bases.
            vMin: Minium value for the color map
            vMax: Maximum value for the color map
            caption: Color map caption
            style: Color map style, which is one of the following

                - predefined style from

                    ['red', 'blue', 'green', 'heat', 'energy', 'bw']

                - customized style in dictionary {value: color}
        """
        self.colormap = _ColorMap(values, vMin, vMax, caption, style, **kwargs)

    def flip(self, *positions):
        """Flip one or more helices identfied by given positions.

        Note: Behind the flip
            For a given base or basepair, VARNA flips the helix the base or the basepair belongs to by identifying first the farest position at 5' and then redrawing the helix in the counter direction from that position.
            By default, VARNA positions bases in clockwise direction, therefore repositioning bases in counter clockwise direction gives the effect of flip.
            Such flipping rule gives the following results:

                1. No flip will happen if given position is unpaired.
                2. Giving even number of positions of the same helix cancels out the flip.
                3. Consider two helices separated by a loop. Giving the position of the first helix flips both helices as one. However, giving the position of the second helix will result the flipping of only the second one, which may cause two helices overlap in the drawing.
                4. In linear drawing mode, flipping will not draw basepair arcs in lower plane as if affects bases positioning.

        Args:
            positions: either a base in integer or a basepair in integer tuple of the helix to flip

        Examples:
            Consider secondary structure
            ```
                    ...(((...)))...((...))...(((...)))...
                    1234567890123456789012345678901234567
            ```
            One can flip the first and third branches by
            >>> v = varnaapi.Structure(structure=dbn)
            >>> v.flip(5, (27,33))

        __See Also:__ [BasicDraw.enable_smart_flip][varnaapi.BasicDraw.enable_smart_flip]
        """
        if self._check_interval:
            map(lambda x: assert_valid_interval(self.length, *(x if isinstance(x, tuple) else (x,))), positions)
        self.to_flip += positions


    def enable_smart_flip(self, enable:bool=True):
        """Enable to flip positions treating to address points 1-3 in flip().
        When enable, for each branch of exterior loop, VARNA API will send only the 5' most position to flip to VARNA if any position (unpaired included) of the branch is given by flip().

        Args:
            enable (bool): Enable or disable smart flip.

        __See Also:__ [BasicDraw.flip][varnaapi.BasicDraw.flip]
        """
        self.smart_flip = enable

    def _gen_command(self):
        """
        Return command to run VARNA
        """
        cmd = ['java', '-cp', varnaapi.settings.CONFIG['varnapath'], 'fr.orsay.lri.varna.applications.VARNAcmd']

        cmd += self._gen_input_cmd()

        cmd += ['-o', self.output]

        cmd += self._gen_param_cmd()

        # Title cmd
        if self._title is not None:
            cmd += self._title._to_cmd()

        # Aux Base pairs
        if len(self.aux_BPs) > 0:
            res = []
            for i, j, style in self.aux_BPs:
                s = "({},{})".format(i,j)
                setting = style._to_cmd(self.get_params(complete=True)['bp'])
                if not setting == "":
                    s += ":" + setting
                res.append(s)
            cmd += ["-auxBPs", ";".join(res)]

        # Highlight Region
        if len(self.highlight_regions) > 0:
            res = []
            for item in self.highlight_regions:
                s = "{}-{}".format(item[0], item[1])
                setting = item[2]._to_cmd()
                if not setting == "":
                    s += ":" + setting
                res.append(s)
            cmd += ['-highlightRegion', ';'.join(res)]

        # BasesStyles
        styles = {'fill': 'baseInner', 'outline': 'baseOutline', 'label': 'baseName', 'number': 'baseNum'}
        styles_dafault = {v: self.get_params().get(v) for v in styles.values() if v in self.get_params()}
        for ind, (style, bases) in enumerate(self.bases_styles.items()):
            s = style._to_cmd(**styles_dafault)
            if not s == "":
                cmd += ["-basesStyle{}".format(ind + 1), s]
                cmd += ["-applyBasesStyle{}on".format(ind + 1), ','.join(map(str, bases))]

        # Annotations
        if len(self.annotations) > 0:
            cmd += ["-annotations", ';'.join([t._to_cmd() for t in self.annotations])]

        # Chem Prob
        if len(self.chem_prob) > 0:
            res = []
            for i, style in self.chem_prob:
                s = "{}-{}".format(i, i+1)
                setting = style._to_cmd()
                if not setting == "":
                    s += ":" + setting
                res.append(s)
            cmd += ["-chemProb", ";".join(res)]

        # Color Map
        if self.colormap is not None:
            cmd += self.colormap._to_cmd()

        # flip
        if self.smart_flip:
            to_flip = _match_ext(self.format_structure(), self.to_flip)
        else:
            to_flip = self.to_flip
        if len(to_flip) > 0:
            cmd += ["-flip", ';'.join('-'.join(str(t) for t in (x if isinstance(x, tuple) else (x,))) for x in to_flip)]
        return cmd

    def format_structure(self):
        return self.structure

    def _gen_input_cmd(self):
        return []

    def savefig(self, output):
        """Call VARNA to draw and store the paint in output

        Args:
            output: Output file name with extension is either png or svg
        """
        self.output = output
        cmd = self._gen_command()
        varnaapi.settings.Logger.debug(cmd)
        subprocess.run(cmd)

    def _to_svg(self, size=None, full:bool=False):
        """Convert drawing to svg that can be displayed in jupyter notebook

        Code inspired from drawsvg and svgpathtools
        """
        tmp = NamedTemporaryFile(suffix='.svg')
        self.savefig(tmp.name)
        # We need to modify some info in svg tag to make it display until VARNA fix it
        x, y = _border_of_svg(tmp.name)
        if full:
            w = "100%"
            h = "100%"
        else:
            if size is None:
                size = max(100, min(600, max(x, y)))
            if x > y:
                w = "{}px".format(size)
                h = "{}px".format(int(ceil(size*y/x)))
            else:
                h = "{}px".format(size)
                w = "{}px".format(int(ceil(size*x/y)))
        res = []
        for line in open(tmp.name).readlines():
            if line.startswith("<svg"):
                line = '<svg width="{}" height="{}" version="1.1" viewBox="0 0 {} {}" \n'.format(w, h, int(ceil(x/100)*100), int(ceil(y/100)*100))
            res.append(line)
        return "".join(res)

    def show(self, size=None, full=False):
        """Display drawing (svg format) in jupyter notebook

        Args:
            size (int): max size (in px) for width or height if given
            full: if True, set image width to 100%
        """
        svg = self._to_svg(size=size, full=full)
        display(JupyterSvgImage(svg))

    def _repr_svg_(self):
        return self._to_svg()


class Structure(BasicDraw):
    """Classic VARNA drawing mode. Constructor from given RNA sequence or/and secondary structure.
    If sequence and structure have different size, the larger one is used
    and ` `s or `.`s will be added to sequence or structure to complement.

    Args:
        sequence: Raw nucleotide sequence for the displayed RNA.
             Each base must be encoded in a single character.
             Letters others than `A`, `C`, `G`, `U` and space are tolerated.
        structure (str or list): RNA (pseudoknotted) secondary structure in dbn
    """
    def __init__(self, structure=None, sequence=None):
        super().__init__()

        self.length = -1
        self.structure = []
        self.sequence = ""

        if structure is not None:
            self.structure = structure
            # if isinstance(structure, list):
            #     if len(structure) > 0:
            #         first = structure[0]
            #         if len(first)==1:
            #             self.structure = check_structure(structure)
            #         elif len(first)==2:
            #             self.structure = _bp_to_struct(structure)
            #         else:
            #             raise Exception("Unrecognized structure format for %s"%(structure))
            # Dot-Bracket Notation
            self.length = len(self.structure)
        if sequence is not None:
            self.length = max(self.length,len(sequence))
            self.sequence = sequence
        # Now we know the length, let's extend the sequence and structure if necessary
        # self.sequence += " "*(self.length-len(self.sequence))
        # self.structure += [-1]*(self.length-len(self.structure))

    # def format_structure(self):
    #     """Return secondary structure in dot-brackaet notation
    #     """
    #     def greedy_fill(c1, c2, res, ss, i, j):
    #         if i <= j:
    #             k = ss[i]
    #             if k == -1:
    #                 greedy_fill(c1, c2, res, ss, i+1, j)
    #             elif k > i:
    #                 if k <= j:
    #                     res[i], res[k] = c1, c2
    #                     ss[i], ss[k] = -1, -1
    #                     greedy_fill(c1, c2, res, ss, i+1, k-1)
    #                     greedy_fill(c1, c2, res, ss, k+1, j)

    #     res = ["." for _ in range(self.length)]
    #     ss = self.structure[:]
    #     for c1, c2 in PARENTHESES_SYSTEMS:
    #         greedy_fill(c1, c2, res, ss, i=0, j=self.length-1)
    #         finished = True
    #         for i in ss:
    #             if i != -1:
    #                 finished = False
    #         if finished:
    #             break
    #     return "".join(res)

    def _gen_input_cmd(self):
        return ['-sequenceDBN', self.sequence, '-structureDBN', self.format_structure()]

    def __repr__(self):
        return repr((self.format_structure(), self.sequence))


class FileDraw(BasicDraw):
    """Drawing class with input structure/sequence given by file
    The simplest input format is dbn format. The file contains two lines: the first line is the sequence and the second one is the structure in dbn.
    Other supported formats are ct, BPseq, TCoffee, Stockholm, RNAML, as well as Varna session.

    Warning: Position value check disable
        As input file is passed to VARNA directly without any parsing, the RNA length is unknown.
        Therefore, all value checks related to position are disable.

    Args:
        inputfile: path to inputfile
    """
    def __init__(self, inputfile):
        super().__init__()
        self.inputfile = inputfile

        # Disable interval check
        self._check_interval = False

    def _gen_input_cmd(self):
        return ['-i', self.inputfile]


class Comparison(BasicDraw):
    """Drawing of two aligned RNAs.
    Unlike classic [Structure][varnaapi.Structure] mode,
    both sequences and structures __MUST__ be specified and have the same size.
    Additionally, the merged secondary structures must currently be without any crossing
    interactions (e.g. pseudoknots), and merging them should give a secondary structure.
    Gap character is `.`.
    Args:
        seq1 (str): Sets the gapped nucleotide sequence for the first RNA sequence
        structure1 (str): Sets the first secondary structure in Dot-Bracket Notation
        seq2 (str): Sets the gapped nucleotide sequence for the second sequence
        strcuture2 (str): Sets the second secondary structure in Doc-Bracket Notation
    """

    def __init__(self, seq1, structure1, seq2, structure2):
        if not (len(seq1) == len(structure1) == len(seq2) == len(structure2)):
            raise Exception("All length should be equal")
        super().__init__()

        self.seq1 = seq1
        self.structure1 = structure1
        self.seq2 = seq2
        self.structure2 = structure2
        self.length = len(seq1)

    def _gen_input_cmd(self):
        return ["-comparisonMode", str(True), "-firstSequence", self.seq1, "-firstStructure", self.structure1, "-secondSequence", self.seq2, "-secondStructure", self.structure2]

    def __repr__(self):
        return repr((self.seq1, self.structure1, self.seq2, self.structure2))


class Motif(BasicDraw):
    """Special class for motif drawing.
    A motif is a rooted ordered tree, similar to a secondary structure,
    but whose leaves may represent base paired positions, named open base
    pairs or open paired leaves and denoted by `(*)`, and the root always
    represents a closing base pair. A motif can also be seen as an union
    of consecutive loops. The figure below represents `((*)(*)(((*)(*))))`.

    Motif class inherits from [Structure][varnaapi.Structure] with some pre-set
    parameters.

    - rotation is set at `180`
    - default base pair style is `simple`
    - base number is hidden by setting default color to white
    (default background color)

    A dummy base pair is added after each open base pair and in front of
    the root, as shown in the figure below.
    Therefore, the index of bases is changed after creating the object.
    For example, the index of first base of root is `1` instead of `0`.
    The default bases style for root is
    `BasesStyle(fill="#606060", outline="#FFFFFF", number="#FFFFFF")` and
    `BasesStyle(fill="#DDDDDD", outline="#FFFFFF", number="#FFFFFF")` for
    dummy bases. One can change them using
    [set_root_bases_style][varnaapi.Motif.set_root_bases_style] and
    [set_dummy_bases_style][varnaapi.Motif.set_dummy_bases_style].

    Args:
        motif (str): Motif in Dot-Bracket Notation.
            `(*)` is used to represent open base pair.
        sequence (str): Chain of characters for motif. Note that sequence
            should exactly match with motif, _i.e._ Equal length and same
            positions for all `*`.

    """
    def __init__(self, motif, sequence=None):
        super().__init__()

        seq = ""
        struct = ""
        extra_bps = []
        pos = 1
        for i, c in enumerate(motif):
            if c == "*":
                if sequence is not None and not sequence[i] == '*':
                    raise Exception("Motif and sequence are not compatible at position {}".format(i))
                extra_bps.append((pos + 1, pos + 2))
                seq += " & "
                struct += "(&)"
                pos += 2
            else:
                if sequence is not None:
                    w = sequence[i]
                else:
                    w = " "
                if w == '*':
                    raise Exception("Motif and sequence are not compatible at position {}".format(i))
                seq += w
                struct += c
                pos += 1
        seq = " " + seq + " "
        struct = "(" + struct + ")"
        self.sequence = seq
        self.structure = struct
        self.length = pos + 1
        extra_bps.append((1, self.length))
        self.extra_bps = extra_bps

        # Default Bases Styles
        self.rootBasesStyle = BasesStyle(fill="#606060", outline="#FFFFFF")
        self.dummyBasesStyle = BasesStyle(fill="#DDDDDD", outline="#FFFFFF")

        self.update(baseNum="#FFFFFF", bpStyle='simple', rotation=180)

    def _gen_input_cmd(self):
        return ["-sequenceDBN", self.sequence, "-structureDBN", self.structure]

    def set_dummy_bases_style(self, style):
        """Set style for dummy bases. Argument is a [BasesStyle][varnaapi.param.BasesStyle] object.
        """
        if not isinstance(style, BasesStyle):
            raise Exception('The argument should be BasesStyle object')
        self.dummyBasesStyle = style

    def set_root_bases_style(self, style):
        """Set style for root bases. Argument is a [BasesStyle][varnaapi.param.BasesStyle] object.
        """
        if not isinstance(style, BasesStyle):
            raise Exception('The argument should be BasesStyle object')
        self.rootBasesStyle = style

    def savefig(self, output, show=False):
        dummybps = []
        for (i,j) in self.extra_bps:
            dummybps += [i, j]
            self.add_aux_BP(i=i, j=j, color="#DDDDDD")
        self.add_aux_BP(i=2, j=self.length-1, color="#000000", thickness=2)

        self.add_bases_style(self.rootBasesStyle, [2, self.length-1])
        self.add_bases_style(self.dummyBasesStyle, dummybps)
        super().savefig(output, show)
