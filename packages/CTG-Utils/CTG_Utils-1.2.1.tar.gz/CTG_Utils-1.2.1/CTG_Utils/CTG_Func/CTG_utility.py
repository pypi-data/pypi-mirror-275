def parse_date(s,year):

    # Standard library imports
    import re
    from datetime import datetime 

    convert_to_date = lambda s: datetime.strptime(s,"%Y_%m_%d")
    s = re.sub(r"-","_",s)
    
    try:
        pattern = re.compile(r"(?P<year>\b\d{4}_)(?P<month>\d{1,2}_)(?P<day>\d{1,2})")
        match = pattern.search(s)
        date = convert_to_date(match.group("year")+match.group("month")+match.group("day"))
    except:
        pattern = re.compile(r"(?P<month>\d{1,2}_)(?P<day>\d{1,2})")
        match = pattern.search(s)
        date = convert_to_date(str(year)+'_'+match.group("month")+match.group("day"))
    
    return date

def day_of_the_date(day,month,year):

    # Standard library imports
    import itertools
    from calendar import monthrange
    
    # Compute the day of the week of the date after "Elementary Number Theory David M. Burton Chap 6.4" [1]
    days_dict = {0: 'dimanche',
                 1: 'Lundi',
                 2: 'mardi',
                 3: 'mercredi',
                 4: 'jeudi',
                 5: 'vendredi',
                 6: 'samedi'}

    #month_dict = dict(zip(itertools.islice(itertools.cycle(l:=range(1,13)),2,2+len(l)),l))
    month_dict = {3: 1, 4: 2, 5: 3, 6: 4, 7: 5,
                  8: 6, 9: 7, 10: 8, 11: 9, 12:
                  10, 1: 11, 2: 12} # [1] p. 125
    
    y = year%100
    c = int(year/100)
    m = month_dict[month]
    if m>10 : y = y-1

    return days_dict[(day + int(2.6*m - 0.2) - 2*c + y + int(c/4) + int(y/4))%7] # [1] thm 6.12
    
def parse_date(s,year):
    
    # Standard library imports
    import re
    from datetime import datetime 

    convert_to_date = lambda s: datetime.strptime(s,"%Y_%m_%d")
    s = re.sub(r"-","_",s)
    
    try:
        pattern = re.compile(r"(?P<year>\b\d{4}_)(?P<month>\d{1,2}_)(?P<day>\d{1,2})")
        match = pattern.search(s)
        date = convert_to_date(match.group("year")+match.group("month")+match.group("day"))
    except:
        pattern = re.compile(r"(?P<month>\d{1,2}_)(?P<day>\d{1,2})")
        match = pattern.search(s)
        date = convert_to_date(str(year)+'_'+match.group("month")+match.group("day"))
    
    return date
    
def day_of_the_date(day,month,year):
    # Compute the day of the week of the date after "Elementary Number Theory David M. Burton Chap 6.4" [1]
    
    
    days_dict = {0: 'Sunday',
                 1: 'Monday',
                 2: 'Tuesday',
                 3: 'Wednesday',
                 4: 'Thursday',
                 5: 'Friday',
                 6: 'Saturday'}

    month_dict = {3: 1, 4: 2, 5: 3, 6: 4, 7: 5,
                  8: 6, 9: 7, 10: 8, 11: 9, 12:
                  10, 1: 11, 2: 12} # [1] p. 125
    
    y = year%100
    c = int(year/100)
    m = month_dict[month]
    if m>10 : y = y-1

    return days_dict[(day + int(2.6*m - 0.2) - 2*c + y + int(c/4) + int(y/4))%7] # [1] thm 6.12

def yamlinfo_randos2df(ctg_path,year):
    
    # Standard library imports
    import os
    from pathlib import Path

    # 3rd party imports
    import pandas as pd
    
    # Reads the yaml file
    info_path = ctg_path / Path(str(year)) / Path('DATA') / Path('info_randos.xlsx')
    
    
    df = pd.read_excel(info_path)
    
    return df
    
def get_sejour_info(ctg_path,year):

    # Standard library imports 
    from collections import namedtuple
    from collections import Counter
    
    sejour_info = namedtuple('sejour_info', 'nbr_jours nbr_sejours histo')
    df =  yamlinfo_randos2df(ctg_path,year)
    info_sejour = df.query('type=="sejour"')['nbr_jours'].tolist()
    
    c = Counter()
    c = Counter(info_sejour)

    
    sejour_info_tup = sejour_info( sum(info_sejour),len(info_sejour),c)
    
    return sejour_info_tup
    
def get_cout_total(year,type_sejour,dg,ctg_path):
    ''' Calcul du coût total des randonnées (type='randonnee") ou des séjours (type="sejour") pour l'année year
    '''
    # Standard library imports
    from pathlib import Path
    
    # Third party import
    import pandas as pd
    
    file_info = Path(ctg_path) / Path(str(year)) / Path('DATA') / Path('info_randos.xlsx')
    df_indo = pd.read_excel(file_info)
    cout_total = 0
    for evenement in dg.index:
        date_rando = f"{str(year)[2:4]}-{evenement[0:5].replace('_','-')}"
        cout_rando = df_indo.query('date==@date_rando and type==@type_sejour')['Cout'].tolist()[0]
        nbr_participants = dg[evenement]
        cout_total += cout_rando * nbr_participants
        
    return cout_total