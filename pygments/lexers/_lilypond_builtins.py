# -*- coding: utf-8 -*-
"""
    pygments.lexers._lilypond_builtins
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    :copyright: Copyright 2006-2019 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""


#from __future__ import unicode_literals

lilypond_keywords = (
    'accepts',
    'alias',
    'consists',
    'defaultchild',
    'denies',
    #'description',
    #'grobdescriptions',
    'hide', # since 2.18
    'include',
    #'invalid',
    'language',
    'name',
    #'objectid',
    'omit', # since 2.18
    'once',
    'set',
    'unset',
    'override',
    'revert',
    'remove',
    'temporary', # since 2.18
    #'sequential',
    #'simultaneous',
    #'type',
    'undo', # since 2.18 (not mentioned in the command index)
    'version',
    'score',
    'book',
    'bookpart',
    'header',
    'paper',
    'midi',
    'layout',
    'with',
    'context',
)

lilypond_music_commands = (
    'absolute', # since 2.18
    'acciaccatura',
    'accidentalStyle', # since 2.16
    'addChordShape', # since 2.16
    'addInstrumentDefinition',
    'addlyrics',
    'addQuote',
    'afterGrace',
    #'afterGraceFraction', # this is a parser variable
    'aikenHeads',
    'aikenHeadsMinor',
    'allowPageTurn',
    'alterBroken', # since 2.18 (?)
    'alternative',
    #'AncientRemoveEmptyStaffContext',
    'appendToTag', # since 2.16
    'applyContext',
    'applyMusic',
    'applyOutput',
    'appoggiatura',
    'arpeggio',
    'arpeggioArrowDown',
    'arpeggioArrowUp',
    'arpeggioBracket',
    'arpeggioNormal',
    'arpeggioParenthesis',
    'ascendens',
    'auctum',
    'augmentum',
    'autoAccidentals',
    'autoBeamOff',
    'autoBeamOn',
    'autochange',
    'balloonGrobText',
    'balloonLengthOff',
    'balloonLengthOn',
    'balloonText',
    'bar',
    'barNumberCheck',
    'bassFigureExtendersOff',
    'bassFigureExtendersOn',
    'bassFigureStaffAlignmentDown',
    'bassFigureStaffAlignmentNeutral',
    'bassFigureStaffAlignmentUp',
    'bendAfter',
    'blackTriangleMarkup',
    'bookOutputName',
    'bookOutputSuffix',
    'bracketCloseSymbol',
    'bracketOpenSymbol',
    'break',
    'breathe',
    'breve',
    'cadenzaOff',
    'cadenzaOn',
    'caesura',
    'cavum',
    'change',
    'chordmode',
    #'chordNameSeparator',
    #'chordPrefixSpacer',
    #'chordRootNamer',
    'chordRepeats', # since 2.16
    'chords',
    'clef',
    'cm',
    'compoundMeter', # since 2.16
    'compressFullBarRests',
    'context',
    #'cr',
    #'cresc',
    #'crescHairpin',
    #'crescTextCresc',
    'crossStaff', # since 2.16
    'cueClef',  # since 2.16
    'cueClefUnset',  # since 2.16
    'cueDuring',
    'cueDuringWithClef',  # since 2.16
    'dashBar',
    'dashDash',
    'dashDot',
    'dashHat',
    'dashLarger',
    'dashPlus',
    'dashUnderscore',
    'deadNote',  # since 2.16
    #'decr',
    'default',
    'defaultNoteHeads',  # since 2.16
    'defaultTimeSignature',
    'defineBarLine', # since 2.18
    'deminutum',
    'denies',
    'descendens',
    #'dim',
    'dimHairpin',
    'dimTextDecr',
    'dimTextDecresc',
    'dimTextDim',
    'displayLilyMusic',
    'displayMusic',
    'divisioMaior',
    'divisioMaxima',
    'divisioMinima',
    'dotsDown',
    'dotsNeutral',
    'dotsUp',
    'drummode',
    'drumPitchTable',
    'drums',
    'dynamicDown',
    'dynamicNeutral',
    'dynamicUp',
    'easyHeadsOff',
    'easyHeadsOn',
    'endcr',
    'endcresc',
    'enddecr',
    'enddim',
    'endincipit',
    'endSpanners',
    'episemFinis',
    'episemInitium',
    'escapedBiggerSymbol',
    'escapedExclamationSymbol',
    'escapedParenthesisCloseSymbol',
    'escapedParenthesisOpenSymbol',
    'escapedSmallerSymbol',
    'expandFullBarRests',
    #'f',
    'featherDurations',
    'fermataMarkup',
    #'ff',
    #'fff',
    #'ffff',
    #'fffff',
    'figuremode',
    'figures',
    'finalis',
    'fingeringOrientations',
    'flexa',
    #'fp',
    'frenchChords',
    'fullJazzExceptions',
    'funkHeads',
    'funkHeadsMinor',
    #'fz',
    'germanChords',
    'glissando',
    'grace',
    'graceSettings',
    'harmonic',
    'hideNotes',
    'hideStaffSwitch',
    'huge',
    'ignatzekExceptionMusic',
    'ignatzekExceptions',
    'iij',
    'IIJ',
    'ij',
    'IJ',
    'improvisationOff',
    'improvisationOn',
    'in',
    'inclinatum',
    'includePageLayoutFile',
    'indent',
    'instrumentSwitch',
    'instrumentTransposition',
    'interscoreline',
    'italianChords',
    'keepWithTag',
    'key',
    'killCues',
    'label',
    'laissezVibrer',
    'large',
    'ligature',
    'linea',
    'longa',
    'lyricmode',
    'lyrics',
    'lyricsto',
    'maininput',
    'majorSevenSymbol',
    'makeClusters',
    'mark',
    'markLengthOff', # since 2.18
    'markLengthOn',  # since 2.18
    'markup',
    'markuplines', # deprecated, till 2.14
    'markuplist', # from 2.16
    'maxima',
    'melisma',
    'melismaEnd',
    'mergeDifferentlyDottedOff',
    'mergeDifferentlyDottedOn',
    'mergeDifferentlyHeadedOff',
    'mergeDifferentlyHeadedOn',
    #'mf',
    'mm',
    #'mp',
    'musicMap',
    'neumeDemoLayout',
    'new',
    'newSpacingSection',
    'noBeam',
    'noBreak',
    'noPageBreak',
    'noPageTurn',
    'normalsize',
    'notemode',
    'numericTimeSignature',
    'octaveCheck',
    'oldaddlyrics',
    'oneVoice',
    'oriscus',
    'ottava',
    'override',
    'overrideProperty',
    'overrideTimeSignatureSettings',  # since 2.16
    #'p',
    'pageBreak',
    'pageTurn',
    'palmMute',  # since 2.16
    'palmMuteOn',  # since 2.16
    'parallelMusic',
    'parenthesisCloseSymbol',
    'parenthesisOpenSymbol',
    'parenthesize',
    'partcombine',
    'partCombineListener',
    'partial',
    'partialJazzExceptions',
    'partialJazzMusic',
    'pes',
    'phrasingSlurDashed',
    'phrasingSlurDotted',
    'phrasingSlurDown',
    'phrasingSlurNeutral',
    'phrasingSlurSolid',
    'phrasingSlurUp',
    'pipeSymbol',
    'pitchedTrill',
    'pointAndClickOff',
    'pointAndClickOn',
    #'pp',
    #'ppp',
    #'pppp',
    #'ppppp',
    'predefinedFretboardsOff',
    'predefinedFretboardsOn',
    'pt',
    'pushToTag', # since 2.16
    'quilisma',
    'quoteDuring',
    'relative',
    'RemoveEmptyRhythmicStaffContext',
    'RemoveEmptyStaffContext',
    'removeWithTag',
    'repeat',
    'repeatTie',
    'resetRelativeOctave',
    'responsum',
    'rest',
    'revert',
    #'rfz',
    'rightHandFinger',
    'sacredHarpHeads',
    'sacredHarpHeadsMinor',
    'scaleDurations',
    'scoreTweak',
    'semiGermanChords',
    'set',
    #'sf',
    #'sff',
    #'sfp',
    #'sfz',
    'shape', # since 2.16
    'shiftDurations',
    'shiftOff',
    'shiftOn',
    'shiftOnn',
    'shiftOnnn',
    'showStaffSwitch',
    'single', # since 2.18
    'skip',
    'skipTypesetting',
    'slurDashed',
    'slurDotted',
    'slurDown',
    'slurNeutral',
    'slurSolid',
    'slurUp',
    'small',
    'sostenutoOff',
    'sostenutoOn',
    'southernHarmonyHeads',
    'southernHarmonyHeadsMinor',
    #'sp',
    'spacingTweaks',
    #'spp',
    'startAcciaccaturaMusic',
    'startAppoggiaturaMusic',
    'startGraceMusic',
    'startGroup',
    'startStaff',
    'startTextSpan',
    'startTrillSpan',
    'stemDown',
    'stemNeutral',
    'stemUp',
    'stopAcciaccaturaMusic',
    'stopAppoggiaturaMusic',
    'stopGraceMusic',
    'stopGroup',
    'stopStaff',
    'stopTextSpan',
    'stopTrillSpan',
    'stringTuning', # since 2.16
    'strokeFingerOrientations',
    'stropha',
    'sustainOff',
    'sustainOn',
    'tabFullNotation',
    'tag',
    'teeny',
    'tempo',
    'tempoWholesPerMinute',
    'textLengthOff',
    'textLengthOn',
    'textSpannerDown',
    'textSpannerNeutral',
    'textSpannerUp',
    'tieDashed',
    'tieDotted',
    'tieDown',
    'tieNeutral',
    'tieSolid',
    'tieUp',
    'tildeSymbol',
    'time',
    'times',
    'timing',
    'tiny',
    'tocItem', # since ?
    'transpose',
    'transposedCueDuring',
    'transposition',
    'treCorde',
    'tuplet', # since 2.18
    'tupletDown',
    'tupletNeutral',
    'tupletUp',
    'tweak',
    'unaCorda',
    'unfoldRepeats',
    'unHideNotes',
    'unit',
    'unset',
    'versus',
    'virga',
    'virgula',
    'voiceFour',
    'voiceFourStyle',
    'voiceNeutralStyle',
    'voiceOne',
    'voiceOneStyle',
    'voiceThree',
    'voiceThreeStyle',
    'voiceTwo',
    'voiceTwoStyle',
    'walkerHeads',
    'walkerHeadsMinor',
    'whiteTriangleMarkup',
    'withMusicProperty',
)

dynamics = (
    #'p',
    'pp',
    'ppp',
    'pppp',
    'ppppp',
    #'f',
    'ff',
    'fff',
    'ffff',
    'fffff',
    'mf',
    'mp',
    'sf',
    'sff',
    'sfp',
    'sfz',
    'sp',
    'spp',
    'rfz',
    'fp',
    'fz',  
    'cr',
    'cresc',
    'crescHairpin',
    'crescTextCresc',
    'decr',
    'decresc',
    'dim',
    'dimHairpin',
    'dimTextDecr',
    'dimTextDecresc',
    'dimTextDim',
    '<',
    '>',
    '!',
)

articulations = (
    'accent',
    'espressivo',
    'marcato',
    'portato',
    'staccatissimo',
    'staccato',
    'tenuto',
)

ornaments = (
    'prall',
    'mordent',
    'prallmordent',
    'turn',
    'upprall',
    'downprall',
    'upmordent',
    'downmordent',
    'lineprall',
    'prallprall',
    'pralldown',
    'prallup',
    'reverseturn',
    'trill',
)
   
fermatas = (
    'shortfermata',
    'fermata',
    'longfermata',
    'verylongfermata',
)

instrument_scripts = (
    'upbow',
    'downbow',
    'flageolet',
    'thumb',
    'snappizzicato',
    'open',
    'halfopen',
    'stopped',
    'lheel',
    'rheel',
    'ltoe',
    'rtoe',
)

repeat_scripts = (
    'segno',
    'coda',
    'varcoda',
)

ancient_scripts = (
    'ictus',
    'accentus',
    'circulus',
    'semicirculus',
    'signumcongruentiae',
)

modes = (
    'major',     
    'minor',     
    'ionian',    
    'dorian',    
    'phrygian',  
    'lydian',    
    'mixolydian',
    'aeolian',   
    'locrian',   
)


markupcommands_nargs = (
# no arguments
(
    'doubleflat',
    'doublesharp',
    'eyeglasses',
    'flat',
    'natural',
    'null',
    'semiflat',
    'semisharp',
    'sesquiflat',
    'sesquisharp',
    'sharp',
    'strut',
    'table-of-contents'
),
# one argument
(
    'backslashed-digit',
    'bold',
    'box',
    'bracket',
    'caps',
    'center-align',
    'center-column',
    'char',
    'circle',
    'column',
    'concat',
    'dir-column',
    'draw-dashed-line', # since 2.18
    'draw-dotted-line', # since 2.18
    'draw-line',
    'dynamic',
    'fill-line',
    'finger',
    'fontCaps',
    'fret-diagram',
    'fret-diagram-terse',
    'fret-diagram-verbose',
    'fromproperty',
    'harp-pedal',
    'hbracket',
    'hspace',
    'huge',
    'italic',
    'justify',
    'justify-field',
    'justify-string',
    'large',
    'larger',
    'left-align',
    'left-brace',
    'left-column',
    'line',
    'lookup',
    'markalphabet',
    'markletter',
    'medium',
    'musicglyph',
    'normalsize',
    'normal-size-sub',
    'normal-size-super',
    'normal-text',
    'number',
    'oval', # since 2.18
    'postscript',
    'right-align',
    'right-brace',
    'right-column',
    'roman',
    'rounded-box',
    'sans',
    'score',
    'simple',
    'slashed-digit',
    'small',
    'smallCaps',
    'smaller',
    'stencil',
    'sub',
    'super',
    'teeny',
    'text',
    'tied-lyric',
    'tiny',
    'transparent',
    'triangle',
    'typewriter',
    'underline',
    'upright',
    'vcenter',
    'vspace',
    'verbatim-file',
    'whiteout',
    'wordwrap',
    'wordwrap-field',
    'wordwrap-string',
),
# two arguments
(
    'abs-fontsize',
    'auto-footnote', # since 2.16
    'combine',
    'customTabClef',
    'fontsize',
    'footnote',
    'fraction',
    'halign',
    'hcenter-in',
    'lower',
    'magnify',
    'note',
    'on-the-fly',
    'override',
    'pad-around',
    'pad-markup',
    'pad-x',
    'page-link',
    'path',     # added in LP 2.13.31
    'raise',
    'rotate',
    'scale',
    'translate',
    'translate-scaled',
    'with-color',
    'with-link',
    'with-url',
    'woodwind-diagram',
),
# three arguments
(
    'arrow-head',
    'beam',
    'draw-circle',
    'epsfile',
    'filled-box',
    'general-align',
    'note-by-number',
    'pad-to-box',
    'page-ref',
    'with-dimensions',
),
# four arguments
(
    'pattern',
    'put-adjacent',
),
# five arguments,
(
    'fill-with-pattern',
),
)

markupcommands = sum(markupcommands_nargs, ())

markuplistcommands = (
    'column-lines',
    'justified-lines',
    'override-lines',
    'wordwrap-internal',
    'wordwrap-lines',
    'wordwrap-string-internal',
)

contexts = (
    'ChoirStaff',
    'ChordNames',
    'CueVoice',
    'Devnull',
    'DrumStaff',
    'DrumVoice',
    'Dynamics',
    'FiguredBass',
    'FretBoards',
    'Global',
    'GrandStaff',
    'GregorianTranscriptionStaff',
    'GregorianTranscriptionVoice',
    'KievanStaff', # since 2.16
    'KievanVoice', # since 2.16
    'Lyrics',
    'MensuralStaff',
    'MensuralVoice',
    'NoteNames',
    'NullVoice',     # since 2.18
    'PetrucciStaff', # since 2.16
    'PetrucciVoice', # since 2.16
    'PianoStaff',
    'RhythmicStaff',
    'Score',
    'Staff',
    'StaffGroup',
    'TabStaff',
    'TabVoice',
    'Timing',
    'VaticanaStaff',
    'VaticanaVoice',
    'Voice',
)

midi_instruments = (
    # (1-8 piano)
    'acoustic grand',
    'bright acoustic',
    'electric grand',
    'honky-tonk',
    'electric piano 1',
    'electric piano 2',
    'harpsichord',
    'clav',
    # (9-16 chrom percussion)
    'celesta',
    'glockenspiel',
    'music box',
    'vibraphone',
    'marimba',
    'xylophone',
    'tubular bells',
    'dulcimer',
    # (17-24 organ)
    'drawbar organ',
    'percussive organ',
    'rock organ',
    'church organ',
    'reed organ',
    'accordion',
    'harmonica',
    'concertina',
    # (25-32 guitar)
    'acoustic guitar (nylon)',
    'acoustic guitar (steel)',
    'electric guitar (jazz)',
    'electric guitar (clean)',
    'electric guitar (muted)',
    'overdriven guitar',
    'distorted guitar',
    'guitar harmonics',
    # (33-40 bass)
    'acoustic bass',
    'electric bass (finger)',
    'electric bass (pick)',
    'fretless bass',
    'slap bass 1',
    'slap bass 2',
    'synth bass 1',
    'synth bass 2',
    # (41-48 strings)
    'violin',
    'viola',
    'cello',
    'contrabass',
    'tremolo strings',
    'pizzicato strings',
    'orchestral harp', # till LilyPond 2.12 was this erroneously called: 'orchestral strings'
    'timpani',
    # (49-56 ensemble)
    'string ensemble 1',
    'string ensemble 2',
    'synthstrings 1',
    'synthstrings 2',
    'choir aahs',
    'voice oohs',
    'synth voice',
    'orchestra hit',
    # (57-64 brass)
    'trumpet',
    'trombone',
    'tuba',
    'muted trumpet',
    'french horn',
    'brass section',
    'synthbrass 1',
    'synthbrass 2',
    # (65-72 reed)
    'soprano sax',
    'alto sax',
    'tenor sax',
    'baritone sax',
    'oboe',
    'english horn',
    'bassoon',
    'clarinet',
    # (73-80 pipe)
    'piccolo',
    'flute',
    'recorder',
    'pan flute',
    'blown bottle',
    'shakuhachi',
    'whistle',
    'ocarina',
    # (81-88 synth lead)
    'lead 1 (square)',
    'lead 2 (sawtooth)',
    'lead 3 (calliope)',
    'lead 4 (chiff)',
    'lead 5 (charang)',
    'lead 6 (voice)',
    'lead 7 (fifths)',
    'lead 8 (bass+lead)',
    # (89-96 synth pad)
    'pad 1 (new age)',
    'pad 2 (warm)',
    'pad 3 (polysynth)',
    'pad 4 (choir)',
    'pad 5 (bowed)',
    'pad 6 (metallic)',
    'pad 7 (halo)',
    'pad 8 (sweep)',
    # (97-104 synth effects)
    'fx 1 (rain)',
    'fx 2 (soundtrack)',
    'fx 3 (crystal)',
    'fx 4 (atmosphere)',
    'fx 5 (brightness)',
    'fx 6 (goblins)',
    'fx 7 (echoes)',
    'fx 8 (sci-fi)',
    # (105-112 ethnic)
    'sitar',
    'banjo',
    'shamisen',
    'koto',
    'kalimba',
    'bagpipe',
    'fiddle',
    'shanai',
    # (113-120 percussive)
    'tinkle bell',
    'agogo',
    'steel drums',
    'woodblock',
    'taiko drum',
    'melodic tom',
    'synth drum',
    'reverse cymbal',
    # (121-128 sound effects)
    'guitar fret noise',
    'breath noise',
    'seashore',
    'bird tweet',
    'telephone ring',
    'helicopter',
    'applause',
    'gunshot',
    # (channel 10 drum-kits - subtract 32768 to get program no.)
    'standard kit',
    'standard drums',
    'drums',
    'room kit',
    'room drums',
    'power kit',
    'power drums',
    'rock drums',
    'electronic kit',
    'electronic drums',
    'tr-808 kit',
    'tr-808 drums',
    'jazz kit',
    'jazz drums',
    'brush kit',
    'brush drums',
    'orchestra kit',
    'orchestra drums',
    'classical drums',
    'sfx kit',
    'sfx drums',
    'mt-32 kit',
    'mt-32 drums',
    'cm-64 kit',
    'cm-64 drums',
)

#scheme_functions = (
#    'set-accidental-style',
#    'set-global-staff-size',
#    'set-octavation',
#    'set-paper-size',
#    'define-public',
#    'define-music-function',
#    'define-markup-command',
#    'empty-stencil',
#    'markup',
#    'number?',
#    'string?',
#    'pair?',
#    'ly:duration?',
#    'ly:grob?',
#    'ly:make-moment',
#    'ly:make-pitch',
#    'ly:music?',
#    'ly:moment?',
#    'ly:format',
#    'markup?',
#    'interpret-markup',
#    'make-line-markup',
#    'make-center-markup',
#    'make-column-markup',
#    'make-musicglyph-markup',
#    'color?',
#    'rgb-color',
#    'x11-color',
#)

scheme_values = (
    'UP',
    'DOWN',
    'LEFT',
    'RIGHT',
    'CENTER',
    'minimum-distance',
    'basic-distance',
    'padding',
    'stretchability',
)

header_variables = (
    'dedication',
    'title',
    'subtitle',
    'subsubtitle',
    'poet',
    'composer',
    'meter',
    'opus',
    'arranger',
    'instrument',
    'piece',
    'breakbefore',
    'copyright',
    'tagline',
    'mutopiatitle',
    'mutopiacomposer',
    'mutopiapoet',
    'mutopiaopus',
    'mutopiainstrument',
    'date',
    'enteredby',
    'source',
    'style',
    'maintainer',
    'maintainerEmail',
    'maintainerWeb',
    'moreInfo',
    'lastupdated',
    'texidoc',
    'footer',
)
    
paper_variables = (
    # fixed vertical
    'paper-height',
    'top-margin',
    'bottom-margin',
    'ragged-bottom',
    'ragged-last-bottom',
    
    # horizontal
    'paper-width',
    'line-width',
    'left-margin',
    'right-margin',
    'check-consistency',
    'ragged-right',
    'ragged-last',
    'two-sided',
    'inner-margin',
    'outer-margin',
    'binding-offset',
    'horizontal-shift',
    'indent',
    'short-indent',
    
    # flex vertical

    'markup-system-spacing',
    'score-markup-spacing',
    'score-system-spacing',
    'system-system-spacing',
    'markup-markup-spacing',
    'last-bottom-spacing',
    'top-system-spacing',
    'top-markup-spacing',
    
    # line breaking
    'max-systems-per-page',
    'min-systems-per-page',
    'system-count',
    'systems-per-page',

    # page breaking
    'blank-after-score-page-force',
    'blank-last-page-force',
    'blank-page-force',
    'page-breaking',
    'page-breaking-system-system-spacing',
    'page-count',
    
    # page numbering
    'auto-first-page-number',
    'first-page-number',
    'print-first-page-number',
    'print-page-number',
    
    # misc
    'page-spacing-weight',
    'print-all-headers',
    'system-separator-markup',
    
    # debugging
    'annotate-spacing',
    
    # different markups
    'bookTitleMarkup',
    'evenFooterMarkup',
    'evenHeaderMarkup',
    'oddFooterMarkup',
    'oddHeaderMarkup',
    'scoreTitleMarkup',
    'tocItemMarkup',
    'tocTitleMarkup',
    
    # fonts
    'fonts',
    
    # undocumented?
    #'blank-after-score-page-force',
    #'force-assignment',
    #'input-encoding',
    #'output-scale',
)

layout_variables = (
    'indent',
    'short-indent',
    'system-count',
    'line-width',
    'ragged-right',
    'ragged-last',
)

#midi_variables = (
#)

repeat_types = (
    'unfold',
    'percent',
    'volta',
    'tremolo',
)

accidental_styles = (
    'default',
    'voice',
    'modern',
    'modern-cautionary',
    'modern-voice',
    'modern-voice-cautionary',
    'piano',
    'piano-cautionary',
    'neo-modern',
    'neo-modern-cautionary',
    'neo-modern-voice',
    'neo-modern-voice-cautionary',
    'dodecaphonic',
    'teaching',
    'no-reset',
    'forget',
)

clefs_plain = (
    'alto',
    'baritone',
    'bass',
    'C',
    'F',
    'french',
    'G',
    'GG',               # since 2.19
    'mezzosoprano',
    'percussion',
    'soprano',
    'subbass',
    'tab',
    'tenor',
    'tenorG',           # since 2.19
    'treble',
    'varbaritone',
    'varC',             # since 2.19
    'varpercussion',    # since 2.19
    'violin',
)
    
clefs = clefs_plain + (
    'treble_8',
    'bass_8',
)

break_visibility = (
    'all-invisible',
    'begin-of-line-visible',
    'end-of-line-visible',
    'all-visible',
    'begin-of-line-invisible',
    'end-of-line-invisible',
    'center-invisible',
)

mark_formatters = (
    'format-mark-alphabet',
    'format-mark-barnumbers',
    'format-mark-letters',
    'format-mark-numbers',
    'format-mark-box-alphabet',
    'format-mark-box-barnumbers',
    'format-mark-box-letters',
    'format-mark-box-numbers',
    'format-mark-circle-alphabet',
    'format-mark-circle-barnumbers',
    'format-mark-circle-letters',
    'format-mark-circle-numbers',
)
