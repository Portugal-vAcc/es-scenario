#!/usr/bin/env python3

_LPPR = {
  '35': [
    'ILS35:N041.13.59,934:W008.40.38,582:352',
    'ILS35C:N041.14.08,617:W008.40.40,692:352',
  ],
  '17': [
    'ILS17C:N041.14.54,316:W008.40.52,795:172',
    'ILS17:N041.15.46,433:W008.41.06,360:172',
  ],
  'ALL': [
    'AIRPORT_ALT:0'
  ],
  'DEPARTURE_CALLSIGNS': {
    'LPPT': ['SWT230P', 'RYR2093', 'RYR2095', 'RYR2695', 'TAP1921', 'TAP1923', 'TAP1925',],
    'LPFR': ['RYR5486',],
    'LPMA': ['TVF93AF', 'TVF72BN', 'TAP1711', 'TAP1713', 'EZY7585']
  },
  'DEPARTURE_FPL': {
    # all lines start with $FP{callsign}
    'LPPT': [
      ':*A:I:B738:400:LPPR:0000:0000:190:LPPT:00:00:0:0::/v/:MANIK DCT XAMAX',
      ':*A:I:B738:410:LPPR:0000:0000:210:LPPT:00:00:0:0::/v/:MANIK DCT XAMAX',
      ':*A:I:B738:420:LPPR:0000:0000:230:LPPT:00:00:0:0::/v/:MANIK DCT XAMAX',
    ],
    'LPFR': [
      ':*A:I:B738:410:LPPR:0000:0000:210:LPFR:00:00:0:0::/v/:MANIK DCT INBOM DCT ALAGU',
      ':*A:I:B738:420:LPPR:0000:0000:230:LPFR:00:00:0:0::/v/:MANIK DCT INBOM DCT ALAGU',
      ':*A:I:B738:430:LPPR:0000:0000:250:LPFR:00:00:0:0::/v/:MANIK DCT INBOM DCT ALAGU',
    ],
    'LPMA': [
      ':*A:I:B738:440:LPPR:0000:0000:350:LPMA:00:00:0:0::/v/:MANIK LAMDI VERAM LIDRO',
      ':*A:I:B738:450:LPPR:0000:0000:370:LPMA:00:00:0:0::/v/:MANIK LAMDI VERAM LIDRO',
      ':*A:I:B738:460:LPPR:0000:0000:390:LPMA:00:00:0:0::/v/:MANIK LAMDI VERAM LIDRO',
    ]
  },
  'STANDS': [
    '41.235583:-8.672527', # S31
    '41.233771:-8.671489', # S10
    '41.235090:-8.672796', # S30
    '41.234244:-8.671844', # S11
    '41.234460:-8.672510', # S12
    '41.235954:-8.672310', # S32
    '41.236432:-8.672290', # S33
    '41.236915:-8.672479', # S34
    '41.237402:-8.672606', # S35
    '41.237795:-8.672871', # S36
    '41.237973:-8.673596', # S37
    '41.238739:-8.673894', # S50
    '41.238922:-8.673973', # S51
    '41.239034:-8.673816', # S52
    '41.239257:-8.673210', # S53
    '41.239814:-8.673009', # S54
    '41.239920:-8.672956', # S55
    '41.240143:-8.672934', # S56
    '41.241052:-8.673391', # S70
    '41.241483:-8.673596', # S71
    '41.241739:-8.673598', # S72
    '41.241919:-8.673718', # S73
    '41.241959:-8.676768', # S66
    '41.241644:-8.676615', # S65
    '41.241272:-8.676561', # S64
    '41.240935:-8.676510', # S63
    '41.240584:-8.676395', # S62
    '41.240248:-8.676302', # S61
    '41.239905:-8.676219', # S60
    '41.238531:-8.675887', # S43
    '41.237920:-8.675738', # S42
    '41.237417:-8.675598', # S41
    '41.236900:-8.675438', # S40
    '41.235698:-8.675066', # S25
    '41.235347:-8.674977', # S24
    '41.234981:-8.674888', # S23
    '41.234630:-8.674799', # S22
    '41.234253:-8.674633', # S21
  ],
  'ARRIVAL_CALLSIGNS': {
    'LPPT': ['TAP1920','TAP1921','TAP1922',],
	'LEMD': ['IBE9154', 'TAP1923']
  },
  'ARRIVAL_FPL': {
    'LPPT': [
      (':*A:I:B738:364:LPPT:0000:0000:20000:LPPR:00:00:0:0::/v/:INBOM DCT ABLEG', 'INBOM'),
    ],
	'LEMD': [
      (':*A:I:B738:440:LEMD:0000:0000:32000:LPPR:00:00:0:0::/v/:BARDI DCT RIVRO DCT VIS DCT PESUL ', 'RIVRO'),
      (':*A:I:B738:460:LEMD:0000:0000:34000:LPPR:00:00:0:0::/v/:BARDI RIVRO VIS PESUL ', 'RIVRO'),
    ]
  },
  'ARRIVAL_ROUTES': {
    'RIVRO': ['PESUL PR662 AKULU',],
	'INBOM': ['ABLEG PR653 AKULU',]
  },
  'ARRIVAL_POSITIONS': {
    'RIVRO': '40.620256:-6.724482',
	'INBOM': '40,124342:-8,334573',
  },
  'ARRIVAL_STARS': {
	'35':{
		'LPPT':'ABLEG:7000',
		'LEMD':'PESUL:7000',
		},
	'17':{
		'LPPT':'ABLEG:8000',
		'LEMD':'PESUL:7000',
	},
  }
}

_LPCS = {
  '35': ['ILS35:N038.43.09,278:W009.21.11,250:352'],
  '17': ['ILS17:N038.43.52,511:W009.21.26,903:172'],
  'ALL': [
    'AIRPORT_ALT:0'
  ],
  'DEPARTURE_CALLSIGNS': {
    'LPCS': ['CSADX', 'CSTEY', 'CSVFD',],
  },
  'DEPARTURE_FPL': {
    'LPCS': [':*A:V:C172:90:LPCS:0000:0000:010:LPCS:00:00:0:0::/v/:LOCAL CIRCUITS',]
  },
  'STANDS': [
    '38.725372:-9.354353', # A1 
    '38.725134:-9.354050', # A2 
    '38.724975:-9.354076', # A3 
    '38.725265:-9.354176', # A4 
    '38.723855:-9.353511', # B1 
    '38.723542:-9.353423', # B2 
    '38.723603:-9.353148', # B3 
    '38.723879:-9.353178', # B4 
    '38.724646:-9.357280', # D1 
    '38.725171:-9.357455', # D2 
    '38.721762:-9.357786', # E1 
    '38.721438:-9.357775', # E2 
    '38.722123:-9.357792', # E4 
    # '38.721547:-9.357157', # HSUL
  ]
}

AIRPORT_SETTINGS = {
  'LPPR': _LPPR,
  'LPCS': _LPCS,
}