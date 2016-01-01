import StringIO,csv

'''
Data from

https://data.gov.uk/dataset/england-nhs-connecting-for-health-organisation-data-service-data-files-of-nhsorganisations

'''

buf=StringIO.StringIO('''00C,NHS DARLINGTON CCG
00D,"NHS DURHAM DALES, EASINGTON AND SEDGEFIELD CCG"
00F,NHS GATESHEAD CCG
00G,NHS NEWCASTLE NORTH AND EAST CCG
00H,NHS NEWCASTLE WEST CCG
00J,NHS NORTH DURHAM CCG
00K,NHS HARTLEPOOL AND STOCKTON-ON-TEES CCG
00L,NHS NORTHUMBERLAND CCG
00M,NHS SOUTH TEES CCG
00N,NHS SOUTH TYNESIDE CCG
00P,NHS SUNDERLAND CCG
00Q,NHS BLACKBURN WITH DARWEN CCG
00R,NHS BLACKPOOL CCG
00T,NHS BOLTON CCG
00V,NHS BURY CCG
00W,NHS CENTRAL MANCHESTER CCG
00X,NHS CHORLEY AND SOUTH RIBBLE CCG
00Y,NHS OLDHAM CCG
01A,NHS EAST LANCASHIRE CCG
01C,NHS EASTERN CHESHIRE CCG
01D,"NHS HEYWOOD, MIDDLETON AND ROCHDALE CCG"
01E,NHS GREATER PRESTON CCG
01F,NHS HALTON CCG
01G,NHS SALFORD CCG
01H,NHS CUMBRIA CCG
01J,NHS KNOWSLEY CCG
01K,NHS LANCASHIRE NORTH CCG
01M,NHS NORTH MANCHESTER CCG
01N,NHS SOUTH MANCHESTER CCG
01R,NHS SOUTH CHESHIRE CCG
01T,NHS SOUTH SEFTON CCG
01V,NHS SOUTHPORT AND FORMBY CCG
01W,NHS STOCKPORT CCG
01X,NHS ST HELENS CCG
01Y,NHS TAMESIDE AND GLOSSOP CCG
02A,NHS TRAFFORD CCG
02D,NHS VALE ROYAL CCG
02E,NHS WARRINGTON CCG
02F,NHS WEST CHESHIRE CCG
02G,NHS WEST LANCASHIRE CCG
02H,NHS WIGAN BOROUGH CCG
02M,NHS FYLDE & WYRE CCG
02N,"NHS AIREDALE, WHARFEDALE AND CRAVEN CCG"
02P,NHS BARNSLEY CCG
02Q,NHS BASSETLAW CCG
02R,NHS BRADFORD DISTRICTS CCG
02T,NHS CALDERDALE CCG
02V,NHS LEEDS NORTH CCG
02W,NHS BRADFORD CITY CCG
02X,NHS DONCASTER CCG
02Y,NHS EAST RIDING OF YORKSHIRE CCG
03A,NHS GREATER HUDDERSFIELD CCG
03C,NHS LEEDS WEST CCG
03D,"NHS HAMBLETON, RICHMONDSHIRE AND WHITBY CCG"
03E,NHS HARROGATE AND RURAL DISTRICT CCG
03F,NHS HULL CCG
03G,NHS LEEDS SOUTH AND EAST CCG
03H,NHS NORTH EAST LINCOLNSHIRE CCG
03J,NHS NORTH KIRKLEES CCG
03K,NHS NORTH LINCOLNSHIRE CCG
03L,NHS ROTHERHAM CCG
03M,NHS SCARBOROUGH AND RYEDALE CCG
03N,NHS SHEFFIELD CCG
03Q,NHS VALE OF YORK CCG
03R,NHS WAKEFIELD CCG
03T,NHS LINCOLNSHIRE EAST CCG
03V,NHS CORBY CCG
03W,NHS EAST LEICESTERSHIRE AND RUTLAND CCG
03X,NHS EREWASH CCG
03Y,NHS HARDWICK CCG
04C,NHS LEICESTER CITY CCG
04D,NHS LINCOLNSHIRE WEST CCG
04E,NHS MANSFIELD AND ASHFIELD CCG
04F,NHS MILTON KEYNES CCG
04G,NHS NENE CCG
04H,NHS NEWARK & SHERWOOD CCG
04J,NHS NORTH DERBYSHIRE CCG
04K,NHS NOTTINGHAM CITY CCG
04L,NHS NOTTINGHAM NORTH AND EAST CCG
04M,NHS NOTTINGHAM WEST CCG
04N,NHS RUSHCLIFFE CCG
04Q,NHS SOUTH WEST LINCOLNSHIRE CCG
04R,NHS SOUTHERN DERBYSHIRE CCG
04V,NHS WEST LEICESTERSHIRE CCG
04X,NHS BIRMINGHAM SOUTH AND CENTRAL CCG
04Y,NHS CANNOCK CHASE CCG
05A,NHS COVENTRY AND RUGBY CCG
05C,NHS DUDLEY CCG
05D,NHS EAST STAFFORDSHIRE CCG
05F,NHS HEREFORDSHIRE CCG
05G,NHS NORTH STAFFORDSHIRE CCG
05H,NHS WARWICKSHIRE NORTH CCG
05J,NHS REDDITCH AND BROMSGROVE CCG
05L,NHS SANDWELL AND WEST BIRMINGHAM CCG
05N,NHS SHROPSHIRE CCG
05P,NHS SOLIHULL CCG
05Q,NHS SOUTH EAST STAFFORDSHIRE AND SEISDON PENINSULA CCG
05R,NHS SOUTH WARWICKSHIRE CCG
05T,NHS SOUTH WORCESTERSHIRE CCG
05V,NHS STAFFORD AND SURROUNDS CCG
05W,NHS STOKE ON TRENT CCG
05X,NHS TELFORD AND WREKIN CCG
05Y,NHS WALSALL CCG
06A,NHS WOLVERHAMPTON CCG
06D,NHS WYRE FOREST CCG
06F,NHS BEDFORDSHIRE CCG
06H,NHS CAMBRIDGESHIRE AND PETERBOROUGH CCG
06K,NHS EAST AND NORTH HERTFORDSHIRE CCG
06L,NHS IPSWICH AND EAST SUFFOLK CCG
06M,NHS GREAT YARMOUTH AND WAVENEY CCG
06N,NHS HERTS VALLEYS CCG
06P,NHS LUTON CCG
06Q,NHS MID ESSEX CCG
06T,NHS NORTH EAST ESSEX CCG
06V,NHS NORTH NORFOLK CCG
06W,NHS NORWICH CCG
06Y,NHS SOUTH NORFOLK CCG
07G,NHS THURROCK CCG
07H,NHS WEST ESSEX CCG
07J,NHS WEST NORFOLK CCG
07K,NHS WEST SUFFOLK CCG
07L,NHS BARKING AND DAGENHAM CCG
07M,NHS BARNET CCG
07N,NHS BEXLEY CCG
07P,NHS BRENT CCG
07Q,NHS BROMLEY CCG
07R,NHS CAMDEN CCG
07T,NHS CITY AND HACKNEY CCG
07V,NHS CROYDON CCG
07W,NHS EALING CCG
07X,NHS ENFIELD CCG
07Y,NHS HOUNSLOW CCG
08A,NHS GREENWICH CCG
08C,NHS HAMMERSMITH AND FULHAM CCG
08D,NHS HARINGEY CCG
08E,NHS HARROW CCG
08F,NHS HAVERING CCG
08G,NHS HILLINGDON CCG
08H,NHS ISLINGTON CCG
08J,NHS KINGSTON CCG
08K,NHS LAMBETH CCG
08L,NHS LEWISHAM CCG
08M,NHS NEWHAM CCG
08N,NHS REDBRIDGE CCG
08P,NHS RICHMOND CCG
08Q,NHS SOUTHWARK CCG
08R,NHS MERTON CCG
08T,NHS SUTTON CCG
08V,NHS TOWER HAMLETS CCG
08W,NHS WALTHAM FOREST CCG
08X,NHS WANDSWORTH CCG
08Y,NHS WEST LONDON CCG
09A,NHS CENTRAL LONDON (WESTMINSTER) CCG
09C,NHS ASHFORD CCG
09D,NHS BRIGHTON AND HOVE CCG
09E,NHS CANTERBURY AND COASTAL CCG
09F,"NHS EASTBOURNE, HAILSHAM AND SEAFORD CCG"
09G,NHS COASTAL WEST SUSSEX CCG
09H,NHS CRAWLEY CCG
09J,"NHS DARTFORD, GRAVESHAM AND SWANLEY CCG"
09L,NHS EAST SURREY CCG
09N,NHS GUILDFORD AND WAVERLEY CCG
09P,NHS HASTINGS AND ROTHER CCG
09W,NHS MEDWAY CCG
09X,NHS HORSHAM AND MID SUSSEX CCG
09Y,NHS NORTH WEST SURREY CCG
10A,NHS SOUTH KENT COAST CCG
10C,NHS SURREY HEATH CCG
10D,NHS SWALE CCG
10E,NHS THANET CCG
10G,NHS BRACKNELL AND ASCOT CCG
10H,NHS CHILTERN CCG
10J,NHS NORTH HAMPSHIRE CCG
10K,NHS FAREHAM AND GOSPORT CCG
10L,NHS ISLE OF WIGHT CCG
10M,NHS NEWBURY AND DISTRICT CCG
10N,NHS NORTH & WEST READING CCG
10Q,NHS OXFORDSHIRE CCG
10R,NHS PORTSMOUTH CCG
10T,NHS SLOUGH CCG
10V,NHS SOUTH EASTERN HAMPSHIRE CCG
10W,NHS SOUTH READING CCG
10X,NHS SOUTHAMPTON CCG
10Y,NHS AYLESBURY VALE CCG
11A,NHS WEST HAMPSHIRE CCG
11C,"NHS WINDSOR, ASCOT AND MAIDENHEAD CCG"
11D,NHS WOKINGHAM CCG
11E,NHS BATH AND NORTH EAST SOMERSET CCG
11H,NHS BRISTOL CCG
11J,NHS DORSET CCG
11M,NHS GLOUCESTERSHIRE CCG
11N,NHS KERNOW CCG
11T,NHS NORTH SOMERSET CCG
11X,NHS SOMERSET CCG
12A,NHS SOUTH GLOUCESTERSHIRE CCG
12D,NHS SWINDON CCG
12F,NHS WIRRAL CCG
12G,"CHESHIRE, WARRINGTON AND WIRRAL COMMISSIONING HUB"
12H,"DURHAM, DARLINGTON AND TEES COMMISSIONING HUB"
12J,GREATER MANCHESTER COMMISSIONING HUB
12K,LANCASHIRE COMMISSIONING HUB
12L,MERSEYSIDE COMMISSIONING HUB
12M,"CUMBRIA, NORTHUMBERLAND, TYNE AND WEAR COMMISSIONING HUB"
12N,NORTH YORKSHIRE AND HUMBER COMMISSIONING HUB
12P,SOUTH YORKSHIRE AND BASSETLAW COMMISSIONING HUB
12Q,WEST YORKSHIRE COMMISSIONING HUB
12R,"ARDEN, HEREFORDSHIRE AND WORCESTERSHIRE COMMISSIONING HUB"
12T,BIRMINGHAM AND THE BLACK COUNTRY COMMISSIONING HUB
12V,DERBYSHIRE AND NOTTINGHAMSHIRE COMMISSIONING HUB
12W,EAST ANGLIA COMMISSIONING HUB
12X,ESSEX COMMISSIONING HUB
12Y,HERTFORDSHIRE AND THE SOUTH MIDLANDS COMMISSIONING HUB
13A,LEICESTERSHIRE AND LINCOLNSHIRE COMMISSIONING HUB
13C,SHROPSHIRE AND STAFFORDSHIRE COMMISSIONING HUB
13G,"BATH, GLOUCESTERSHIRE, SWINDON AND WILTSHIRE COMMISSIONING HUB"
13H,"BRISTOL, NORTH SOMERSET, SOMERSET AND SOUTH GLOUCESTERSHIRE COMMISSIONING HUB"
13J,"DEVON, CORNWALL AND ISLES OF SCILLY COMMISSIONING HUB"
13K,KENT AND MEDWAY COMMISSIONING HUB
13L,SURREY AND SUSSEX COMMISSIONING HUB
13M,THAMES VALLEY COMMISSIONING HUB
13N,WESSEX COMMISSIONING HUB
13P,NHS BIRMINGHAM CROSSCITY CCG
13Q,NATIONAL COMMISSIONING HUB 1
13R,LONDON COMMISSIONING HUB
13T,NHS NEWCASTLE GATESHEAD CCG
13V,YORKSHIRE AND HUMBER COMMISSIONING HUB
13W,LANCASHIRE AND GREATER MANCHESTER COMMISSIONING HUB
13X,CUMBRIA AND NORTH EAST COMMISSIONING HUB
13Y,CHESHIRE AND MERSEYSIDE COMMISSIONING HUB
14A,NORTH MIDLANDS COMMISSIONING HUB
14C,WEST MIDLANDS COMMISSIONING HUB
14D,CENTRAL MIDLANDS COMMISSIONING HUB
14E,EAST COMMISSIONING HUB
14F,SOUTH WEST COMMISSIONING HUB
14G,SOUTH EAST COMMISSIONING HUB
14H,SOUTH CENTRAL COMMISSIONING HUB
99A,NHS LIVERPOOL CCG
99C,NHS NORTH TYNESIDE CCG
99D,NHS SOUTH LINCOLNSHIRE CCG
99E,NHS BASILDON AND BRENTWOOD CCG
99F,NHS CASTLE POINT AND ROCHFORD CCG
99G,NHS SOUTHEND CCG
99H,NHS SURREY DOWNS CCG
99J,NHS WEST KENT CCG
99K,NHS HIGH WEALD LEWES HAVENS CCG
99M,NHS NORTH EAST HAMPSHIRE AND FARNHAM CCG
99N,NHS WILTSHIRE CCG
99P,"NHS NORTHERN, EASTERN AND WESTERN DEVON CCG"
99Q,NHS SOUTH DEVON AND TORBAY CCG''')

ccg_=dict()
reader=csv.reader(buf)
for i in reader:
  ccg_[i[0]]=i[1]


def name(x):
  return ccg_[x]

def ccgs():
  return set(ccg_)