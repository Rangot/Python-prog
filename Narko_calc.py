# Данные о веществах

drugs = {
 'Amphetamine': {'dopamine': True, 
                'serotonin': False,
                'average_dosage': '100-150',
                'psycho_effect_hours': '8-10',  
                'cost_per_1_usage': '150-200'},
        'MDMA': {'dopamine': False, 
                'serotonin': True,
                'oxytocin': True,
                'average_dosage': '100-150',
                'psycho_effect_hours': '4-5',  
                'cost_per_1_usage': '700-1500'},
     'NBOMe':    {'dopamine': False, 
                'serotonin': True,
                'oxytocin': False,
                'average_dosage': '0.6 - 1.2',
                'psycho_effect_hours': '5-6',  
                'cost_per_1_usage': '300-500'}}
                

dosage_MDMA = drugs['MDMA']

print(dosage_MDMA['average_dosage'])

# Узнавать, планируют ли марафонить. Если да, сколько дней подряд.
# Если нет, то рассчитывать по одной дозе на день